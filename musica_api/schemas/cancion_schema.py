from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CancionCreate(BaseModel):
    titulo: str
    artista: str
    album: str
    duracion: int
    año: int
    genero: str


class CancionRead(CancionCreate):
    id: int
    fecha_creacion: datetime

    model_config = ConfigDict(from_attributes=True)
