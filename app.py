import firebase_admin
from firebase_admin import credentials, firestore
import requests
import time
import matplotlib.pyplot as plt
import socketio

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

sio = socketio.Server()

@sio.on('connect')
def connect(sid, environ):
    print('Client connected')

@sio.on('disconnect')
def disconnect(sid):
    print('Client disconnected')

def monitor_endpoints():
    db = firestore.client()
    endpoints_collection = db.collection("endpointuri")

    while True:
        statuses = []
        for doc in endpoints_collection.stream():
            endpoint_url = doc.to_dict().get("url")
            if endpoint_url:
                status = get_endpoint_status(endpoint_url)
                statuses.append(status)
                
                endpoint_doc_ref = endpoints_collection.document(doc.id)
                update_endpoint_status(endpoint_doc_ref, status)
                
                
                # Send real-time update to client
                sio.emit('update', {'status': status})

                

        # Plot chart
        plt.figure(figsize=(8, 6))
        plt.hist(statuses, bins=['Stable', 'Unstable', 'Down'])
        plt.title('Endpoint Status Distribution')
        plt.xlabel('Status')
        plt.ylabel('Frequency')
        plt.savefig('endpoint_status_chart.png')
        plt.close()
        
        time.sleep(10)  # Sleep for 10 seconds

if __name__ == "__main__":
    app = socketio.WSGIApp(sio)
    monitor_endpoints()

    