from django.shortcuts import render
import cv2
from django.http import StreamingHttpResponse, HttpResponse
import requests

NGROK_CAMERA_URL = " https://dfe6-129-2-89-208.ngrok-free.app/vid_feed"

def forward_camera_feed(request):
    try:
        stream = requests.get(NGROK_CAMERA_URL, stream=True, timeout=5)
        return StreamingHttpResponse(stream.iter_content(chunk_size=1024),
                                     content_type=stream.headers['Content-Type'])
    except Exception as e:
        print(f"Camera stream error: {e}")
        return HttpResponse("Camera unavailable", status=503)
