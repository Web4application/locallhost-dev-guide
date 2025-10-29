# Start a simple react vite project
npm create vite@latest my-app --template react
cd my-app
npm install
npm run dev # opens on 5173 by default

      default port often 5000
      
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port=5000

            default port 8080 (changeable via application.properties)

        # override port when starting
java -jar app.jar --server.port=8081port
          
