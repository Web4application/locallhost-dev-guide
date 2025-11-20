# Locallhost Dev Guide — Dark Interactive AI Edition

This project is a local, interactive developer guide that demonstrates common dev environment ports, frameworks, and troubleshooting — with an AI-powered search (client + server) and a talking avatar demo.
Built and packaged for Seriki Yakub (KUBU LEE).

## Quick start (Flask-only, zero Node)

1. Create a Python venv and install:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

2. Run the Flask app:
```bash
cd backend
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8080
```

Open http://localhost:8080

## Quick start (Docker Compose)
```bash
docker compose up --build
```

## Structure
- backend/: Flask backend and lightweight server AI
- static/: client JS/CSS for the interactive UI
- templates/: HTML template served by Flask
- frontend/: optional Vite/React skeleton (not required for core demo)
- LICENSE: Custom Locallhost Dev License v1.0
