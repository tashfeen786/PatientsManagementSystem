from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get('/sort')
def sort_patients(sort_by: str= Query(..., description= 'sort on the basis of height, weight, bmi') order: str= Query('asc', description= 'sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code= 400, detail= f'Invalid fields select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code= 400, detail= 'Invalid order between asc and desc')


    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by, 0), reverse= sort_order)
    
    return sorted_data
