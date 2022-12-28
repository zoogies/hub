# hub

[![wakatime](https://wakatime.com/badge/github/Yoyolick/hub.svg)](https://wakatime.com/badge/github/Yoyolick/hub)

a central hub for all of my live projects

---

## Setup

Docker Compose:

```yml
version: '3'
services:
  api:
    image: ghcr.io/yoyolick/api:latest
    ports:
      - 5505:5055
    volumes:
      - host-storage:container-path
    restart: unless-stopped
  gui:
    image: ghcr.io/yoyolick/hub:latest
    ports:
      - 3303:3000
    restart: unless-stopped
    depends_on:
      - api
```