from zeep import Client

def convert_energy(kw_value):
    try:
        # Usamos uma API SOAP pública de câmbio para simular energia
        client = Client("https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL")
        result = client.service.NumberToWords(int(kw_value))

        return {
            "energia_solar_kW": kw_value,
            "energia_convertida_simulada": result
        }

    except Exception as e:
        return {"erro": str(e)}
