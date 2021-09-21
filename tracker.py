import json
import requests
import os
import time

def updateAPI():
    global LocationAPI
    global AstronautAPI
    LocationAPI = requests.get("http://api.open-notify.org/iss-now.json")
    AstronautAPI = requests.get("http://api.open-notify.org/astros.json")

def clear():
    os.system('clear')

def trackLocation():
    longitude = LocationAPI.json()['iss_position']['longitude']
    latitude = LocationAPI.json()['iss_position']['latitude']
    print("\nCurrent Coordinates of the ISS is: latitude("+latitude+") longitude("+longitude+")")

def trackAstronauts():
    astronauts = AstronautAPI.json()['people']
    number = AstronautAPI.json()['number']
    print("\n There are " + str(number) + " astronauts right now on the ISS.")
    for x in range(0, len(astronauts)):
        print("\n\t" + astronauts[x]['name'])

def live():
    while True:
        updateAPI()
        clear()
        print("\n\tInternational Space Station Astronauts & Coordinates Tracker")
        trackLocation()
        trackAstronauts()

def start():
    clear()
    print("\n\tInternational Space Station Astronauts & Coordinates Tracker\n")
    print("Commands: \nlive \t\t  - Have a live feed.\nlocation \t  - Know the exact location once.\nastronauts   \t  - Know who is up in the ISS right now.\n")
    while True:
        cmd = input("\n> ")
        if(cmd.lower() == "live"):
            live()
        elif(cmd.lower() == "location"):
            updateAPI()
            trackLocation()
        elif(cmd.lower() == "astronauts"):
            updateAPI()
            trackAstronauts()

start()
