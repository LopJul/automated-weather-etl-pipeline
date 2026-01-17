import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "data", "weather.db")
TABLE_NAME = "helsinki_daily_weather"

def load_to_sqlite(df):
  os.makedirs(os.path.join(base_dir, "data"), exist_ok=True)
  db_exists = os.path.exists(db_path)

  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()

  if not db_exists:
    print("Creating new database and table")
    cursor.execute(f"""
    CREATE TABLE {TABLE_NAME} (
      date TEXT,
      timestamp_utc TEXT,
      city TEXT,
      temperature REAL,
      humidity INTEGER,
      wind_speed REAL,
      weather_description TEXT,
      UNIQUE(timestamp_utc, city)
    )
    """)
    conn.commit()
  else:
    print("Database already exists.")

  for _, row in df.iterrows():
        cursor.execute(f"""
        INSERT OR IGNORE INTO {TABLE_NAME} 
        (date, timestamp_utc, city, temperature, humidity, wind_speed, weather_description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            row['date'],
            row['timestamp_utc'],
            row['city'],
            row['temperature'],
            row['humidity'],
            row['wind_speed'],
            row['weather_description']
        ))

  conn.commit()

  conn.close()
  print(f"{len(df)} rows processed and duplicates ignored")