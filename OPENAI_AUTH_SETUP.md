# OpenAI API Authentication Setup

This guide explains how to set up authentication for OpenAI Text-to-Speech API.

## Quick Setup (Option 1: Environment Variable)

### Step 1: Get Your API Key
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Click **Create new secret key**
4. Copy the API key (you'll only see it once!)

### Step 2: Set Environment Variable

**On macOS/Linux:**
```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

**To make it permanent (add to ~/.zshrc or ~/.bashrc):**
```bash
echo 'export OPENAI_API_KEY="sk-your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

**In Jupyter Notebook:**
```python
import os
os.environ['OPENAI_API_KEY'] = 'sk-your-api-key-here'
```

**In Python script:**
```python
import os
os.environ['OPENAI_API_KEY'] = 'sk-your-api-key-here'
from tajik_tts import synthesize_tajik_text
```

---

## Option 2: Using .env File (Recommended for Projects)

### Step 1: Create .env file
Create a file named `.env` in your project directory:

```bash
# .env file
OPENAI_API_KEY=sk-your-api-key-here
```

### Step 2: Install python-dotenv
```bash
pip install python-dotenv
```

### Step 3: Use in your code
The `tajik_tts.py` module automatically loads `.env` file, so you don't need to do anything extra!

```python
from tajik_tts import synthesize_tajik_text

# .env is loaded automatically
text = "Субҳ барвақт бедор шудам."
output = synthesize_tajik_text(text, "output.mp3")
```

**⚠️ Important:** Add `.env` to your `.gitignore` to avoid committing credentials!

---

## Option 3: Set in Code (Quick Testing)

For quick testing, you can set it directly in code:

```python
import os
os.environ['OPENAI_API_KEY'] = 'sk-your-api-key-here'

from tajik_tts import synthesize_tajik_text
```

---

## Quick Test

After setting up authentication, test it:

```python
from tajik_tts import synthesize_tajik_text

text = "Субҳ барвақт бедор шудам."
output = synthesize_tajik_text(text, "test.mp3")
print(f"✅ Success! Audio saved to: {output}")
```

---

## Pricing & Billing

OpenAI TTS API is pay-per-use:
- **tts-1**: $15.00 per 1M characters
- **tts-1-hd**: $30.00 per 1M characters

Make sure you have:
1. Added a payment method to your OpenAI account
2. Set up billing limits (optional but recommended)
3. Checked your usage: https://platform.openai.com/usage

---

## Troubleshooting

### Error: "OPENAI_API_KEY not found"
- Make sure you've set the environment variable correctly
- Check that the variable name is exactly `OPENAI_API_KEY`
- Try running `echo $OPENAI_API_KEY` in terminal to verify

### Error: "Incorrect API key provided"
- Verify your API key is correct
- Make sure there are no extra spaces or quotes
- Get a new key from https://platform.openai.com/api-keys

### Error: "You exceeded your current quota"
- Check your OpenAI account billing and usage
- Add payment method if needed
- Check usage limits: https://platform.openai.com/usage

### Error: "Rate limit exceeded"
- You're making too many requests too quickly
- Wait a moment and try again
- Consider using rate limiting in your code

---

## Available Voices

OpenAI TTS supports these voices:
- **alloy** - Neutral, balanced voice
- **echo** - Clear, professional voice
- **fable** - Warm, friendly voice
- **onyx** - Deep, authoritative voice
- **nova** - Bright, energetic voice
- **shimmer** - Soft, gentle voice

## Available Models

- **tts-1** - Faster, standard quality (recommended for most use cases)
- **tts-1-hd** - Slower, higher quality (use for final production)

---

## Example Usage

```python
from tajik_tts import synthesize_tajik_text

# Basic usage
output = synthesize_tajik_text("Субҳ барвақт бедор шудам.", "output.mp3")

# With custom voice
output = synthesize_tajik_text(
    "Субҳ барвақт бедор шудам.",
    "output.mp3",
    voice="nova"
)

# With HD model
output = synthesize_tajik_text(
    "Субҳ барвақт бедор шудам.",
    "output.mp3",
    model="tts-1-hd"
)
```

