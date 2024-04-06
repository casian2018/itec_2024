import firebase_admin
from firebase_admin import credentials, firestore

# Încarcă cheia de acces la Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\Oprea\\Downloads\\itec2024-firebase-adminsdk-yjefv-9c193ac533.json")
firebase_admin.initialize_app(cred)

# Obține o referință la baza de date Firestore
db = firestore.client()

# Definește datele pentru noul document
new_endpoint_data = {
    "url": "https://itec.ro",
    "status": "Stable",
    "bugs": [
        {
            "title": "Bug 1",
            "description": "Descrierea bug-ului 1"
        },
        {
            "title": "Bug 2",
            "description": "Descrierea bug-ului 2"
        }
        # Adaugă mai multe bug-uri după nevoie
    ]
}

try:
    # Adaugă un nou document în colecția /endpointuri
    new_endpoint_ref = db.collection("endpointuri").add(new_endpoint_data)
    # Obține id-ul documentului din tuplul returnat
    document_id = new_endpoint_ref[1].id
    print("Document created with ID:", document_id)
except firestore.FirestoreError as e:
    print("Error creating document:", e)
