from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class CancionBase(SQLModel):
    titulo: str
    artista: str
    album: str
    duracion: int
    año: int
    genero: str


class Cancion(CancionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)
