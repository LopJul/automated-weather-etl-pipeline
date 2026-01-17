import pandas as pd
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def weatherdata_to_dataframe(weather_data):
  now_utc = datetime.now(timezone.utc)
  now_helsinki = datetime.now(ZoneInfo("Europe/Helsinki"))
  row = {
    "date": now_helsinki.date().isoformat(),
    "timestamp_utc": now_utc.isoformat(),
    "city": weather_data["name"],
    "temperature": weather_data["main"]["temp"],
    "humidity": weather_data["main"]["humidity"],
    "wind_speed": weather_data["wind"]["speed"],
    "weather_description": weather_data["weather"][0]["description"]
  }

  return pd.DataFrame([row])