import requests

def get_weather(city):
    # Your OpenWeatherMap API key here
    api_key = "05f73d400e5eaff5b0deb5d23f27ef93"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the complete API URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"  # The `units=metric` will give the temperature in Celsius
    
    # Send the HTTP request to the API
    response = requests.get(complete_url)
    
    # Convert the response to JSON format
    data = response.json()
    
    # If the response contains valid data
    if data["cod"] == 200:
        # Extract relevant data from the JSON response
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        # Print out the weather data
        print(f"Weather in {city}:")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Weather: {weather_data['description']}")
        print(f"Humidity: {main_data['humidity']}%")
    else:
        # If the city was not found
        print("City not found or invalid API request.")

# Ask the user for input
city = input("Enter city name: ")
get_weather(city)
