# Hoodi Testnet Node Setup

This project sets up an Ethereum node on the **Hoodi (Sepolia)** testnet using **Docker Compose**, with:

- **Execution Layer**: Geth (`ethereum/client-go`)
- **Consensus Layer**: Lighthouse (`sigp/lighthouse`)

Tested on **Ubuntu running under WSL on Windows**, using Docker Desktop with WSL2 integration.

## Files Provided

- `docker-compose.yml`: Docker configuration for Geth and Lighthouse.
- `jwt/jwt.hex`: Shared JWT secret for EL ↔ CL authentication.
- `docker-containers-running.png`: Screenshot showing containers active in Docker Desktop.
- `docker-ps-output.png`: Terminal output from `docker ps` confirming containers are running.
- `geth-syncing-progress.png`: Shows `eth_syncing` output as Geth begins syncing.

## Running the Node

1. Ensure Docker is installed and running.
2. From the project directory, run:
   ```bash
   docker-compose up -d
   ```

## Verifying the Setup

### 1. Check Geth Syncing

Run:
```bash
curl -X POST http://localhost:8545 \
  -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'
```

- For the first few minutes (e.g. 3–5 minutes), the output may show `"currentBlock": "0x0"` — this is expected while the node connects to peers.
- When syncing starts, you’ll see `currentBlock` and `highestBlock` values increasing.
- A response of `false` means syncing is fully complete.

### 2. Check Lighthouse Health

Run:
```bash
curl http://localhost:5052/eth/v1/node/health
```

- This may return nothing if Geth is not yet syncing.
- Wait until Geth shows syncing progress, then check Lighthouse.
- Once healthy, it should return HTTP `200 OK`.

## Notes

- JWT secret was generated via:
  ```bash
  openssl rand -hex 32 > jwt/jwt.hex
  ```
- Volume paths are relative; containers mount `./jwt` and data directories for Geth and Lighthouse.

## Status

- Geth and Lighthouse are both running and communicating over the Engine API.
- Node is actively syncing on the Sepolia network.
