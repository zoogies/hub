# hub

[![wakatime](https://wakatime.com/badge/github/Yoyolick/hub.svg)](https://wakatime.com/badge/github/Yoyolick/hub)

a central hub for all of my live projects

---

## Setup

Docker Compose:

```Dockerfile
version: '3'
services:
  api:
    build: src/backend
    ports:
      - 5505:5055
    volumes:
      - ./src/backend/backups:/src/backend/backups
    restart: unless-stopped
  gui:
    build: src/frontend
    ports:
      - 3303:3000
    restart: unless-stopped
    depends_on:
      - api
```