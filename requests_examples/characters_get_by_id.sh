#!/bin/bash

API_URL="http://localhost:5000"
TOKEN="coloque_seu_token_aqui"
CHARACTER_ID="coloque_o_id_aqui"

curl -X GET "$API_URL/my-characters/$CHARACTER_ID" \
-H "Authorization: Bearer $TOKEN"

echo -e "\n✅ Personagem retornado por ID"
