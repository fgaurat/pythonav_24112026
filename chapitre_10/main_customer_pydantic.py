from pprint import pprint
from pydantic import BaseModel,field_validator

class Customer(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    gender:str
    ip_address:str
    
    @field_validator('email')
    def validate_email(cls,v):
        if '@' not in v:
            raise ValueError('Email error')
        return v
        

def main():
    gender:str
    c = Customer(
        id="1",
        first_name="Jean",
        last_name="Martin",
        email="jm.truc.com",
        gender="Male",
        ip_address="127.0.0.1")
    print(c)

if __name__=='__main__':
    main()
