from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Favorito(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_usuario: int = Field(foreign_key="usuario.id")
    id_cancion: int = Field(foreign_key="cancion.id")
    fecha_marcado: datetime = Field(default_factory=datetime.utcnow)
