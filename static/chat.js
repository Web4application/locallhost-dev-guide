const form = document.getElementById("chat-form");
const messagesUL = document.getElementById("messages");

let lastCursor = null;

function addMessage(msg) {
  const li = document.createElement("li");
  li.innerHTML = msg.html;
  messagesUL.appendChild(li);
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const body = formData.get("body");
  const username = formData.get("username") || "Anonymous";

  await fetch("/a/message/new", {
    method: "POST",
    headers: {"X‑Requested‑With": "XMLHttpRequest"},
    body: formData
  }).then(res => res.json())
    .then(msg => {
      addMessage(msg);
      lastCursor = msg.id;
    });

  form.reset();
});

async function pollUpdates() {
  const resp = await fetch("/a/message/updates", {
    method: "POST",
    headers: {"Content‑Type": "application/x‑www‑form‑urlencoded"},
    body: `cursor=${lastCursor||""}`
  });
  const data = await resp.json();
  data.messages.forEach(addMessage);
  if (data.messages.length) {
    lastCursor = data.messages[data.messages.length-1].id;
  }
  setTimeout(pollUpdates, 1000);
}

pollUpdates();
