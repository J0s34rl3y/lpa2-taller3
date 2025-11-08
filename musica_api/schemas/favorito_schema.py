from datetime import datetime

from pydantic import BaseModel, ConfigDict


class FavoritoCreate(BaseModel):
    id_usuario: int
    id_cancion: int


class FavoritoRead(FavoritoCreate):
    id: int
    fecha_marcado: datetime

    model_config = ConfigDict(from_attributes=True)
