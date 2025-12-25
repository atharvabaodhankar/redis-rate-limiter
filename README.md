# 🚀 Redis Rate Limiter

![Redis Rate Limiter Hero](./Architecture.png)

Hi there! 👋 Welcome to the **Redis Rate Limiter**.

A high-performance, lightweight, and scalable API rate limiting solution built with **FastAPI** ⚡ and **Redis** 🧠.
Designed to protect your services from abuse while maintaining blazing fast response times.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg)
![Redis](https://img.shields.io/badge/redis-7.0-red.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

---

## 🎨 Visual Architecture

```mermaid
sequenceDiagram
    participant Client
    participant API as FastAPI Server
    participant Redis as Redis Cache
    
    Client->>API: Request (w/ API Key)
    API->>Redis: INCR rate:{api_key}
    Redis-->>API: Current Count
    
    alt Count == 1
        API->>Redis: EXPIRE rate:{api_key} 10
    end
    
    alt Count <= Limit
        API->>Client: 200 OK (Success)
    else Count > Limit
        API->>Client: 429 Too Many Requests
    end