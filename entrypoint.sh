#!/bin/bash
set -e

echo "Running script"
echo -e "$EE_PRIVATE_KEY" | base64 -d > privatekey.pem
exec python main.py $1
