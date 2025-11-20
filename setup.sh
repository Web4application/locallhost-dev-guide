#!/bin/bash
set -e
echo "Creating virtual env, installing Python deps..."
python3 -m venv venv || true
. venv/bin/activate
pip install -r backend/requirements.txt
echo "Starting Flask app (port 8080)..."
cd backend
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8080
