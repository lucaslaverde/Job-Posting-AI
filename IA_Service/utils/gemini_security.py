import hmac
import hashlib
import json
import base64
import time
from django.conf import settings

def generate_gemini_auth_headers(endpoint):
    gemini_api_key = settings.GEMINI_API_KEY
    gemini_api_secret = settings.GEMINI_API_SECRET.encode()

    # Crear un payload para la autenticación HMAC
    payload = {
        "request": endpoint,
        "nonce": int(time.time() * 1000)
    }

    encoded_payload = base64.b64encode(json.dumps(payload).encode())
    signature = hmac.new(gemini_api_secret, encoded_payload, hashlib.sha384).hexdigest()

    headers = {
        "X-GEMINI-APIKEY": gemini_api_key,
        "X-GEMINI-PAYLOAD": encoded_payload,
        "X-GEMINI-SIGNATURE": signature,
        "Content-Type": "text/plain"
    }

    return headers
