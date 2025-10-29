from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True) # Object creation k time pe jo fields nhi diye unhe exclude kr dega like in our case gender.
# temp = patient1.model_dump(exclude=['name','gender'])
# temp = patient1.model_dump(exclude={'address': {'state'}})
# temp = patient1.model_dump(exclude={'address': ['state']})
# temp = patient1.model_dump_json()  # if you to dump as json string.

print(temp)
print(type(temp))