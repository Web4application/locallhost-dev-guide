import asyncio
import tornado.ioloop
import tornado.web
import tornado.escape
import os
import uuid
from tornado.options import define, options, parse_command_line

# Configuration flags
define("port", default=8888, help="Run on given port", type=int)
define("debug", default=True, help="Run in debug mode")

class MessageBuffer:
    def __init__(self, cache_size=200):
        self.cond = tornado.locks.Condition()
        self.cache = []
        self.cache_size = cache_size

    def get_messages_since(self, cursor_id):
        results = []
        for msg in reversed(self.cache):
            if msg["id"] == cursor_id:
                break
            results.append(msg)
        results.reverse()
        return results

    def add_message(self, message):
        self.cache.append(message)
        if len(self.cache) > self.cache_size:
            self.cache = self.cache[-self.cache_size :]
        # Notify any waiting readers
        self.cond.notify_all()

# Global buffer
global_message_buffer = MessageBuffer()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            messages=global_message_buffer.cache,
            xsrf_token=self.xsrf_token
        )

class MessageNewHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username", "Anonymous")
        body = self.get_argument("body", "").strip()
        if not body:
            self.set_status(400)
            self.write({"error": "Empty message"})
            return

        message = {
            "id": str(uuid.uuid4()),
            "username": tornado.escape.xhtml_escape(username),
            "body": tornado.escape.xhtml_escape(body),
        }
        message["html"] = tornado.escape.to_unicode(
            self.render_string("message.html", message=message)
        )

        global_message_buffer.add_message(message)

        self.set_header("Content-Type", "application/json")
        self.write(message)

class MessageUpdatesHandler(tornado.web.RequestHandler):
    async def post(self):
        cursor = self.get_argument("cursor", None)
        messages = global_message_buffer.get_messages_since(cursor)
        while not messages:
            # Wait for new messages
            try:
                await global_message_buffer.cond.wait()
            except asyncio.CancelledError:
                # request was closed
                return
            # After waking up
            messages = global_message_buffer.get_messages_since(cursor)

        # If connection is closed, do nothing
        if self.request.connection.stream.closed():
            return

        self.set_header("Content-Type", "application/json")
        self.write({"messages": messages})

    def on_connection_close(self):
        try:
            self.wait_future.cancel()
        except Exception:
            pass

async def main():
    parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", MainHandler),
            (r"/a/message/new", MessageNewHandler),
            (r"/a/message/updates", MessageUpdatesHandler),
        ],
        cookie_secret=os.environ.get("COOKIE_SECRET", str(uuid.uuid4())),
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=options.debug,
    )
    app.listen(options.port)
    print(f"[locallhost.dev] Chat server running at http://localhost:{options.port}")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
