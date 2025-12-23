import requests
import smtplib
from datetime import datetime

MY_LAT = 21.901840
MY_LONG =  83.348267
EMAIL = "gadhavirushiraj7@gmail.com"
PASSWORD = "nnea krgu xbyn hqut"

request = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
data = request.json()

latitude = data["latitude"]
longitude = data["longitude"]

live_location = (latitude, longitude)


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.send_message(msg="Subject:ISS is near you!\n\nWake up and look into the sky ISS is near you in the space", from_addr=EMAIL, to_addrs=EMAIL)

if (latitude-5<=MY_LAT<=longitude+4 and longitude-5<=MY_LONG<=longitude+5) or True:
    sunrise_response = requests.get(f"https://api.sunrisesunset.io/json?lat={MY_LAT}&lng={MY_LONG}")
    sunrise_data = sunrise_response.json()
    sunrise_time = str(sunrise_data['results']["sunrise"]).split(" ")[0].split(":")[0]
    sunset_time = str(sunrise_data["results"]["sunset"]).split(" ")[0].split(":")[0]

    now = datetime.now()
    current_hours = now.hour

    if int(sunset_time)<current_hours<int(sunrise_time):
        send_mail()