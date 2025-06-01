#!/bin/bash

API_URL="http://localhost:5000"

TOKEN="coloque_seu_token_aqui"

curl -X GET "http://localhost:5000/auth/me" \
-H "Authorization: Bearer $TOKEN"

echo -e "\n✅ Dados do usuário retornados"
