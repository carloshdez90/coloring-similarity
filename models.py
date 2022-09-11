from pydantic import BaseModel


class Item(BaseModel):
    expected_image: str
    student_response: str
