from django.http import JsonResponse
import requests
from .utils.gemini_security import generate_gemini_auth_headers

GEMINI_API_URL = "https://api.gemini.com/v1"

def chatbot_gemini(request):
    user_input = request.GET.get("query")  # El input del usuario
    response_text = ""

    if "balance" in user_input:
        endpoint = "/v1/balances"
        headers = generate_gemini_auth_headers(endpoint)
        url = GEMINI_API_URL + endpoint
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            # Si la API responde con éxito
            balances = response.json()
            response_text = f"Tus balances son: {balances}"
        else:
            response_text = "No se pudo obtener el balance en este momento."
    
    elif "ordenes" in user_input:
        # Aquí un ejemplo de consulta avanzada sobre órdenes
        endpoint = "/v1/orders"
        headers = generate_gemini_auth_headers(endpoint)
        url = GEMINI_API_URL + endpoint
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            orders = response.json()
            response_text = f"Tienes las siguientes órdenes activas: {orders}"
        else:
            response_text = "No se pudieron obtener las órdenes activas."

    else:
        response_text = "No entendí tu consulta. Puedes preguntar por tu balance o por órdenes."

    return JsonResponse({"response": response_text})
