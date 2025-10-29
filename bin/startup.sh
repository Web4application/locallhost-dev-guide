#!/bin/bash
echo "Starting Tomcat Dev Environment..."

# Kill default ports if used
npx kill-port 8080 8443 8009

# Start Tomcat
$CATALINA_HOME/bin/startup.sh

echo "Tomcat started!"
echo "HTTP: http://localhost:8080"
echo "HTTPS: https://localhost:8443"
echo "Service 1: http://service1.local:8080"
echo "Service 2: http://service2.local:8080"
