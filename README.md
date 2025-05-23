# Junior Node Operator – Technical Assignment   -- By Wenbo Jiao
Thank you for reviewing this submission. If you need any further information, feel free to contact me at wbj0706@gmail.com at any time.

This repository contains my completed submission for the **Gateway.fm Junior Node Operator** technical assignment.

The assignment includes 4 main tasks and 1 optional bonus task. Each task is organized into a clearly labeled folder with associated code, configuration files, and screenshots.

---

## 📁 Repository Structure

```
├── 1.basic_linux_knowledge.md       # Answers to basic Linux CLI questions
├── 2.hoodi-node/                    # Ethereum node setup using Docker Compose
│   ├── docker-compose.yml
│   ├── README.md
│   ├── geth-syncing-progress.png
│   └── ...
├── 3.RPC-Endpoint/                  # Python script to call eth_syncing method
│   ├── rpc_call.py
│   ├── output.txt
│   └── README.md
├── 4.Coding-Task/                   # Python script to check status of nodes
│   ├── nodes.txt
│   ├── status_checker.py
│   ├── report.txt
│   └── README.md
├── Bonus-Task(Monitoring)/         # Option C: Prometheus + Grafana setup
│   ├── docker-compose.yml
│   ├── prometheus.yml
│   ├── json-config.yml
│   ├── prometheus-up-status.png
│   ├── grafana-lighthouse-async-tasks.png
│   ├── successful setup.png
│   └── README.md
└── README.md                        # (You are here)
```

---

## ✅ Task Overview

### 1. Basic Linux Knowledge

Provided answers to 5 Linux system administration questions, including process listing, curl, chmod, chown, and journalctl usage.  
📄 See: `1.basic_linux_knowledge.md`

---

### 2. Ethereum Node Setup (Hoodi Testnet)

Used **Geth** (EL) and **Lighthouse** (CL) to run a full Ethereum node connected to the Hoodi testnet via Docker Compose.  
📁 See: `2.hoodi-node/`

---

### 3. Calling RPC Endpoint

Wrote a Python script to call the `eth_syncing` method on the local Geth node (`http://localhost:8545`).  
📁 See: `3.RPC-Endpoint/`

---

### 4. Coding Task: Node Availability Checker

Script reads a list of node URLs and writes a report (`UP`/`DOWN`) based on their HTTP 200 response.  
📁 See: `4.Coding-Task/`

---

### 5. Bonus Task (Option C): Monitoring

Set up **Prometheus** and **Grafana** to collect metrics from both Geth and Lighthouse nodes:
- Geth: via `json-exporter` probing `/debug/vars`
- Lighthouse: native Prometheus metrics at `/metrics`

📁 See: `Bonus-Task(Monitoring)/`

---

## 📦 Submission Format

- All tasks are modularized by folder
- Configurations and scripts are clearly documented
- Screenshots are included to demonstrate working setups

---


