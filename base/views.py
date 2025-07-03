from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def home(request):
    return render(request,"base/home.html")

current_wave  = "none"

@csrf_exempt
def set_wave(request):
    if request.method == "POST":
        data = json.loads(request.body)
        global current_wave
        current_wave = data.get("type","none")
        return JsonResponse({"status":"wave set","wave":current_wave})
    return JsonResponse({"error":"Only Post allowed"},status = 405)

def get_wave(request):
    return JsonResponse({"wave_type":current_wave}) 
#when esp tries to communicate with backend 
#this give esp the current wave that is which signal to generate
latest_voltage = 0.0

@csrf_exempt
def recieve_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        voltage = data.get("voltage")
        latest_voltage = voltage
        print("esp sent a voltage:",voltage)
        return JsonResponse({"status":"data recieved"})
    return JsonResponse({"error":"POST only"},status = 405)

def latest_data(request):
    return JsonResponse({"latest data":latest_voltage})

def voltage_render(request):
    return render(request,"base/voltage_display.html")
