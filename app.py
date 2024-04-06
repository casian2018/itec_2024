import firebase_admin
from firebase_admin import credentials, firestore
import requests
import time

# Inițializează aplicația Firebase
cred = credentials.Certificate("C:\\Users\\Oprea\\Downloads\\itec2024-firebase-adminsdk-yjefv-9c193ac533.json")
firebase_admin.initialize_app(cred)

# Funcție pentru a obține starea unui endpoint
def get_endpoint_status(endpoint_url):
    try:
        response = requests.get(endpoint_url)
        if response.status_code == 200 or response.status_code == 302:
            return "Stable"
        else:
            return "Unstable"
    except:
        return "Down"

# Funcție pentru a actualiza starea unui endpoint în Firestore
def update_endpoint_status(endpoint_doc_ref, new_status):
    endpoint_doc_ref.update({"stare": new_status})

# Obține o referință către colecția "endpointuri" din Firestore
db = firestore.client()
endpoints_collection = db.collection("endpointuri")

# Buclă infinită pentru a actualiza starea endpoint-urilor la fiecare 30 de secunde
while True:
    # Iterează prin toate documentele din colecția "endpointuri"
    for doc in endpoints_collection.stream():
        # Obține URL-ul endpointului din document
        endpoint_url = doc.to_dict().get("url")
        if endpoint_url:
            # Obține starea actuală a endpointului
            status = get_endpoint_status(endpoint_url)
            
            # Obține referința către documentul endpointului
            endpoint_doc_ref = endpoints_collection.document(doc.id)
            
            # Actualizează starea endpointului în Firestore
            update_endpoint_status(endpoint_doc_ref, status)
    
    # Așteaptă 30 de secunde înainte de a începe următoarea iterație
    time.sleep(1)
