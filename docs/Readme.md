# 🌐 Locallhost Development Environment Guide

> A comprehensive reference for configuring and managing your local web development environment.

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

```

```rust
Start Angular on port 4201:
ng serve --port 4201
npm start -- --port 4201
Find what's using port 4201:
lsof -i :4201 (Mac/Linux)
netstat -ano | findstr :4201 (Windows)
Kill process on port 4201:
kill -9 $(lsof -t -i:4201) (Mac/Linux)
for /f "tokens=5" %a in ('netstat -aon ^| findstr :4201') do taskkill /PID %a /F (Windows)
Check Angular version:
ng version
npm list @angular/core
About Port 4201

Port 4201 is commonly used for:

Angular backup - When port 4200 is busy
Multiple Angular apps - Running simultaneously
Development testing - Different versions
Ionic backup - Mobile app development
Angular workspaces - Multiple projects
Common Use Cases

Running multiple Angular applications during development
Testing different versions of the same Angular app
Micro-frontends architecture with multiple Angular apps
Angular workspace with multiple projects
Development and testing environments running in parallel
🔄 Angular Multi-Port Development

Managing multiple Angular applications and development scenarios on different ports

Multiple Application Setup

ng serve --port 4200 - Main application
ng serve --port 4201 - Secondary application
ng serve --port 4202 - Third application
Configure different environments
Set up proxy configurations
Development Workflows

Feature branch development
Parallel development testing
Version comparison testing
Micro-frontend development
Team collaboration scenarios
Port Management

Automatic port detection
Manual port assignment
Port conflict resolution
Port range configuration
Environment-specific ports
Testing & Quality

Cross-application testing
Integration testing setup
Performance comparison
Browser compatibility testing
Load testing scenarios
📁 Angular Workspace Management

Managing Angular workspaces with multiple projects and applications

Workspace Configuration

ng new my-workspace --create-application=false
ng generate application app1 - Create app
ng generate library my-lib - Create library
Configure angular.json for multiple apps
Set up shared dependencies
Multi-Application Development

ng serve app1 --port 4200
ng serve app2 --port 4201
Shared component libraries
Common styling and themes
Unified build processes
Library Development

ng build my-lib - Build library
ng test my-lib - Test library
Library versioning strategies
Publishing to npm registry
Library documentation
Deployment Strategies

Individual app deployment
Monorepo deployment
Shared asset management
Environment configuration
CI/CD pipeline setup
🎯 Angular Development Scenarios

Common development scenarios and solutions for port 4201

Feature Development

Isolated feature development:

Create feature branch for new functionality
Run development server on port 4201
Test feature independently
Compare with main application
Integration testing before merge
Version Testing

Testing different versions:

Run current version on port 4200
Run new version on port 4201
Side-by-side comparison
Performance benchmarking
User acceptance testing
Team Collaboration

Multi-developer scenarios:

Different developers on different ports
Code review and testing
Shared development environment
Conflict resolution strategies
Team development workflows
Micro-Frontend Development

Micro-frontend architecture:

Independent micro-applications
Shared component libraries
Module federation setup
Cross-application communication
Unified deployment strategy
⚙️ Angular Configuration & Optimization

Advanced configuration and optimization for Angular applications on port 4201

angular.json Configuration

Configure multiple serve targets
Set default ports for applications
Configure build optimizations
Set up proxy configurations
Environment-specific settings
Performance Tuning

Optimize change detection
Configure bundle splitting
Set up lazy loading
Optimize template compilation
Configure caching strategies
Development Tools

Configure source maps
Set up debugging tools
Configure hot reload
Set up testing frameworks
Configure linting rules
Environment Management

Environment-specific configurations
API endpoint management
Feature flag configuration
Build optimization settings
Deployment configurations
Related Angular & Frontend Ports

Port 4200 - Primary Angular development port
Port 3000 - React development server
Port 8080 - Backend API server
Port 5173 - Vite.js development server
📋 Port 4201 Development Summary

Port 4201 serves as a strategic backup and alternative development port for Angular applications, enabling developers to run multiple Angular applications simultaneously or handle port conflicts efficiently. It's particularly valuable for complex development scenarios involving feature branches, version testing, team collaboration, and micro-frontend architectures.

Understanding how to effectively manage multiple Angular applications across different ports, configure workspaces, and implement advanced development workflows is essential for modern Angular development teams. Port 4201 provides the flexibility needed for sophisticated development scenarios while maintaining the same powerful development features as the primary port 4200.

