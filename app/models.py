from datetime import datetime

from pydantic import BaseModel


class FileBaseModel(BaseModel):
    full_name: str

    class Config:
        schema_extra = {
            "example": {
                "full_name": "cartoon.jpeg",
            }
        }


class FileFullModel(FileBaseModel):
    name: str
    expansion: str
    size: float
    date_change: datetime
    detail: str = "Succes"

    class Config:
        schema_extra = {
            "example": {
                "full_name": "cartoon.jpeg",
                "name": "cartoon",
                "expansion": "jpeg",
                "size": "233",
                "date_change": datetime.now(),
                "detail": "succes",
            }
        }