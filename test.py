import firebase_admin
from firebase_admin import credentials, firestore

# Încarcă cheia de acces la Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\Oprea\\Downloads\\itec2024-firebase-adminsdk-yjefv-9c193ac533.json")
firebase_admin.initialize_app(cred)

# Obține o referință la baza de date Firestore
db = firestore.client()

# Definește datele pentru un nou document
new_bug_data = {
    "title": "Bug 1",
    "description": "Descrierea bug-ului 1"
}

try:
    # Interoghează colecția "/endpointuri" pentru a obține primul document
    endpoint_query = db.collection("endpointuri").limit(1)
    endpoint_docs = endpoint_query.stream()

    # Verifică dacă există vreun document în colecție
    for endpoint_doc in endpoint_docs:
        # Obține URL-ul din documentul endpoint
        endpoint_url = endpoint_doc.to_dict()["url"]
        # Adaugă URL-ul în datele pentru noul bug
        new_bug_data["project"] = endpoint_url
        # Adaugă un nou document în colecția "bugs" cu datele actualizate
        new_bug_ref = db.collection("bugs").add(new_bug_data)
        print("Document created with ID:", new_bug_ref[1])
        break  # Ieșiți din bucla for după ce ați găsit primul document
    else:
        print("Nu s-au găsit documente în colecția '/endpointuri'")
except Exception as e:
    print("Error creating document:", e)
