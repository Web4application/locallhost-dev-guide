git clone https://github.com/Web4application/locallhost-dev-guide.git
cd locallhost-dev-guide
chmod +x scripts/*.sh
./scripts/push-to-github.sh

lsof -i :PORT            # (Mac/Linux) find what's using a port
netstat -ano | findstr :PORT # (Windows) find what's using a port
kill -9 PID                  # (Mac/Linux) kill a process by PID
taskkill /PID PID /F         # (Windows) kill a process by PID
nc -zv localhost PORT        # (Mac/Linux) check if port is open
telnet localhost PORT        # (Windows/Linux) check if port is open
python -m http.server PORT   # start a simple HTTP server (python)
npx http-server -p PORT      # start simple static server (node)
          
