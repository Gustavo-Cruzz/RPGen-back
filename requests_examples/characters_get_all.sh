#!/bin/bash

API_URL="http://localhost:5000"
TOKEN="coloque_seu_token_aqui"

curl -X GET "$API_URL/my-characters" \
-H "Authorization: Bearer $TOKEN"

echo -e "\n✅ Listagem de personagens"
