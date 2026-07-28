from pydantic import BaseModel

class Movie(BaseModel):
    name: str
    rating: float


schema = Movie.model_json_schema()

print(schema)