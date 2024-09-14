import requests
import json

def fetch_weather_data_by_id(city_id):
    """Fetch weather data for a given city by ID from the OpenWeather API."""
    api_key = "29e95d8ac4ec8c7f52abb22f9b426bcc"  # Updated with your new API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}"
    
    try:
        # Fetching data from OpenWeather API
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def process_weather_data(weather_data):
    """Process the weather data to extract meaningful information."""
    if weather_data is None:
        return None

    # Extracting necessary information
    city = weather_data.get("name")
    temperature_kelvin = weather_data["main"]["temp"]
    temperature_celsius = round(temperature_kelvin - 273.15, 2)
    description = weather_data["weather"][0]["description"]

    # Processed data dictionary
    processed_data = {
        "city": city,
        "temperature_celsius": temperature_celsius,
        "description": description
    }

    return processed_data

def write_data_to_file(data, filename="weather_data.json"):
    """Write processed data to a JSON file."""
    if data is None:
        print("No data to write.")
        return

    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data written to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

def main():
    """Main function to fetch, process, and save weather data."""
    # Example: Fetch weather data for Kansas City, US (City ID: 4393217)
    city_id = 4393217  # Kansas City, US
    print(f"Fetching weather data for city ID {city_id}...")

    # Fetching weather data
    weather_data = fetch_weather_data_by_id(city_id)

    # Processing the data
    processed_data = process_weather_data(weather_data)

    # Writing the processed data to a file
    write_data_to_file(processed_data, "kansas_city_weather.json")

if __name__ == "__main__":
    # This block ensures that main() is called only when this script is executed directly
    main()