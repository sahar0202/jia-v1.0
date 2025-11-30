#!/bin/bash
echo "--- Meluncurkan Vault (Ghost Heart)"
docker run -d --cap-add=IPC_LOCK --name jia-vault -p 8200:8200 \
-e 'VAULT_DEV_ROOT_TOKEN_ID=mydevtoken' vault:latest

echo "--- Meluncurkan ChromaDB (Ingatan Lokal)"
docker run -d -p 8002:8000 --name jia-chromadb chromadb/chroma

echo "--- Meluncurkan Tool Dispatcher (Demon Hand)"
docker build -t jia-tools-sender ./03_TOOL_DISPATCHER
docker run -d -p 8001:8001 --name jia-tools jia-tools-sender:latest

echo "✅ Semua service lokal aktif. Vault: http://localhost:8200"
