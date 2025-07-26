from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.UtilisateurOut)
def creer(utilisateur: schemas.UtilisateurCreate, db: Session = Depends(get_db)):
    return crud.creer_utilisateur(db, utilisateur)

@router.get("/{user_id}", response_model=schemas.UtilisateurOut)
def lire(user_id: int, db: Session = Depends(get_db)):
    utilisateur = crud.lire_utilisateur(db, user_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur

@router.delete("/{user_id}", response_model=schemas.UtilisateurOut)
def supprimer(user_id: int, db: Session = Depends(get_db)):
    utilisateur = crud.supprimer_utilisateur(db, user_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur
