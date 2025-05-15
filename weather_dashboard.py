import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


API_KEY = '4227708c05dcb910661f68eb04c9b431'
CITY = 'Mumbai,IN'


URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'


response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

   
    if 'list' in data:
       
        dates = []
        temperatures = []
        humidities = []

        for entry in data['list']:
            dt = datetime.fromtimestamp(entry['dt'])        
            temp = entry['main']['temp']                    
            humidity = entry['main']['humidity']            
            dates.append(dt)
            temperatures.append(temp)
            humidities.append(humidity)

        
        sns.set(style="darkgrid")

     
        plt.figure(figsize=(14, 6))

       
        plt.subplot(2, 1, 1)
        sns.lineplot(x=dates, y=temperatures, color="red")
        plt.title(f"Temperature Forecast for {CITY}")
        plt.ylabel("Temperature (°C)")
        plt.subplot(2, 1, 2)
        sns.lineplot(x=dates, y=humidities, color="blue")
        plt.title(f"Humidity Forecast for {CITY}")
        plt.ylabel("Humidity (%)")
        plt.xlabel("Date and Time")

        plt.tight_layout()
        plt.show()
    else:
        print("Error: Unexpected API response format. Could not find forecast data.")
else:
    print(f"Failed to get data. HTTP Status code: {response.status_code}")
