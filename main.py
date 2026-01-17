from extract_weatherdata import get_weatherdata
from pipeline_weather import weatherdata_to_dataframe
from load_weatherdata import load_to_sqlite

def main():
    weather_data = get_weatherdata()
    if not weather_data:
        print("Error while fetching weather data")
        return
    
    df = weatherdata_to_dataframe(weather_data)

    print(f"City:", weather_data["name"])
    print(f"Description:", weather_data ["weather"][0]["main"])
    print("Temperature:", weather_data["main"]["temp"], "°C")
    print("Humidity:", weather_data["main"]["humidity"], "%")
    print("Wind:", weather_data["wind"]["speed"], "m/s")

    load_to_sqlite(df)

    print("Data loaded succesfully!")

if __name__ == "__main__":
    main()