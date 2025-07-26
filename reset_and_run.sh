#!/bin/bash

echo "Nettoyage complet des conteneurs et volumes..."
docker rm -f fastapi_app 2>/dev/null || echo "Conteneur 'fastapi_app' non trouvé, pas de suppression nécessaire."
docker-compose down -v

echo "Nettoyage des ressources Docker inutilisées..."
docker system prune -f

echo "Reconstruction des images Docker..."
docker-compose build

echo "Démarrage des services..."
docker-compose up -d

echo "✅ Le projet est lancé. API disponible sur http://localhost:8000/docs"
