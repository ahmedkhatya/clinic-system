#!/bin/bash

echo "🚀 Starting Clinic System..."

# تحقق إن .env موجود
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "📋 Copy .env.example to .env and fill in the values:"
    echo "   cp .env.example .env"
    exit 1
fi

# سجّل دخول لـ GHCR
echo "🔐 Logging in to GitHub Container Registry..."
echo $GITHUB_TOKEN | docker login ghcr.io -u $GITHUB_USERNAME --password-stdin

# Pull آخر إصدار
echo "📦 Pulling latest images..."
docker-compose pull

# شغّل
echo "▶️ Starting containers..."
docker-compose up -d

echo "✅ Done! App is running on http://localhost:8000"
