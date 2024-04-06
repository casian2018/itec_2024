import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\Oprea\\Downloads\\itec2024-firebase-adminsdk-yjefv-9c193ac533.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Function to add a new endpoint with bugs
def add_endpoint_with_bugs(url, bugs):
    doc_ref = db.collection('endpointuri').document()
    doc_ref.set({
        'url': url,
        'bugs': bugs
    })

# Function to delete an endpoint by its document ID
def delete_endpoint(endpoint_id):
    db.collection('endpointuri').document(endpoint_id).delete()

# Function to mark a bug as resolved and delete it
def mark_bug_resolved(endpoint_id, bug_index):
    endpoint_ref = db.collection('endpointuri').document(endpoint_id)
    endpoint_data = endpoint_ref.get().to_dict()

    if endpoint_data is None:
        print(f"Error: Endpoint with ID '{endpoint_id}' does not exist.")
        return

    bugs = endpoint_data.get('bugs', [])

    if len(bugs) <= bug_index:
        print(f"Error: Bug index '{bug_index}' out of range for endpoint '{endpoint_id}'.")
        return

    # Mark the bug as resolved
    bugs[bug_index]['resolved'] = True

    # Update the endpoint document
    endpoint_ref.update({
        'bugs': bugs
    })

    # Delete the bug if resolved
    if bugs[bug_index]['resolved']:
        del bugs[bug_index]
        endpoint_ref.update({
            'bugs': bugs
        })

# Example usage
if __name__ == "__main__":
    # Add a new endpoint with bugs
    add_endpoint_with_bugs("https://example.com/api", [
        {"description": "Bug 1", "resolved": False},
        {"description": "Bug 2", "resolved": False}
    ])

    # Retrieve the document ID of the newly added endpoint
    endpoint_query = db.collection('endpointuri').where('url', '==', 'https://example.com/api').limit(1).get()
    endpoint_document_id = endpoint_query[0].id if endpoint_query else None

    if endpoint_document_id:
        # Mark a bug as resolved and delete it
        mark_bug_resolved(endpoint_document_id, 0)
    else:
        print("Error: Endpoint not found.")
