from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 characters', examples=['Nitish', 'Amit'])]
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Patients marital status')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]
    email: EmailStr
    linkedin_url: AnyUrl

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

# patient_info = {'name':'nitish', 
#                 'age': '30',
#                 'weight': 75.2,
#                 'married':True,
#                 'allergies': ['dust', 'pollen'],
#                 'contact_details': {'email': 'abc@gmail.com', 'phone': '123456'}}


# patient_info = {'name':'nitish', 
#                 'age': '30',
#                 'weight': 75.2,
#                 'married':True,
#                 'contact_details': {'email': 'abc@gmail.com', 'phone': '123456'}}


# patient_info = {'name':'nitish', 
#                 'age': '30',
#                 'weight': 75.2,
#                 'married':True,
#                 'contact_details': {'phone': '123456'},
#                 'email': 'a@g.c',
#                 'linkedin_url': 'https://linkedin.com1322'
# }

# patient_info = {'name':'nitish', 
#                 'age': '30',
#                 'weight': -75.2,
#                 'married':True,
#                 'contact_details': {'phone': '123456'},
#                 'email': 'a@g.c',
#                 'linkedin_url': 'https://linkedin.com1322'
# }

patient_info = {'name':'nitish', 
                'age': '30',
                'weight': 75.2,
                'married':True,
                'contact_details': {'phone': '123456'},
                'email': 'a@g.c',
                'linkedin_url': 'https://linkedin.com1322'
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
