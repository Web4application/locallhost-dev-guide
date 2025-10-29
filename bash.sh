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
          
python -m http.server PORT
chmod +x dev-launcher.sh && ./dev-launcher.sh

# Check OS
OS=$(uname 2>/dev/null || echo Windows)

# Ask for port
if [ "$OS" = "Windows" ]; then
  powershell -Command "$PORT = Read-Host 'Enter port to use'; Write-Output $PORT"
  PORT=$(powershell -Command "$PORT = Read-Host 'Enter port to use'; Write-Output $PORT")
else
  read -p "Enter port to use: " PORT
fi

echo "Checking port $PORT..."

# Kill existing process on the port
npx kill-port $PORT

# Detect LAN IP
if [ "$OS" = "Darwin" ]; then
  LAN=$(ipconfig getifaddr en0 2>/dev/null)
elif [ "$OS" = "Linux" ]; then
  LAN=$(hostname -I | awk '{print $1}')
else
  # Windows PowerShell
  LAN=$(powershell -Command "(Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -notlike '*Loopback*' }).IPAddress")
fi

# Start HTTP server
npx http-server -p $PORT &

# Output URLs
echo "Server running at: http://localhost:$PORT"
echo "LAN URL: http://$LAN:$PORT"
