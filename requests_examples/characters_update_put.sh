#!/bin/bash

API_URL="http://localhost:5000"
TOKEN="coloque_seu_token_aqui"
CHARACTER_ID="coloque_o_id_aqui"

curl -X PUT "$API_URL/my-characters/$CHARACTER_ID" \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "name": "Aragorn II",
  "class": "Rei",
  "level": 20
}'

echo -e "\n✅ Personagem atualizado (PUT)"
