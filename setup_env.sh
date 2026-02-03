#!/bin/bash

# Setup script for Google Cloud TTS authentication
# This script helps you set up environment variables for authentication

echo "🔐 Google Cloud TTS Authentication Setup"
echo "========================================"
echo ""

# Check which shell we're using
if [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.profile"
fi

echo "Choose authentication method:"
echo "1) API Key (simpler, good for testing)"
echo "2) Service Account JSON file (more secure, recommended for production)"
echo ""
read -p "Enter choice (1 or 2): " choice

if [ "$choice" = "1" ]; then
    echo ""
    echo "To get an API key:"
    echo "1. Go to: https://console.cloud.google.com/apis/credentials"
    echo "2. Click 'Create Credentials' → 'API Key'"
    echo "3. Copy the API key"
    echo ""
    read -p "Enter your Google Cloud API key: " api_key
    
    if [ -z "$api_key" ]; then
        echo "❌ No API key provided. Exiting."
        exit 1
    fi
    
    # Set for current session
    export GOOGLE_API_KEY="$api_key"
    echo "✅ GOOGLE_API_KEY set for current session"
    
    # Add to shell RC file
    if grep -q "GOOGLE_API_KEY" "$SHELL_RC"; then
        echo "⚠️  GOOGLE_API_KEY already exists in $SHELL_RC"
        read -p "Do you want to update it? (y/n): " update
        if [ "$update" = "y" ]; then
            # Remove old entry and add new one
            sed -i.bak "/GOOGLE_API_KEY/d" "$SHELL_RC"
            echo "export GOOGLE_API_KEY=\"$api_key\"" >> "$SHELL_RC"
            echo "✅ Updated $SHELL_RC"
        fi
    else
        echo "" >> "$SHELL_RC"
        echo "# Google Cloud TTS API Key" >> "$SHELL_RC"
        echo "export GOOGLE_API_KEY=\"$api_key\"" >> "$SHELL_RC"
        echo "✅ Added GOOGLE_API_KEY to $SHELL_RC"
    fi
    
elif [ "$choice" = "2" ]; then
    echo ""
    echo "To get a service account key:"
    echo "1. Go to: https://console.cloud.google.com/iam-admin/serviceaccounts"
    echo "2. Create a service account or select existing"
    echo "3. Go to 'Keys' tab → 'Add Key' → 'Create new key' → JSON"
    echo "4. Download the JSON file"
    echo ""
    read -p "Enter full path to your service account JSON file: " json_path
    
    if [ ! -f "$json_path" ]; then
        echo "❌ File not found: $json_path"
        exit 1
    fi
    
    # Convert to absolute path
    json_path=$(cd "$(dirname "$json_path")" && pwd)/$(basename "$json_path")
    
    # Set for current session
    export GOOGLE_APPLICATION_CREDENTIALS="$json_path"
    echo "✅ GOOGLE_APPLICATION_CREDENTIALS set for current session"
    
    # Add to shell RC file
    if grep -q "GOOGLE_APPLICATION_CREDENTIALS" "$SHELL_RC"; then
        echo "⚠️  GOOGLE_APPLICATION_CREDENTIALS already exists in $SHELL_RC"
        read -p "Do you want to update it? (y/n): " update
        if [ "$update" = "y" ]; then
            # Remove old entry and add new one
            sed -i.bak "/GOOGLE_APPLICATION_CREDENTIALS/d" "$SHELL_RC"
            echo "export GOOGLE_APPLICATION_CREDENTIALS=\"$json_path\"" >> "$SHELL_RC"
            echo "✅ Updated $SHELL_RC"
        fi
    else
        echo "" >> "$SHELL_RC"
        echo "# Google Cloud Service Account Credentials" >> "$SHELL_RC"
        echo "export GOOGLE_APPLICATION_CREDENTIALS=\"$json_path\"" >> "$SHELL_RC"
        echo "✅ Added GOOGLE_APPLICATION_CREDENTIALS to $SHELL_RC"
    fi
else
    echo "❌ Invalid choice"
    exit 1
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To use in current session, run:"
if [ "$choice" = "1" ]; then
    echo "  export GOOGLE_API_KEY=\"$api_key\""
else
    echo "  export GOOGLE_APPLICATION_CREDENTIALS=\"$json_path\""
fi
echo ""
echo "Or open a new terminal to automatically load from $SHELL_RC"
echo ""
echo "Test it with:"
echo "  python -c \"from tajik_tts import synthesize_tajik_text; print('✅ Authentication working!')\""

