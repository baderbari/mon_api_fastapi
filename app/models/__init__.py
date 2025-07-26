import os
import importlib
from pathlib import Path

# Récupère le chemin absolu du dossier actuel (models)
models_dir = Path(__file__).resolve().parent

# Pour chaque fichier Python dans le dossier, sauf __init__.py et fichiers spéciaux
for file in os.listdir(models_dir):
    if file.endswith(".py") and file != "__init__.py" and not file.startswith("_"):
        module_name = file[:-3]  # retire le .py
        importlib.import_module(f"app.models.{module_name}")
