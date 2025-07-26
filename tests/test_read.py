import uuid
from tests.conftest import client

def test_lecture_utilisateur(client):
    email = f"bob+{uuid.uuid4().hex[:6]}@example.com"
    creation = client.post("/utilisateurs/", json={"nom": "Bob", "email": email})
    assert creation.status_code == 200
    utilisateur_id = creation.json()["id"]

    lecture = client.get(f"/utilisateurs/{utilisateur_id}")
    assert lecture.status_code == 200
    assert lecture.json()["email"] == email
