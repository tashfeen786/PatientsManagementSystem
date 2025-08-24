from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import  Annotated
import json


app = FastAPI()

class patient(BaseModel):
    id: Annotated[str, Field(description= 'ID of the Patient', example= 'P001')]
    name: Annotated[str, Field(description= 'Name of the Patient', example= 'John Doe')]
    age: Annotated[int, Field(description= 'Age of the Patient', example= 30)]
    height: Annotated[float, Field(description= 'Height of the Patient in cm', example= 175.5)]
    weight: Annotated[float, Field(description= 'Weight of the Patient in kg', example= 70.0)]
    
    @computed_field
    def bmi(self) -> float:
        return round(self.weight / ((self.height / 100) ** 2), 2)
    

    @computed_field
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= self.bmi < 24.9:
            return 'Normal weight'
        elif 25 <= self.bmi < 29.9:
            return 'Overweight'
        else:
            return 'Obesity'

def load_data():
    with open('patiants.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patiants.json', 'w') as f:
        json.dump(data, f)




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
def sort_patients(sort_by: str= Query(..., description= 'sort on the basis of height, weight, bmi'), order: str= Query('asc', description= 'sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code= 400, detail= f'Invalid fields select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code= 400, detail= 'Invalid order between asc and desc')


    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by, 0), reverse= sort_order)
    
    return sorted_data



@app.post('/Create')
def create_patient(patient: patient):

    # Load existing data
    data = load_data()

    # Check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code= 400, detail= 'Patient with this ID already exists')
    
    # Add new patient data

    data[patient.id] = patient.model_dump(exclude = ['id'])

    # Save updated data
    save_data(data)

    return JSONResponse(status_code= 201, content= {'message': 'Patient created successfully', 'patient_id': patient.id})



@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]
