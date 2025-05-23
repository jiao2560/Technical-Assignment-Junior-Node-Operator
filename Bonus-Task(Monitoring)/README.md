# Bonus Task (Monitoring) – Gateway.fm Technical Assessment

## ✅ Objective

Set up **Prometheus** and **Grafana** to monitor an Ethereum node (Geth + Lighthouse) on the Hoodi testnet, and demonstrate successful metrics collection.

## 📦 Folder Contents

- `docker-compose.yml` – Launches Prometheus, Grafana, and JSON Exporter services (connected to your Ethereum node)
- `prometheus.yml` – Prometheus scrape config for Lighthouse and JSON-exported Geth metrics
- `json-config.yml` – JSON Exporter config to extract Geth metrics from `/debug/vars`
- `grafana-lighthouse-async-tasks.png` – Grafana panel showing `async_tasks_count` from Lighthouse
- `prometheus-up-status.png` – Prometheus query confirming Geth and Lighthouse are both up
- `successful setup.png` – Docker Desktop screenshot showing all containers running

## 🚀 How to Run

1. Ensure your Ethereum node (`geth` and `lighthouse`) is running using Docker with correct port exposure.
2. In this folder, run:

   ```bash
   docker-compose up -d
   ```

3. Access:
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000  
     Login: `admin` / `admin` (you’ll be prompted to change password)

4. In Grafana:
   - Add a new **Prometheus data source**: `http://prometheus:9090`
   - Create panels for metrics like `async_tasks_count`

## 📊 Monitored Metrics

- `up{job="geth"}` and `up{job="lighthouse"}` confirm the node services are online
- `async_tasks_count` shows per-service task metrics from Lighthouse
- Geth metrics (like `geth_heap_alloc`) are exposed via JSON Exporter at `/debug/vars`

## ✅ Result

- All monitoring components are running and integrated
- Metrics from both clients are actively collected and visualized in Grafana
- Submission includes screenshots and configuration demonstrating successful setup
