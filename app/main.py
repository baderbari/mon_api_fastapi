from fastapi import FastAPI
import app.models
from app.database import Base, engine
from app.models import utilisateurs

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(utilisateurs.router, prefix="/utilisateurs", tags=["Utilisateurs"])
