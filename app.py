from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual API key
api_key = "e9559cbb6c0e8d0ad0665e4e96531af8"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None

    if request.method == 'POST':
        city = request.form['city']
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather = {
                    'city': city.title(),
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'].title(),
                    'humidity': data['main']['humidity'],
                    'wind': data['wind']['speed'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                error = "City not found. Please try again."
        else:
            error = "Please enter a city name."

    return render_template('index.html', weather=weather, error=error)
    
if __name__ == '__main__':
    app.run(debug=True)
