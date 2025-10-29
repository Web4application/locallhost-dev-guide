import asyncio, os, uuid, tornado.web, tornado.escape
from tornado.options import define, options, parse_command_line
from tornado.locks import Condition

define("port", default=int(os.environ.get("PORT", 8888)), type=int)
define("debug", default=True)

class MessageBuffer:
    def __init__(self):
        self.cond = Condition()
        self.cache = []
        self.cache_size = 200

    def get_messages_since(self, cursor):
        results = []
        for msg in reversed(self.cache):
            if msg["id"] == cursor: break
            results.append(msg)
        results.reverse()
        return results

    def add_message(self, message):
        self.cache.append(message)
        if len(self.cache) > self.cache_size:
            self.cache = self.cache[-self.cache_size:]
        self.cond.notify_all()

global_message_buffer = MessageBuffer()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=global_message_buffer.cache)

class MessageNewHandler(tornado.web.RequestHandler):
    def post(self):
        message = {"id": str(uuid.uuid4()), "body": self.get_argument("body")}
        message["html"] = tornado.escape.to_unicode(
            self.render_string("message.html", message=message)
        )
        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)
        global_message_buffer.add_message(message)

class MessageUpdatesHandler(tornado.web.RequestHandler):
    async def post(self):
        cursor = self.get_argument("cursor", None)
        messages = global_message_buffer.get_messages_since(cursor)
        while not messages:
            self.wait_future = global_message_buffer.cond.wait()
            try: await self.wait_future
            except asyncio.CancelledError: return
            messages = global_message_buffer.get_messages_since(cursor)
        if self.request.connection.stream.closed(): return
        self.write(dict(messages=messages))
    def on_connection_close(self):
        self.wait_future.cancel()

async def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/a/message/new", MessageNewHandler),
            (r"/a/message/updates", MessageUpdatesHandler),
        ],
        cookie_secret=os.environ.get("COOKIE_SECRET", "__TODO:_GENERATE__"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=options.debug,
    )
    app.listen(options.port)
    print(f"Tornado chat running on port {options.port}")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
