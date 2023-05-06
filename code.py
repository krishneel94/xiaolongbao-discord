import os
import subprocess
import re
import requests
import json


DISCORD_WEBHOOK_URL = "YOUR WEBHOOK HERE"


# Change directory to the directory of the Python script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

command1 = ["docker-compose", "logs", "--tail=1000"]
process1 = subprocess.Popen(command1, stdout=subprocess.PIPE)
command2 = ["grep", "join code"]
process2 = subprocess.Popen(command2, stdin=process1.stdout, stdout=subprocess.PIPE)
output = process2.communicate()[0]

# Split the output by line and get the last element
most_recent_line = output.decode().splitlines()[-1]
#print(most_recent_line)

# Search for the join code pattern in the most recent line
match = re.search(r'join code (\d+)', most_recent_line)

# Check if a match was found and print the join code
if match:
    join_code = match.group(1)
    print(f"Join code found: {join_code}")

    payload = {
    "username": "Valheim-Homie",
    "content": f"Join code found: {join_code}"
}
else:
    print("Join code not found.")
    payload = {
    "username": "Valheim-Homie",
    "content": "Join code not found, please try again!"
}

# Send the payload to Discord
response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

# Check if the request was successful
if response.status_code == 204:
    print("Message sent successfully!")
else:
    print("Error sending message to Discord.")