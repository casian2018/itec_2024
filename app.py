import firebase_admin
from firebase_admin import credentials, firestore
import requests
import time
import urllib3
from grafanalib.core import *

# Disable TLS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Firebase initialization
cred = credentials.Certificate("itec2024-firebase-adminsdk-yjefv-9c193ac533.json")
firebase_admin.initialize_app(cred)

# Function to get endpoint status
def get_endpoint_status(endpoint_url):
    try:
        response = requests.get(endpoint_url, verify=False)
        if response.status_code == 200 or response.status_code == 302:
            return "Stable"
        else:
            return "Unstable"
    except:
        return "Down"

# Function to update endpoint status in Firestore
def update_endpoint_status(endpoint_doc_ref, new_status):
    endpoint_doc_ref.update({"status": new_status})

# Function to monitor endpoints
def monitor_endpoints():
    db = firestore.client()
    endpoints_collection = db.collection("endpointuri")

    try:
        while True:
            for doc in endpoints_collection.stream():
                endpoint_url = doc.to_dict().get("url")
                if endpoint_url:
                    # Check if there are any bugs submitted for this endpoint
                    bugs_collection = db.collection("bugs").where("project", "==", endpoint_url).limit(1).stream()
                    if bugs_collection:
                        status = "Unstable"
                    else:
                        status = get_endpoint_status(endpoint_url)

                    endpoint_doc_ref = endpoints_collection.document(doc.id)
                    update_endpoint_status(endpoint_doc_ref, status)

            time.sleep(10)  # Sleep for 10 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped.")

# Function to create Grafana dashboard
def create_dashboard():
    # Define dashboard properties
    dashboard = Dashboard(
        title="Endpoint Status Dashboard",
        rows=[
            Row(panels=[
                Graph(
                    title="Endpoint Status",
                    dataSource="Firebase",
                    targets=[
                        Target(
                            expr='firebase_endpoint_status{endpoint="YOUR_ENDPOINT"}',
                            legendFormat="{{endpoint}}"
                        )
                    ]
                )
            ])
        ]
    )
    
    # Save the dashboard to a JSON file
    with open("endpoint_status_dashboard.json", "w") as f:
        f.write(dashboard.to_json(indent=2))

if __name__ == "__main__":
    monitor_endpoints()
    create_dashboard()
