from fastapi import FastAPI
from app.routers import utilisateurs
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(utilisateurs.router, prefix="/utilisateurs", tags=["Utilisateurs"])
