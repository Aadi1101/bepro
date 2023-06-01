from fetchdata import fetch_data 
def transform_data(db):

    zeros_list = [0] * 132
    symptoms_char = fetch_data(db)
    #print(symptoms_char)

    with open('./symptoms.txt','r') as f:
        symptom = f.read()
        symptoms = symptom.split('\n')
    #print(len(symptoms))

    for i in range(len(symptoms_char)):
        for j in range(len(symptoms)):
            if symptoms_char[i] == symptoms[j]:
                zeros_list[j] = 1
            else:
                continue
    return zeros_list