import uuid
from tests.conftest import client

def test_suppression_utilisateur(client):
    email = f"eve+{uuid.uuid4().hex[:6]}@example.com"
    creation = client.post("/utilisateurs/", json={"nom": "Eve", "email": email})
    utilisateur_id = creation.json()["id"]

    suppression = client.delete(f"/utilisateurs/{utilisateur_id}")
    assert suppression.status_code == 200

    lecture = client.get(f"/utilisateurs/{utilisateur_id}")
    assert lecture.status_code == 404
