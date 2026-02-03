#!/bin/bash

# Quick deployment script for Streamlit Cloud
# This script helps prepare your app for Streamlit Cloud deployment

echo "🚀 Preparing for Streamlit Cloud Deployment"
echo "==========================================="
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
    echo "✅ Git initialized"
fi

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: requirements.txt not found!"
    exit 1
fi

# Check if app.py exists
if [ ! -f "app.py" ]; then
    echo "❌ Error: app.py not found!"
    exit 1
fi

echo "✅ All required files found"
echo ""
echo "📋 Next steps:"
echo "1. Create a GitHub repository (if you haven't already)"
echo "2. Push your code:"
echo "   git add ."
echo "   git commit -m 'Deploy to Streamlit Cloud'"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
echo "   git push -u origin main"
echo ""
echo "3. Go to https://share.streamlit.io"
echo "4. Sign in with GitHub"
echo "5. Click 'New app'"
echo "6. Select your repository"
echo "7. Set main file: app.py"
echo "8. Click 'Deploy'"
echo ""
echo "⏱️  Deployment takes ~2-5 minutes"
echo "📝 Note: First model download may take additional time"

