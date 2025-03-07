import requests
import json
import configparser
import time

# create ConfigParser-Object
config = configparser.ConfigParser()

# read config file
config.read('config.ini')

# Pi-hole configuration
PIHOLE_HOST = config['DEFAULT']['piHole']  # oder die IP-Adresse deines Pi-hole
API_PASSWORD = config['DEFAULT']['apiKey']  # Dein Web-Interface Passwort
BLOCK_PAUSE = config['DEFAULT'].getint('blockPause')

# Authentication
auth_response = requests.post(f"http://{PIHOLE_HOST}/api/auth", json={"password": API_PASSWORD})

if auth_response.status_code == 200:
    #print("Authentication successful")
    api_token = auth_response.json().get('session', {}).get('sid')
    
    #print (api_token)

    if api_token:
        # Deactivate PiHole for BLOCK_PAUSE seconds
        disable_response = requests.post(f"http://{PIHOLE_HOST}/api/dns/blocking", json={"blocking": False, "timer": BLOCK_PAUSE, "sid": api_token})

        if disable_response.status_code == 200:
            disableTime = disable_response.json().get('timer')

            disableTimeSec = disableTime % 60
            if disableTime > 59:
                disableTime = int(disableTime / 60)
                print(f"Pi-hole has been disabled for {disableTime}:{disableTimeSec:>02} minutes")
            else:
                print(f"Pi-hole has been disabled for {disableTimeSec} seconds")
            
        else:
            print(f"Error with deactivation request: {disable_response.status_code}")
            print(disable_response.text)

        current_session = requests.get(f"http://{PIHOLE_HOST}/api/auth/sessions", json={"sid": api_token})
        #print(current_session.text)
         
        current_session_id = None
        for session in current_session.json().get("sessions", []):
            if session.get("current_session"):
                current_session_id = session["id"]
                break
         
        if current_session_id is not None:
            requests.delete(f"http://{PIHOLE_HOST}/api/auth/session/{current_session_id}", json={"sid": api_token})
            print("...")
            time.sleep(2)
        else:
            print("No session found")
            input("Press enter to continue...")
    else:
        print("No token in response")
        input("Press enter to continue...")
else:
    print(f"Authentication error: {auth_response.status_code}")
    print(auth_response.text)
    input("Press enter to continue...")
