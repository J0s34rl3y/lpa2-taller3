from fastapi.testclient import TestClient


def test_root(client: TestClient):
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("nombre") == "API de Música"


def test_health(client: TestClient):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json().get("status") == "healthy"


def test_crud_usuario(client: TestClient):
    # crear
    payload = {"nombre": "Test User", "correo": "test@example.com"}
    r = client.post("/api/usuarios/", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["correo"] == payload["correo"]

    uid = data["id"]
    # obtener
    r2 = client.get(f"/api/usuarios/{uid}")
    assert r2.status_code == 200
    # listar
    r3 = client.get("/api/usuarios/")
    assert r3.status_code == 200


def test_crud_cancion_y_buscar(client: TestClient):
    payload = {
        "titulo": "Cancion Test",
        "artista": "Artista",
        "album": "Album",
        "duracion": 200,
        "año": 2020,
        "genero": "Pop",
    }
    r = client.post("/api/canciones/", json=payload)
    assert r.status_code == 200
    data = r.json()
    cid = data["id"]

    r2 = client.get(f"/api/canciones/{cid}")
    assert r2.status_code == 200

    # buscar
    r3 = client.get("/api/canciones/buscar", params={"q": "Cancion"})
    assert r3.status_code == 200


def test_favoritos_flow(client: TestClient):
    # crear usuario
    u = client.post("/api/usuarios/", json={"nombre": "Fav User", "correo": "fav@example.com"}).json()
    # crear cancion
    c = client.post(
        "/api/canciones/",
        json={
            "titulo": "Fav Song",
            "artista": "A",
            "album": "B",
            "duracion": 123,
            "año": 2021,
            "genero": "Rock",
        },
    ).json()

    f = client.post("/api/favoritos/", json={"id_usuario": u["id"], "id_cancion": c["id"]})
    assert f.status_code == 200

    # listar favoritos
    r = client.get("/api/favoritos/")
    assert r.status_code == 200
