#!/bin/bash

set -e

LOG_DIR="logs"
mkdir -p "$LOG_DIR"
NOW=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_FILE="$LOG_DIR/test_$NOW.log"

echo "📁 Log enregistré dans : $LOG_FILE"

CONTAINER_NAME="fastapi_app"
STATUS=$(docker inspect -f '{{.State.Status}}' $CONTAINER_NAME 2>/dev/null || echo "notfound")

if [ "$STATUS" == "exited" ]; then
    echo "♻️ Redémarrage du conteneur..."
    docker start $CONTAINER_NAME
elif [ "$STATUS" == "notfound" ]; then
    echo "❌ Le conteneur n'existe pas. Lancement complet..."
    docker-compose up -d --build
    sleep 5
fi

status_after=$(docker inspect -f '{{.State.Status}}' $CONTAINER_NAME)
if [ "$status_after" != "running" ]; then
    echo "❌ Le conteneur a planté. Logs :"
    docker logs $CONTAINER_NAME | tee -a "$LOG_FILE"
    exit 1
fi

echo "🧪 Exécution des tests..."
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
docker exec -i $CONTAINER_NAME pytest tests/ | tee -a "$LOG_FILE"
echo "✅ Tests terminés à $(date)"
