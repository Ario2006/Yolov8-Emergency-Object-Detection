#!/bin/bash
set -e

echo "🔧 Installing Python dependencies..."
pip install --upgrade pip
pip install -r python/requirements.txt

echo "📦 Installing Node.js dependencies..."
cd backend
npm install

echo "✅ Build complete!"
