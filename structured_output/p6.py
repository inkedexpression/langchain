from pydantic import BaseModel , field_validator

class Password(BaseModel):
    user : str
    password : str

    @field_validator("password")
    @classmethod
    def password_validate(cls ,value):
        if len(value) < 8:
            raise ValueError("the password has to be more or equal to 8")
        if '@' not in value:
            raise Exception("@ has to be used in the password")
        return value

cx = {'user':'dhauash','password':'dhanushn@ik'}
result = Password(**cx)
print(result)
