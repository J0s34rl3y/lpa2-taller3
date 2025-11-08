from typing import List, Optional

from sqlmodel import Session, select

from .models import Cancion, Favorito, Usuario


# ------------------ Usuarios ------------------
def create_usuario(db: Session, usuario: Usuario) -> Usuario:
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def get_usuario(db: Session, usuario_id: int) -> Optional[Usuario]:
    return db.get(Usuario, usuario_id)


def list_usuarios(db: Session) -> List[Usuario]:
    return db.exec(select(Usuario)).all()


def update_usuario(db: Session, usuario_id: int, cambios: dict) -> Optional[Usuario]:
    usuario = get_usuario(db, usuario_id)
    if not usuario:
        return None
    for k, v in cambios.items():
        setattr(usuario, k, v)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def delete_usuario(db: Session, usuario_id: int) -> bool:
    usuario = get_usuario(db, usuario_id)
    if not usuario:
        return False
    db.delete(usuario)
    db.commit()
    return True


# ------------------ Canciones ------------------
def create_cancion(db: Session, cancion: Cancion) -> Cancion:
    db.add(cancion)
    db.commit()
    db.refresh(cancion)
    return cancion


def get_cancion(db: Session, cancion_id: int) -> Optional[Cancion]:
    return db.get(Cancion, cancion_id)


def list_canciones(db: Session) -> List[Cancion]:
    return db.exec(select(Cancion)).all()


def update_cancion(db: Session, cancion_id: int, cambios: dict) -> Optional[Cancion]:
    cancion = get_cancion(db, cancion_id)
    if not cancion:
        return None
    for k, v in cambios.items():
        setattr(cancion, k, v)
    db.add(cancion)
    db.commit()
    db.refresh(cancion)
    return cancion


def delete_cancion(db: Session, cancion_id: int) -> bool:
    cancion = get_cancion(db, cancion_id)
    if not cancion:
        return False
    db.delete(cancion)
    db.commit()
    return True


def buscar_canciones(db: Session, q: str) -> List[Cancion]:
    q_like = f"%{q}%"
    stmt = select(Cancion).where(
        (Cancion.titulo.ilike(q_like)) | (Cancion.artista.ilike(q_like)) | (Cancion.genero.ilike(q_like))
    )
    return db.exec(stmt).all()


# ------------------ Favoritos ------------------
def create_favorito(db: Session, favorito: Favorito) -> Favorito:
    # evitar duplicados simples
    existing = db.exec(
        select(Favorito).where(
            (Favorito.id_usuario == favorito.id_usuario) & (Favorito.id_cancion == favorito.id_cancion)
        )
    ).first()
    if existing:
        return existing
    db.add(favorito)
    db.commit()
    db.refresh(favorito)
    return favorito


def get_favorito(db: Session, favorito_id: int) -> Optional[Favorito]:
    return db.get(Favorito, favorito_id)


def list_favoritos(db: Session) -> List[Favorito]:
    return db.exec(select(Favorito)).all()


def delete_favorito(db: Session, favorito_id: int) -> bool:
    f = get_favorito(db, favorito_id)
    if not f:
        return False
    db.delete(f)
    db.commit()
    return True


def listar_favoritos_usuario(db: Session, usuario_id: int) -> List[Favorito]:
    stmt = select(Favorito).where(Favorito.id_usuario == usuario_id)
    return db.exec(stmt).all()
