#!/bin/bash

curl -X POST "http://localhost:5000/auth/register" \
-H "Content-Type: application/json" \
-d '{
  "name": "ana",
  "email": "ana@example.com",
  "password": "senha123"
}'

echo -e "\n✅ Registro realizado"
