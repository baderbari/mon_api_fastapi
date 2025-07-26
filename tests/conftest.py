import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import Utilisateur
import sys

print("🧭 PYTHONPATH =", sys.path)

# Fixture pour le client de test
@pytest.fixture
def client():
    return TestClient(app)

# Nettoyage automatique de la table utilisateurs après chaque test
@pytest.fixture(autouse=True)
def cleanup_utilisateurs():
    yield
    db = SessionLocal()
    try:
        db.query(Utilisateur).delete()
        db.commit()
    finally:
        db.close()
