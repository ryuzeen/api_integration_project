from flask import Blueprint, jsonify
from service.weather_service import get_weather_data
from service.energy_service import convert_energy

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/weather/<city>', methods=['GET'])
def weather(city):
    result = get_weather_data(city)
    return jsonify(result)

@api_blueprint.route('/convert-energy/<float:kw>', methods=['GET'])
def energy_conversion(kw):
    result = convert_energy(kw)
    return jsonify(result)

@api_blueprint.route('/alert/<city>', methods=['GET'])
def unified_alert(city):
    weather = get_weather_data(city)
    if "risk" in weather and weather["risk"] in ["ALTO", "EXTREMO"]:
        alert_level = "CRÍTICO"
    else:
        alert_level = "NORMAL"

    result = {
        "cidade": city,
        "tempo": weather,
        "status_energia": convert_energy(5.0),
        "nível_alerta": alert_level
    }
    return jsonify(result)
