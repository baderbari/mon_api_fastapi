from pydantic import BaseModel, ConfigDict, EmailStr


class UtilisateurCreate(BaseModel):
    email: EmailStr
    nom: str

    model_config = ConfigDict(from_attributes=True)


class UtilisateurOut(BaseModel):
    id: int
    nom: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
