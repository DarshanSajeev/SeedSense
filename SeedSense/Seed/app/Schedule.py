"@Alexander Kibeedi"
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"daily": ["temperature_2m_max", "temperature_2m_min", "sunshine_duration", "precipitation_sum", "rain_sum"]
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
daily_sunshine_duration = daily.Variables(2).ValuesAsNumpy()
daily_precipitation_sum = daily.Variables(3).ValuesAsNumpy()
daily_rain_sum = daily.Variables(4).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}

daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min
daily_data["sunshine_duration"] = daily_sunshine_duration
daily_data["precipitation_sum"] = daily_precipitation_sum
daily_data["rain_sum"] = daily_rain_sum

daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)

for index, row in daily_dataframe.iterrows():
    print(f"Date: {row['date']}")
    print(f"Max Temperature: {row['temperature_2m_max']}°C")
    print(f"Min Temperature: {row['temperature_2m_min']}°C")
    print(f"Precipitation Sum: {row['precipitation_sum']} mm")
    print(f"Rain Sum: {row['rain_sum']} mm")
    print(f"Sunshine duration: {row['sunshine_duration']} seconds")
    print("-" * 20)

def getMaxTemp(day):
    maxTemp = daily_dataframe.iloc[day]['temperature_2m_max']
    return maxTemp

def getMinTemp(day):
    minTemp = daily_dataframe.iloc[day]['temperature_2m_min']
    return minTemp

def getAvgTemp(day): #Check rounding 
    minTemp = daily_dataframe.iloc[day]['temperature_2m_min']
    maxTemp = daily_dataframe.iloc[day]['temperature_2m_max']
    avgTemp = minTemp+maxTemp
    avgTemp/=2
    print("Average temp is", avgTemp)
    return avgTemp

     

def getRain(day):
    maxTemp = daily_dataframe.iloc[day]['rain_sum']
    return maxTemp

def getSun(day):
    sunSeconds = daily_dataframe.iloc[day]['sunshine_duration']
    sunHours=sunSeconds/3600
    return sunHours

def getRainfallGap():
    
    rain=False
    rain_gap_count=0
    rain_gap=0
    for day in range(0,6):
        rain_sum=daily_dataframe.iloc[day]['rain_sum']
        if rain_sum>0:
            rain=True
            rain_gap_count=rain_gap
            rain_gap=0
        if rain==False:
            rain_gap+=1
            if rain_gap_count<rain_gap:
                rain_gap_count=rain_gap
    return rain_gap_count






import pandas as pd

# Load the CSV file
from app import db
from app.models import Seeds
import pandas as pd

# Query the database to get all seed data
seeds = Seeds.query.all()

# Convert the seed data to a list of dictionaries
seed_data = []
for seed in seeds:
    seed_data.append({
        "SeedId": seed.SeedId,
        "SeedName": seed.SeedName,
        "OwnerId": seed.OwnerId,
        "MinTemp": seed.MinTemp,
        "MaxTemp": seed.MaxTemp,
        "MinRain": seed.MinRain,
        "MaxRain": seed.MaxRain,
        "MinSun": seed.MinSun,
        "MaxSun": seed.MaxSun,
        "GermeTime": seed.GermeTime,
        "WaterFreq": seed.WaterFreq,
        "MineralGive": seed.MineralGive,
        "MineralTake": seed.MineralTake
    })
df = pd.DataFrame(seed_data)


#Warning messages depending on which condition not achieved
tempWarning1=("Temp too low")
tempWarning2=("Temp too high")
sunWarning1=("Sunlight hours too low")
sunWarning2=("Sunlight hours too high")
waterWarning=("Plant not watered not frequently enough")
rainWarning1=("Rainfall too low")
rainWarning2=("Rainfall too high")

userID=0
def add_notification(user_id, message):
    # Create a new notification
    notification = Notifications(UserId=user_id, Message=message)
    
    # Add the notification to the session and commit
    db.session.add(notification)
    db.session.commit()

#Check the different conditions
def checkTemp(minTemp, maxTemp, weather):
     if weather<minTemp:
          print (tempWarning1)
          add_notification(userID, tempWarning1)
     if weather>maxTemp:
          print (tempWarning2)
          add_notification(userID, tempWarning2)

def checkSunlight(minSun, maxSun, weather):
     if weather<minSun:
          print (sunWarning1)
     if weather>maxSun:
          print (sunWarning2)
          add_notification(userID, sunWarning1)
def checkWatering(waterFreq, weatherRainfallGap):
     if waterFreq<weatherRainfallGap:
          print(waterWarning)
          add_notification(userID, sunWarning2)

def checkRainfall(minRain, maxRain, weather):
    if weather<minRain:
        print(rainWarning1)
        add_notification(userID, rainWarning1)
    if weather>maxRain:
        print(rainWarning2)
        add_notification(userID, rainWarning2)




# Loop through the different seeds
for index, row in df.iterrows():
    seed_type = row["Seed Type"]
    min_temp = row["Min Temp (°C)"]
    max_temp = row["Max Temp (°C)"]
    min_rainfall = row["Min Rainfall (mm)"]
    max_rainfall = row["Max Rainfall (mm)"]
    min_sunlight = row["Min Sunlight (hours/day)"]
    max_sunlight = row["Max Sunlight (hours/day)"]
    germination_time = row["Germination Time (days)"]
    watering_frequency = row["Watering Frequency (days)"]



    

     



    for dayNo in range(0,6):
        print("------------", seed_type, "Day:", dayNo, "------------")
        checkTemp(min_temp, max_temp, getAvgTemp(dayNo))
        checkSunlight(min_sunlight, max_sunlight, getSun(dayNo))
        checkRainfall(min_rainfall, max_rainfall, getRain(dayNo))
    checkWatering(watering_frequency, getRainfallGap())