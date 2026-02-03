#!/bin/bash

# Run the Tajik TTS Web Application

echo "🎙️ Starting Tajik TTS Web Application..."
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit is not installed!"
    echo "   Install with: pip install streamlit"
    exit 1
fi

# Check if port 8501 is in use, if so, use alternative port
if lsof -Pi :8501 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "⚠️  Port 8501 is already in use. Using port 8502 instead..."
    streamlit run app.py --server.port 8502
else
    streamlit run app.py
fi
