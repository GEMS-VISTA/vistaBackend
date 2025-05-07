from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import serial
import requests

BRIDGE_URL =  " https://058f-129-2-89-208.ngrok-free.app" # or https://<ngrok-url> if using ngrok

@api_view(['POST'])
def led_on(request):
    print("LED ON request received")
    try:
        response = requests.post(f"{BRIDGE_URL}/led/on")
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        print(f"Failed to reach bridge: {e}")
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def led_off(request):
    print("LED OFF request received")
    try:
        response = requests.post(f"{BRIDGE_URL}/led/off")
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        print(f"Failed to reach bridge: {e}")
        return JsonResponse({'error': str(e)}, status=500)
