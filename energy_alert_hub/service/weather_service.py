import requests
from data.api_keys import WEATHER_API_KEY

def get_weather_data(city):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&lang=pt"
        response = requests.get(url)
        data = response.json()

        condition = data["current"]["condition"]["text"]
        wind_kph = data["current"]["wind_kph"]
        temp_c = data["current"]["temp_c"]

        # Lógica de risco
        if wind_kph > 40 or "chuva" in condition.lower():
            risk = "ALTO"
        elif temp_c > 38:
            risk = "MODERADO"
        else:
            risk = "BAIXO"

        return {
            "cidade": data["location"]["name"],
            "condição": condition,
            "temperatura": f"{temp_c} ºC",
            "vento": f"{wind_kph} km/h",
            "risk": risk
        }

    except Exception as e:
        return {"erro": str(e)}
