import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

# Añadir el directorio raíz al PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import app


@pytest.fixture(scope="session")
def engine():
    # motor en memoria para tests
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture()
def session(engine):
    # Limpiar todas las tablas antes de cada test
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as s:
        yield s


@pytest.fixture()
def client(session):
    # override la dependencia get_session para usar la sesión en memoria
    from musica_api.database import get_session

    def get_session_override():
        yield session

    app.dependency_overrides[get_session] = get_session_override

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()


@pytest.fixture()
def usuario_test(session):
    """Fixture que crea un usuario de prueba en la base de datos"""
    from musica_api.models.usuario import Usuario

    usuario = Usuario(nombre="Test User", correo="test@example.com")
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


@pytest.fixture()
def cancion_test(session):
    """Fixture que crea una canción de prueba en la base de datos"""
    from musica_api.models.cancion import Cancion

    cancion = Cancion(
        titulo="Test Song",
        artista="Test Artist",
        album="Test Album",
        duracion=180,
        año=2024,
        genero="Rock",
    )
    session.add(cancion)
    session.commit()
    session.refresh(cancion)
    return cancion
