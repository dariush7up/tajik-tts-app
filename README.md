# Tajik Text-to-Speech (TTS) Evaluation

This project provides tools for generating and evaluating Tajik text-to-speech using Facebook's MMS-TTS model.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

**Note:** For combining audio chunks, you'll also need `ffmpeg`:
```bash
brew install ffmpeg  # macOS
# or
apt-get install ffmpeg  # Linux
```
The app has a fallback method, but `ffmpeg` is recommended for best results.

### 2. No Authentication Needed!

The Facebook MMS-TTS model runs **locally** on your machine - no API keys, no billing, completely free!

The model will automatically download on first use (~140MB).

### 3. Run the Web Application

**Option A: Using the script**
```bash
./run_app.sh
```

**Option B: Direct command**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### 4. Or Use Programmatically

```python
from tajik_tts import synthesize_tajik_text

text = "Субҳ барвақт бедор шудам."
output = synthesize_tajik_text(text, "output.wav")
```

### 3. Use in Your Code

```python
from tajik_tts import synthesize_tajik_text

text = "Субҳ барвақт бедор шудам."
output = synthesize_tajik_text(text, "output.wav")
```

### 4. Use in Jupyter Notebook

```python
# In a notebook cell
import os
os.environ['GOOGLE_API_KEY'] = 'your-api-key'  # Or use service account

from tajik_tts import synthesize_tajik_text

text = "Субҳ барвақт бедор шудам."
output = synthesize_tajik_text(text, "output.wav")
```

## Files

- `app.py` - **Web application** (Streamlit frontend)
- `tajik_tts.py` - Main TTS module for generating audio
- `tts_tajik_subjective_methods.ipynb` - Notebook for evaluation metrics (VCS, RTF)
- `MMS_TTS_SETUP.md` - Detailed model setup guide
- `FRONTEND_README.md` - Web application documentation
- `setup_auth_example.py` - Code examples
- `requirements.txt` - Python dependencies
- `run_app.sh` - Quick start script for web app

## Features

- ✅ Generate audio from Tajik text using Facebook MMS-TTS model
- ✅ **Free** - No API keys or billing required
- ✅ **Local** - Runs entirely on your machine (privacy-friendly)
- ✅ **Tajik-specific** - Trained specifically for Tajik language
- ✅ Voice Cloning Similarity (VCS) evaluation
- ✅ Real-Time Factor (RTF) calculation
- ✅ Batch processing support
- ✅ Reproducible generation (with seed parameter)

## Model Information

- **Model**: `facebook/mms-tts-tgk`
- **Source**: [Hugging Face](https://huggingface.co/facebook/mms-tts-tgk)
- **License**: CC-BY-NC 4.0
- **Size**: ~140MB (auto-downloads on first use)

For detailed setup and usage, see [MMS_TTS_SETUP.md](MMS_TTS_SETUP.md).

## 🚀 Deployment

Want to deploy this app so others can use it? See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment guide.

**Quick options:**
- **Streamlit Cloud** (easiest, free): [share.streamlit.io](https://share.streamlit.io)
- **Docker** (production-ready): See `Dockerfile`
- **Heroku**: See `Procfile` and `runtime.txt`

Run `./deploy_streamlit_cloud.sh` for quick deployment guide.

