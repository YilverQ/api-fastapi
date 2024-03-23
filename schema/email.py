from pydantic import BaseModel

#Model
class Email(BaseModel):
    to   	: str
    subject : str
    body 	: str