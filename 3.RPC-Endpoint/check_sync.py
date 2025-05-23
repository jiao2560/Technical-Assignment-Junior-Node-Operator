"""
check_sync.py
-------------
This script connects to a local Ethereum node running on the Hoodi (Sepolia) testnet
and checks the syncing status using the eth_syncing RPC method.

Expected to run after completing Task 2 (node setup).
"""

import requests
import json

# RPC endpoint URL of the local Geth node
url = "http://localhost:8545"

# JSON-RPC request payload
payload = {
    "jsonrpc": "2.0",
    "method": "eth_syncing",
    "params": [],
    "id": 1
}

try:
    # Send the request
    response = requests.post(url, json=payload)
    result = response.json()

    # Pretty-print the result
    print("Response from eth_syncing:")
    print(json.dumps(result, indent=2))

except requests.exceptions.RequestException as e:
    print(f"Error connecting to {url}: {e}")
