from django.shortcuts import render
import requests
# Create your views here.
def tempapp(request):
    city = 'Visakhapatnam'
    city = request.GET.get("city")
    apikey = 'aec0b5b07abbb0e1d66672777e380557'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
    response = requests.get(url)
    resp = response.json()

    payload = {
        "City" : resp["name"],
        "weather" : resp["weather"][0]["main"], 
        "Kelvin" : (int (resp["main"]["temp"])),
        "celcius" : (int (resp["main"]["temp"])) - 273,
        "weatherIcon" : resp["weather"][0]["icon"]

    }

    context = {"resp":payload}
    
    return render(request,"index.html",context)


