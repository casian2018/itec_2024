import firebase_admin
from firebase_admin import credentials, firestore
import requests
import time

cred = credentials.Certificate("C:\\Users\\Oprea\\Downloads\\itec2024-firebase-adminsdk-yjefv-9c193ac533.json")
firebase_admin.initialize_app(cred)

def get_endpoint_status(endpoint_url):
    try:
        response = requests.get(endpoint_url, verify=False)
        if response.status_code == 200 or response.status_code == 302:
            return "Stable"
        else:
            return "Unstable"
    except:
        return "Down"

def update_endpoint_status(endpoint_doc_ref, new_status):
    endpoint_doc_ref.update({"status": new_status})

def monitor_endpoints():
    db = firestore.client()
    endpoints_collection = db.collection("endpointuri")

    while True:
        for doc in endpoints_collection.stream():
            endpoint_url = doc.to_dict().get("url")
            if endpoint_url:
                # Check if there are any bugs submitted for this endpoint
                bugs_collection = db.collection("bugs").where("project", "==", endpoint_url).limit(1).get()
                if bugs_collection:
                    status = "Unstable"
                else:
                    status = get_endpoint_status(endpoint_url)

                endpoint_doc_ref = endpoints_collection.document(doc.id)
                update_endpoint_status(endpoint_doc_ref, status)
        
        time.sleep(10)  # Sleep for 10 seconds

if __name__ == "__main__":
    monitor_endpoints()
