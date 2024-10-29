# redis_demo

`redis_demo` is a Django project demonstrating Redis-based Pub/Sub messaging with both HTTP and WebSocket support through Django’s ASGI framework. It includes a `chat` app for real-time message broadcasting, and is fully containerized using Docker.

## Features

- **Django ASGI** setup with HTTP and WebSocket support.
- **Redis Pub/Sub** for real-time messaging.
- **Dockerized environment** for simplified setup and deployment.
- Automated superuser creation on the first run.

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pyved/redis_demo.git
   cd redis_demo
   ```
1. **Build and Run Containers**:
   ```bash
   ./start.sh
   ```

2. **Stop Containers**:
   ```bash
   ./stop.sh
   ```
