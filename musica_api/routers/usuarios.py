from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from musica_api import crud
from musica_api.database import get_session
from musica_api.models import Usuario
from musica_api.schemas.usuario_schema import UsuarioCreate, UsuarioRead

router = APIRouter()


@router.get("/", response_model=List[UsuarioRead])
def listar_usuarios(db: Session = Depends(get_session)):
    return crud.list_usuarios(db)


@router.post("/", response_model=UsuarioRead)
def crear_usuario(payload: UsuarioCreate, db: Session = Depends(get_session)):
    # validar correo único
    from sqlmodel import select

    existing = db.exec(select(Usuario).where(Usuario.correo == payload.correo)).first()
    if existing:
        raise HTTPException(status_code=422, detail="Correo ya registrado")
    usuario = Usuario(nombre=payload.nombre, correo=payload.correo)
    return crud.create_usuario(db, usuario)


@router.get("/{usuario_id}", response_model=UsuarioRead)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_session)):
    u = crud.get_usuario(db, usuario_id)
    if not u:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return u


@router.put("/{usuario_id}", response_model=UsuarioRead)
def actualizar_usuario(usuario_id: int, payload: UsuarioCreate, db: Session = Depends(get_session)):
    updated = crud.update_usuario(db, usuario_id, payload.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated


@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_session)):
    ok = crud.delete_usuario(db, usuario_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"ok": True}
