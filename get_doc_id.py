import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def get_doc_id(db):
    collection_ref = db.collection('patient_login')
    query = collection_ref.where('email', '==', 'nitinbhoi@gmail.com')
    document_ids = [doc.id for doc in query.stream()]
    for document_id in document_ids:
        return document_id
'''
document_ids = [doc.id for doc in collection_ref.list_documents()]
for document_id in document_ids:
    doc_id.append(document_id)
print(doc_id)
'''