from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from musica_api.database import create_db_and_tables
from musica_api.routers.canciones import router as canciones_router
from musica_api.routers.favoritos import router as favoritos_router
from musica_api.routers.usuarios import router as usuarios_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Inicializa recursos al arrancar la aplicación (crear tablas si falta).
    """
    create_db_and_tables()
    yield


app = FastAPI(
    title="API de Música",
    description="API RESTful para gestionar usuarios, canciones y favoritos",
    version="1.0.0",
    lifespan=lifespan,
)


# CORS - permitir todo en desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluir routers
app.include_router(usuarios_router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(canciones_router, prefix="/api/canciones", tags=["Canciones"])
app.include_router(favoritos_router, prefix="/api/favoritos", tags=["Favoritos"])


@app.get("/", tags=["Root"])
def root():
    return {
        "nombre": "API de Música",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
