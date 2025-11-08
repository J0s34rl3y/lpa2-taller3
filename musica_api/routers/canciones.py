from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session

from musica_api import crud
from musica_api.database import get_session
from musica_api.models import Cancion
from musica_api.schemas.cancion_schema import CancionCreate, CancionRead

router = APIRouter()


@router.get("/", response_model=List[CancionRead])
def listar_canciones(db: Session = Depends(get_session)):
    return crud.list_canciones(db)


@router.post("/", response_model=CancionRead)
def crear_cancion(payload: CancionCreate, db: Session = Depends(get_session)):
    cancion = Cancion(**payload.model_dump())
    return crud.create_cancion(db, cancion)


@router.get("/buscar", response_model=List[CancionRead])
def buscar(q: Optional[str] = Query(None, min_length=1), db: Session = Depends(get_session)):
    if not q:
        return []
    return crud.buscar_canciones(db, q)


@router.get("/{cancion_id}", response_model=CancionRead)
def obtener_cancion(cancion_id: int, db: Session = Depends(get_session)):
    c = crud.get_cancion(db, cancion_id)
    if not c:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return c


@router.put("/{cancion_id}", response_model=CancionRead)
def actualizar_cancion(cancion_id: int, payload: CancionCreate, db: Session = Depends(get_session)):
    updated = crud.update_cancion(db, cancion_id, payload.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return updated


@router.delete("/{cancion_id}")
def eliminar_cancion(cancion_id: int, db: Session = Depends(get_session)):
    ok = crud.delete_cancion(db, cancion_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return {"ok": True}
