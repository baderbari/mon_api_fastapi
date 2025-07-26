import uuid
from tests.conftest import client

def test_creer_utilisateur(client):
    nom = "Alice"
    email = f"alice+{uuid.uuid4().hex[:6]}@example.com"
    response = client.post("/utilisateurs/", json={"nom": nom, "email": email})
    assert response.status_code == 200
    data = response.json()
    assert data["nom"] == nom
    assert data["email"] == email
