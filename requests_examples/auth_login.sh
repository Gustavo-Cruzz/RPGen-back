#!/bin/bash

curl -X POST "http://localhost:5000/auth/login" \
-H "Content-Type: application/json" \
-d '{
  "email": "ana@example.com",
  "password": "senha123"
}'

echo -e "\n✅ Login realizado"
