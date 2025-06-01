#!/bin/bash

API_URL="http://localhost:5000"
TOKEN="coloque_seu_token_aqui"
CHARACTER_ID="coloque_o_id_aqui"

curl -X PATCH "$API_URL/characters/$CHARACTER_ID" \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "level": 10
}'

echo -e "\n✅ Personagem atualizado (PATCH)"
