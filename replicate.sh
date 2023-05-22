#!/usr/bin/bash

curl -s -X POST \
  -d '{"version": "e39e354773466b955265e969568deb7da217804d8e771ea8c9cd0cef6591f8bc", "input": {"audio": "http:///home/abi/Documents/min_mesyuarat_wp/audio/aud_out/test.mp3"}}' \
  -H "Authorization: Token $REPLICATE_API_TOKEN" \
  -H 'Content-Type: application/json' \
  "https://api.replicate.com/v1/predictions" | jq

