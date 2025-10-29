
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
