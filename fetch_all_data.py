import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from get_doc_id import get_doc_id

symptoms = list()

# Initialize the Firebase Admin SDK

# Get a Firestore client
doc_id = list()
def fetch_all_data(db,collection_ref):
    doc_id = get_doc_id(db)
# Specify the document path
    doc_ref = db.collection(collection_ref).document(doc_id)

    # Fetch the document
    doc = doc_ref.get()


        
    if doc.exists:
        # Access the data within the document
        data = doc.to_dict()
    else:
        print('Document does not exist')
    return data
