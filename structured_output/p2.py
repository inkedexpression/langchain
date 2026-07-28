from pydantic import BaseModel

class Price(BaseModel):

    name : str
    price : float

new_cx = {'name':'laptop','price':"50000"}
cx = Price(**new_cx)
print(cx)