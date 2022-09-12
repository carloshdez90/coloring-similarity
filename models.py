from pydantic import BaseModel
import uuid


class Item(BaseModel):
    expected_image: str
    student_response: str
    quark_id: uuid.UUID
