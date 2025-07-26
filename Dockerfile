# Utilise une image légère avec Python
FROM python:3.11-slim

# Crée un dossier pour ton code
WORKDIR /app

# Copie les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le reste du code dans le conteneur
COPY . .

# Démarre l’application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

