# arch labs

## Lab 1 - Docker

#### Run
docker compose up --build

#### Endpoint
http://localhost:8080/api/v1/get

## Lab 2 - Redis and TTL

#### Setup
1. `docker compose up --build`
2. In another terminal to see logs: `docker compose logs -f api-demo`

#### Access
- Swagger (FastAPI): http://localhost:8080/docs
- View TTL: `docker exec -it keydb keydb-cli`

## Lab 3 - RabbitMQ

#### Setup
1. `docker compose up --build`
2. Run consumer.py
3. Create a POST request with a new user and watch logs

#### Access
- Swagger: http://localhost:8080/docs
- RabbitMQ Dashboard: http://localhost:15672 (guest:guest)

## Lab 4 - Monitoring and Alerts

#### Setup
1. `docker compose up --build`

#### Access
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin:admin)
- AlertManager: http://localhost:9093
- Prometheus Alerts: http://localhost:9090/alerts

#### Configuration
- To change RabbitMQ dashboard panel: go to http://localhost:15672 → Queues and Streams → test-dashboard → publish message

## Lab 5 - CQRS and Event Sourcing

#### Setup
1. `docker compose up --build`

#### Access
- Swagger (FastAPI): http://localhost:8080/docs

#### Usage
1. Create account: UUID (e.g., 5a955866-3a68-4fae-b117-87a972dd9a46)
2. Operations: Credit → Debit → Get Balance → Get History