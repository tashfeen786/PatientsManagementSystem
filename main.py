from fastapi import FastAPI, Path, HTTPException
import json


app = FastAPI()

def load_data():
    with open('patiants.json', 'r') as f:
        data = json.load(f)

    return data



@app.get("/")
def hello():
    return {'message': 'Patients Management System API'}

@app.get('/About')
def about():
    return {'message': 'A Fully funcational API to manage patients records'}


@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patiants/{patient_id}')
def view_patient(patient_id: str = Path(..., description= 'ID if the Patient in DB', example= 'P001')):
    # load all patiants data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code= 404, detail= 'Patient not found')