from sqlalchemy.orm import Session
from app import models, schemas

def creer_utilisateur(db: Session, utilisateur: schemas.UtilisateurCreate):
    nouveau = models.Utilisateur(nom=utilisateur.nom, email=utilisateur.email)
    db.add(nouveau)
    db.commit()
    db.refresh(nouveau)
    return nouveau

def lire_utilisateur(db: Session, user_id: int):
    return db.query(models.Utilisateur).filter(models.Utilisateur.id == user_id).first()

def supprimer_utilisateur(db: Session, user_id: int):
    utilisateur = db.query(models.Utilisateur).filter(models.Utilisateur.id == user_id).first()
    if utilisateur:
        db.delete(utilisateur)
        db.commit()
    return utilisateur
