# API de Música

Una [API RESTful](https://aws.amazon.com/es/what-is/restful-api/) para gestionar usuarios, canciones y favoritos. Desarrollada con [FastAPI](https://fastapi.tiangolo.com/), [SQLModel](https://sqlmodel.tiangolo.com/) y [Pydantic](https://docs.pydantic.dev/).

## Autor

**Jose Arley Ramirez**  
GitHub: [@J0s34rl3y]

## Descripción

Esta API permite administrar:
- **Usuarios**: crear y gestionar perfiles de usuarios.
- **Canciones**: agregar, actualizar y eliminar canciones con sus metadatos.
- **Favoritos**: gestionar las canciones favoritas de cada usuario.

El proyecto incluye una interfaz de documentación interactiva generada automáticamente con [Swagger](https://swagger.io/) disponible en el *endpoint* `/docs`.

## Estructura del Proyecto

```
lpa2-taller3
├──  README.md            # Este archivo, documentación completa del proyecto
├──  .gitignore           # Archivos y directorios a ignorar por Git
├──  .pre-commit-config.yaml  # Configuración de hooks pre-commit
├──  pyproject.toml       # Configuración de herramientas (ruff, black)
├──  pytest.ini           # Configuración de pytest
├──  main.py              # Script principal para ejecutar la aplicación
├──  musica.db            # Base de Datos SQLite
├──  requirements.txt     # Dependencias del proyecto
├──  utils.py             # Funciones de utilidad
├──  musica_api/          # Módulo principal del API
│   ├──  __init__.py      # Inicialización del módulo
│   ├──  config.py        # Configuración de la aplicación
│   ├──  database.py      # Configuración de base de datos
│   ├──  crud.py          # Operaciones CRUD
│   ├──  models/          # Modelos SQLModel
│   │   ├──  usuario.py
│   │   ├──  cancion.py
│   │   └──  favorito.py
│   ├──  schemas/         # Schemas Pydantic
│   │   ├──  usuario_schema.py
│   │   ├──  cancion_schema.py
│   │   └──  favorito_schema.py
│   └──  routers/         # Routers FastAPI
│       ├──  usuarios.py
│       ├──  canciones.py
│       └──  favoritos.py
├──  frontend/            # Interfaz web Flask
│   ├──  app.py           # Aplicación Flask
│   └──  templates/       # Templates HTML
│       ├──  base.html
│       ├──  index.html
│       ├──  usuarios.html
│       ├──  canciones.html
│       └──  favoritos.html
└──  tests/               # Pruebas automatizadas
    ├──  conftest.py      # Fixtures de pytest
    └──  test_api.py      # Pruebas unitarias

```
## Modelo de Datos

1. **Usuario**:
   - id: Identificador único
   - nombre: Nombre del usuario
   - correo: Correo electrónico (único)
   - fecha_registro: Fecha de registro

2. **Canción**:
   - id: Identificador único
   - titulo: Título de la canción
   - artista: Artista o intérprete
   - album: Álbum al que pertenece
   - duracion: Duración en segundos
   - año: Año de lanzamiento
   - genero: Género musical
   - fecha_creacion: Fecha de creación del registro

3. **Favorito**:
   - id: Identificador único
   - id_usuario: ID del usuario (clave foránea)
   - id_cancion: ID de la canción (clave foránea)
   - fecha_marcado: Fecha en que se marcó como favorito

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/J0s34rl3y/lpa2-taller3.git
   cd lpa2-taller3
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Linux/Mac
   # o
   .venv\Scripts\activate  # En Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Instala los hooks de pre-commit:

   ```bash
   pre-commit install
   ```

## Ejecución

### Backend (API)

1. Ejecuta el servidor FastAPI:

   ```bash
   uvicorn main:app --reload --port 8002
   ```

2. Accede a la API:
   - API: [http://127.0.0.1:8002/](http://127.0.0.1:8002/)
   - Documentación *Swagger UI*: [http://127.0.0.1:8002/docs](http://127.0.0.1:8002/docs)
   - Documentación *ReDoc*: [http://127.0.0.1:8002/redoc](http://127.0.0.1:8002/redoc)

### Frontend (Interfaz Web)

1. En otra terminal, ejecuta el frontend Flask:

   ```bash
   cd frontend
   python app.py
   ```

2. Accede a la interfaz web:
   - Frontend: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Pruebas

Ejecuta las pruebas automáticas con pytest:

```bash
pytest tests/ -v --cov
```

## Uso de la API

### Usuarios

- **Listar usuarios**: `GET /api/usuarios`
- **Crear usuario**: `POST /api/usuarios`
- **Obtener usuario**: `GET /api/usuarios/{id}`
- **Actualizar usuario**: `PUT /api/usuarios/{id}`
- **Eliminar usuario**: `DELETE /api/usuarios/{id}`

### Canciones

- **Listar canciones**: `GET /api/canciones`
- **Crear canción**: `POST /api/canciones`
- **Obtener canción**: `GET /api/canciones/{id}`
- **Actualizar canción**: `PUT /api/canciones/{id}`
- **Eliminar canción**: `DELETE /api/canciones/{id}`
- **Buscar canciones**: `GET /api/canciones/buscar?titulo=value&artista=value&genero=value`

### Favoritos

- **Listar favoritos**: `GET /api/favoritos`
- **Marcar favorito**: `POST /api/favoritos`
- **Obtener favorito**: `GET /api/favoritos/{id}`
- **Eliminar favorito**: `DELETE /api/favoritos/{id}`
- **Listar favoritos de usuario**: `GET /api/usuarios/{id}/favoritos`
- **Marcar favorito específico**: `POST /api/usuarios/{id_usuario}/favoritos/{id_cancion}`
- **Eliminar favorito específico**: `DELETE /api/usuarios/{id_usuario}/favoritos/{id_cancion}`

## Desarrollo del Taller

### Características Implementadas

✅ **API RESTful completa** con FastAPI y SQLModel
✅ **Frontend web** con Flask y Bootstrap 5
✅ **Pruebas automatizadas** con pytest (66% cobertura)
✅ **Pre-commit hooks** con ruff, black y pytest
✅ **Calidad de código** configurada con ruff y black
✅ **Documentación automática** con Swagger UI y ReDoc
✅ **Validación de datos** con Pydantic v2
✅ **Manejo de errores** HTTP apropiados

### Estado de TODOs

Todos los `# TODO` del código original han sido implementados:
- ✅ Modelos SQLModel completados (Usuario, Cancion, Favorito)
- ✅ Schemas Pydantic con validaciones
- ✅ Operaciones CRUD completas
- ✅ Routers con todos los endpoints
- ✅ Tests automatizados funcionando
- ✅ Validaciones de email, año, etc.

### Tecnologías Utilizadas

- **Backend**: FastAPI 0.115+, SQLModel, Pydantic v2
- **Frontend**: Flask, Bootstrap 5, Jinja2
- **Base de datos**: SQLite (desarrollo)
- **Testing**: pytest, pytest-cov, pytest-asyncio
- **Calidad**: ruff, black, pre-commit
- **Documentación**: Swagger UI, ReDoc

## Sugerencias de Mejora

1. **Autenticación y autorización**: Implementar JWT o OAuth2 para proteger los endpoints y asociar los usuarios automáticamente con sus favoritos.

2. **Paginación**: Añadir soporte para paginación en las listas de canciones, usuarios y favoritos para mejorar el rendimiento con grandes volúmenes de datos.

3. **Base de datos en producción**: Migrar a una base de datos más robusta como PostgreSQL o MySQL para entornos de producción.

4. **Docker**: Contenerizar la aplicación para facilitar su despliegue en diferentes entornos.

5. **Registro (logging)**: Implementar un sistema de registro más completo para monitorear errores y uso de la API.

6. **Caché**: Añadir caché para mejorar la velocidad de respuesta en consultas frecuentes.

7. **Estadísticas de uso**: Implementar un sistema de seguimiento para analizar qué canciones son más populares y sugerir recomendaciones basadas en preferencias similares.

8. **Subida de archivos**: Permitir la subida de archivos de audio y gestionar su almacenamiento en un servicio como S3 o similar.

