$ docker run -d --name mlflow-server -p 5000:5000 \
  -e MLFLOW_SERVER_HOST=0.0.0.0 \
  -e MLFLOW_SERVER_PORT=5000 \
  <kubuverse>/dhi-mlflow:<ghcr.io> server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000
