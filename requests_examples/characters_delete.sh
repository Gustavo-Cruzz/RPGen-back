#!/bin/bash

API_URL="http://localhost:5000"
TOKEN="coloque_seu_token_aqui"
CHARACTER_ID="coloque_o_id_aqui"

curl -X DELETE "$API_URL/characters/$CHARACTER_ID" \
-H "Authorization: Bearer $TOKEN"

echo -e "\n✅ Personagem deletado"
