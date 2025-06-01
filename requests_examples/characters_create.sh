#!/bin/bash

API_URL="http://localhost:5000"
TOKEN="coloque_seu_token_aqui"

curl -X POST "$API_URL/characters" \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "name": "Aragorn",
  "class": "Ranger",
  "level": 5
}'

echo -e "\n✅ Personagem criado"
