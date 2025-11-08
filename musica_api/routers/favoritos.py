from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from musica_api import crud
from musica_api.database import get_session
from musica_api.models import Favorito
from musica_api.schemas.favorito_schema import FavoritoCreate, FavoritoRead

router = APIRouter()


@router.get("/", response_model=List[FavoritoRead])
def listar_favoritos(db: Session = Depends(get_session)):
    return crud.list_favoritos(db)


@router.post("/", response_model=FavoritoRead)
def crear_favorito(payload: FavoritoCreate, db: Session = Depends(get_session)):
    f = Favorito(id_usuario=payload.id_usuario, id_cancion=payload.id_cancion)
    creado = crud.create_favorito(db, f)
    return creado


@router.get("/{favorito_id}", response_model=FavoritoRead)
def obtener_favorito(favorito_id: int, db: Session = Depends(get_session)):
    f = crud.get_favorito(db, favorito_id)
    if not f:
        raise HTTPException(status_code=404, detail="Favorito no encontrado")
    return f


@router.delete("/{favorito_id}")
def eliminar_favorito(favorito_id: int, db: Session = Depends(get_session)):
    ok = crud.delete_favorito(db, favorito_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Favorito no encontrado")
    return {"ok": True}


@router.get("/usuario/{usuario_id}", response_model=List[FavoritoRead])
def favoritos_de_usuario(usuario_id: int, db: Session = Depends(get_session)):
    return crud.listar_favoritos_usuario(db, usuario_id)
