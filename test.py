import requests
import time
import json
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore
cred = credentials.Certificate("itec2024-firebase-adminsdk-yjefv-9c193ac533.json")  # Replace with your service account key
initialize_app(cred)
db = firestore.client()

# Define the Discord webhook URL
discord_webhook_url = 'https://discord.com/api/webhooks/1226365478189010998/xRUs9oM6IcgbliDsCLoaUYuRpd8Vf-Jas73KtnhtMjdxG5QS7l53MmlcKlF1HJZ79ZYX'

# URL statuses
states = {
    'STABLE': 'Stable',
    'UNSTABLE': 'Unstable',
    'DOWN': 'Down'
}

# Function to send message to Discord webhook
def send_discord_webhook_message(content):
    payload = {'content': content}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(discord_webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        print('Webhook message sent successfully.')
    else:
        print(f'Failed to send webhook message. Status code: {response.status_code}')

# Function to monitor URL status
def monitor_url(url):
    try:
        response = requests.head(url, timeout=10)
        if response.status_code >= 200 and response.status_code < 400:
            print(f'URL {url} is {states["STABLE"]}.')
        else:
            message = f'URL {url} is {states["DOWN"]}. Status code: {response.status_code}'
            send_discord_webhook_message(message)
    except requests.exceptions.RequestException as e:
        message = f'Error accessing URL {url}: {str(e)}'
        send_discord_webhook_message(message)

# Function to fetch URLs from Firestore
def fetch_urls_from_firestore():
    urls = []
    # Assuming you have a collection named 'endpointuri' with documents containing 'url' field
    endpointuri_ref = db.collection('endpointuri')
    docs = endpointuri_ref.stream()
    for doc in docs:
        urls.append(doc.to_dict()['url'])
    return urls

# Monitoring loop
while True:
    try:
        urls = fetch_urls_from_firestore()
        for url in urls:
            monitor_url(url)
        time.sleep(10)  # Wait for 10 seconds before checking again
    except KeyboardInterrupt:
        print('Monitoring stopped by user.')
        break
