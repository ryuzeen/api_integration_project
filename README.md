
# ⚡ EnergyAlertHub

**EnergyAlertHub** é uma plataforma integrada que visa mitigar os impactos da falta de energia elétrica por meio do uso de tecnologias modernas como APIs REST e SOAP. O sistema fornece informações climáticas em tempo real, simula o aproveitamento de energia alternativa e gera alertas inteligentes baseados em condições ambientais adversas.

Este projeto foi desenvolvido como parte de um trabalho interdisciplinar do curso de Engenharia de Software, aplicando conceitos de integração de sistemas, boas práticas de arquitetura em camadas, consumo de APIs, modularidade e engenharia de software orientada a serviços.

---

## 🌟 Funcionalidades

- 🔍 **Consulta Climática** via REST API pública da WeatherAPI.
- ⚡ **Simulação de Conversão de Energia** via API SOAP (Number Conversion Service).
- 🚨 **Alerta Unificado de Risco de Apagão** com base na previsão climática e condições simuladas.

---

## 🛠️ Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ryuzeen/api_integration_project.git
   cd api_integration_project
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure a chave da WeatherAPI:**
   - Acesse: https://www.weatherapi.com/my/
   - Crie sua conta gratuita e gere uma chave de API.
   - No arquivo `data/api_keys.py`, insira a chave assim:
     ```python
     WEATHER_API_KEY = "SUA_CHAVE_AQUI"
     ```

5. **Execute o servidor Flask:**
   ```bash
   python app.py
   ```

6. **Acesse os endpoints no navegador ou via Postman/cURL:**
   - `http://localhost:5000/weather/<cidade>`  
     → Retorna o clima e risco de queda de energia.
   - `http://localhost:5000/convert-energy/<valor>`  
     → Converte um valor simulado de energia solar para "valor escrito".
   - `http://localhost:5000/alert/<cidade>`  
     → Mostra alerta unificado com base no clima e energia.

---

## 📚 Tecnologias Utilizadas

- **Python 3.10+**
- **Flask** – Framework web
- **requests** – Consumo de API REST
- **zeep** – Cliente SOAP
- **WeatherAPI** – REST pública
- **DataAccess SOAP Service** – API SOAP de simulação

---

## 👨‍💻 Integrantes

- Rafael Perussi Caczan – RM93092  
- Octávio Hernandez Chiste Cordeiro – RM97894  
- Sabrina Flores – RM550781

---

## 🧩 Motivação Interdisciplinar

Este projeto nasceu da proposta de integrar conhecimentos das disciplinas do 3º ano de Engenharia de Software, conectando tópicos como:

- **Engenharia de Requisitos e Análise de Sistemas**
- **Desenvolvimento Web e Backend**
- **Integração de APIs e Protocolos de Comunicação**
- **Boas práticas de arquitetura em camadas**
- **Responsividade frente a problemas reais da sociedade**

A escolha do tema — **queda de energia** — remete a problemas cada vez mais frequentes no Brasil, e demonstra como a tecnologia pode oferecer respostas práticas, eficientes e inteligentes a esse tipo de desafio.

---
