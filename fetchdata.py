import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from get_doc_id import get_doc_id

symptoms = list()

# Initialize the Firebase Admin SDK

# Get a Firestore client
doc_id = list()
def fetch_data(db):
    doc_id = get_doc_id(db)
# Specify the document path
    doc_ref = db.collection('patient_symptoms').document(doc_id)

    # Fetch the document
    doc = doc_ref.get()


        
    if doc.exists:
        # Access the data within the document
        data = doc.to_dict()
        symp = data['symptoms']
        #print(symp)
        symptoms = symp.split(' ')
    else:
        print('Document does not exist')
    return symptoms