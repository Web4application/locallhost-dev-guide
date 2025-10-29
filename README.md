# 🌐 Locallhost Development Environment Guide

 A comprehensive reference for configuring and managing your local web development environment.

This guide helps you set up and manage **frontend**, **backend**, and **database** development environments efficiently — covering everything from port assignments to troubleshooting.

---

## 🖥️ Frontend Development Ports

| Port | Purpose | Frameworks |
|------|----------|-------------|
| 3000 | React Dev Server | React, Next.js |
| 5173 | Vite Dev Server | Vue.js, React, Svelte |
| 4200 | Angular Dev Server | Angular CLI |
| 3001 | Alternate React | React, Next.js |
| 4201 | Alternate Angular | Angular |

🔗 [Frontend Guide →](./docs/frontend.md)

---

## ⚙️ Backend Development Ports

| Port | Purpose | Frameworks |
|------|----------|-------------|
| 8080 | Spring Boot | Java, Microservices |
| 8000 | Python Dev | Django, FastAPI |
| 5000 | Flask/Node | Flask, Express.js |
| 9000 | Alt Backend | Microservices |
| 8081 | Alt Spring Boot | Java |
| 5001 | Alt Python | Django, Flask |

🔗 [Backend Guide →](./docs/backend.md)

---

## 🗄️ Database Ports

| Port | Database | Type |
|------|-----------|------|
| 3306 | MySQL | Relational |
| 5432 | PostgreSQL | Relational |
| 27017 | MongoDB | NoSQL |
| 1433 | SQL Server | Relational |
| 1521 | Oracle | Relational |
| 6379 | Redis | Cache |
| 11211 | Memcached | Cache |

🔗 [Database Guide →](./docs/databases.md)

---

## 🔧 Troubleshooting

- [Port Already in Use](./docs/troubleshooting/port-in-use.md)
- [Connection Refused Errors](./docs/troubleshooting/connection-refused.md)
- [CORS Issues](./docs/troubleshooting/cors-errors.md)
- [Localhost Not Working](./docs/troubleshooting/localhost-troubleshooting.md)

---

## 🧠 Best Practices

✅ **Port Management:**  
- Use environment variables for configurable ports  
- Document all port usage in your README  
- Avoid hard-coding ports in production builds  

🔒 **Security Tips:**  
- Keep dev databases local only  
- Use `.env` files and never commit secrets  
- Apply HTTPS locally when testing APIs  

⚡ **Performance:**  
- Enable caching where possible  
- Use Docker for reproducible setups  
- Monitor system resources with `htop` or `docker stats`

---

## 📦 Example Dev Setup

Example Docker Compose setup for a simple Python + PostgreSQL stack:

```yaml
version: "3"
services:
  web:
    build: ./backend
    ports:
      - "8000:8000"
    env_file: .env
  db:
    image: postgres
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: devpass

locallhost-dev-guide/
├── guides/
│   ├── frontend-ports.md
│   ├── backend-ports.md
│   ├── database-ports.md
│   ├── common-issues.md
│   └── best-practices.md
├── assets/
│   └── diagrams/
├── .gitignore
├── README.md
├── LICENSE
└── mkdocs.yml  # optional if you host as a doc site
```

# 🌐 Locallhost.dev — Development Environment Configuration Guide

Setting up a proper development environment is crucial for efficient web development.  
This guide helps you configure ports, servers, databases, and frameworks for a seamless setup.

---

## 🖥️ Frontend Development Ports

| Port | Default Use | Frameworks |
|------|--------------|-------------|
| **3000** | React Development Server | React, Next.js |
| **5173** | Vite Development Server | Vue, React, Svelte |
| **4200** | Angular Development Server | Angular CLI |
| **3001** | Alternative React Port | React, Next.js |
| **4201** | Alternative Angular Port | Angular |

👉 [View Full Frontend Port Guide](guides/frontend-ports.md)

---

## ⚙️ Backend Development Ports

| Port | Default Use | Frameworks |
|------|--------------|-------------|
| **8080** | Spring Boot Default | Java, Spring Boot |
| **8000** | Python Development | FastAPI, Django, Flask |
| **5000** | Flask & Node.js | Express, Flask |
| **9000** | Alternative Backend Port | General Use |
| **8081** | Alt Spring Boot | Java, Spring Boot |

👉 [View Full Backend Guide](guides/backend-ports.md)

---

## 🗄️ Database Ports

| Port | Database | Description |
|------|-----------|-------------|
| **3306** | MySQL | Default MySQL/MariaDB |
| **5432** | PostgreSQL | Default Postgres |
| **27017** | MongoDB | Default MongoDB |
| **6379** | Redis | In-memory cache |
| **11211** | Memcached | Cache layer |

👉 [View Database Port Guide](guides/database-ports.md)

---

## 🔧 Common Development Issues

- **Port already in use** → [Fix Guide](guides/common-issues.md#port-already-in-use)
- **Connection refused**
- **CORS errors**
- **Localhost not working**

---

## 💡 Best Practices
- Use environment variables for port config.
- Document ports in README.
- Don’t expose dev databases to the internet.
- Use connection pooling for DBs.

---

## 🧠 About
This project is maintained as a public developer reference under **MIT License**.  
Inspired by *Locallhost.dev* — A modern handbook for local dev environments.

Contributions welcome! 🧑‍💻
