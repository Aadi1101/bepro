from flask import Flask, jsonify, request
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from transform_data import transform_data
from fetch_all_data import fetch_all_data
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('./firestore-cred.json')
firebase_admin.initialize_app(cred)
app = Flask(__name__)
CORS(app)
# Load the TensorFlow model
model = tf.keras.models.load_model('./disease_model_1.h5')

# Define the route for model prediction
@app.route('/predict', methods=['GET','POST'])
def predict():
    # Get the input data from the request
    # Convert the input data to a numpy array
    db = None
    if not db:
        db = firestore.client()
    input_array = transform_data(db)
    print("input_array: ",input_array)
    

    # Make predictions using the loaded model
    y_pred = model.predict([np.expand_dims(input_array, axis=0)])
    ans = [int(np.argmax(i)) for i in y_pred]
    # Convert the predictions to a list
    #predicted_classes = [int(prediction) for prediction in predictions]

    # Prepare the response as JSON
    for i in range(len(ans)):
        dictionary = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}
        disease = dictionary[ans[i]]
    response = {
        'Condition': disease
    }
    print(response)
    data = fetch_all_data(db,'patient_data')
    data['Predicted'] = disease
    #print(data)
    x = ''
    query = db.collection('patient_login').where('email', '==', 'nitinbhoi@gmail.com')
    document_ids = [doc.id for doc in query.stream()]
    print(document_ids)
    for document_id in document_ids:
        x = x + document_id
    print('doc id: ',x)
    db.collection('patient_data').document(x).update(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
