# Google Cloud Authentication Setup

This guide explains how to set up authentication for Google Cloud Text-to-Speech API.

## Option 1: Service Account (Recommended for Production)

### Step 1: Create a Service Account
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project (or create a new one)
3. Navigate to **IAM & Admin** → **Service Accounts**
4. Click **Create Service Account**
5. Give it a name (e.g., "tts-tajik-service")
6. Click **Create and Continue**
7. Grant role: **Cloud Text-to-Speech API User**
8. Click **Done**

### Step 2: Create and Download Key
1. Click on the service account you just created
2. Go to **Keys** tab
3. Click **Add Key** → **Create new key**
4. Choose **JSON** format
5. Download the JSON file (e.g., `tts-tajik-key.json`)

### Step 3: Set Environment Variable

**On macOS/Linux:**
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/tts-tajik-key.json"
```

**In your terminal (add to ~/.zshrc or ~/.bashrc for persistence):**
```bash
echo 'export GOOGLE_APPLICATION_CREDENTIALS="/Users/dariush.ubaydi@cognitedata.com/workspace/tts tajik/tts-tajik-key.json"' >> ~/.zshrc
source ~/.zshrc
```

**In Jupyter Notebook:**
```python
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/tts-tajik-key.json'
```

**In Python script:**
```python
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/tts-tajik-key.json'
from tajik_tts import synthesize_tajik_text
```

---

## Option 2: API Key (Simpler for Testing)

### Step 1: Enable Text-to-Speech API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to **APIs & Services** → **Library**
3. Search for "Cloud Text-to-Speech API"
4. Click **Enable**

### Step 2: Create API Key
1. Go to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **API Key**
3. Copy the API key
4. (Optional) Click **Restrict Key** to limit usage to Text-to-Speech API only

### Step 3: Set Environment Variable

**On macOS/Linux:**
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

**In your terminal (add to ~/.zshrc for persistence):**
```bash
echo 'export GOOGLE_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

**In Jupyter Notebook:**
```python
import os
os.environ['GOOGLE_API_KEY'] = 'your-api-key-here'
```

**In Python script:**
```python
import os
os.environ['GOOGLE_API_KEY'] = 'your-api-key-here'
from tajik_tts import synthesize_tajik_text
```

---

## Option 3: Using .env File (Recommended for Projects)

### Step 1: Create .env file
Create a file named `.env` in your project directory:

```bash
# .env file
GOOGLE_API_KEY=your-api-key-here
# OR
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
```

### Step 2: Install python-dotenv
```bash
pip install python-dotenv
```

### Step 3: Load in your code
```python
from dotenv import load_dotenv
load_dotenv()  # Loads .env file

from tajik_tts import synthesize_tajik_text
```

**⚠️ Important:** Add `.env` to your `.gitignore` to avoid committing credentials!

---

## Quick Test

After setting up authentication, test it:

```python
from tajik_tts import synthesize_tajik_text

text = "Субҳ барвақт бедор шудам."
output = synthesize_tajik_text(text, "test.wav")
print(f"✅ Success! Audio saved to: {output}")
```

---

## Troubleshooting

### Error: "No credentials found"
- Make sure you've set the environment variable correctly
- Check that the path to the JSON file is correct (use absolute path)
- Verify the JSON file is valid

### Error: "API not enabled"
- Go to Google Cloud Console → APIs & Services → Library
- Enable "Cloud Text-to-Speech API"

### Error: "Billing not enabled"
- Google Cloud requires billing to be enabled for TTS API
- Go to Billing in Google Cloud Console and set up billing

### Error: "Permission denied"
- For service account: Make sure it has "Cloud Text-to-Speech API User" role
- For API key: Make sure Text-to-Speech API is enabled

