from pydantic import BaseModel
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name':'nitish', 'age': '30'}
# patient_info = {'name':'nitish', 'age': 'thirty'}

patient1 = Patient(**patient_info)

update_patient_data(patient1)