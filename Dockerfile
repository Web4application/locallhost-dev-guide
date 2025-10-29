# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by Tornado
EXPOSE 8888

# Default command to run the chat server
CMD ["python", "chat_server.py", "--port=8888"]
