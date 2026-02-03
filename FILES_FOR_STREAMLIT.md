# Files Needed for Streamlit Cloud Deployment

## ✅ REQUIRED FILES (Must Keep)

These files are **essential** for Streamlit Cloud:

1. **`app.py`** - Main Streamlit application
2. **`tajik_tts.py`** - TTS generation module
3. **`requirements.txt`** - Python dependencies
4. **`.streamlit/config.toml`** - Streamlit configuration (optional but recommended)
5. **`.gitignore`** - Excludes unnecessary files from git

## 📚 DOCUMENTATION (Optional but Helpful)

- `README.md` - Project overview
- `STREAMLIT_DEPLOY.md` - Step-by-step deployment guide
- `STREAMLIT_CHECKLIST.md` - Quick checklist

## ❌ FILES NOT NEEDED (Can Delete or Ignore)

These are for other deployment methods, **not needed for Streamlit Cloud**:

- `Dockerfile` - For Docker deployment
- `.dockerignore` - For Docker
- `Procfile` - For Heroku
- `runtime.txt` - For Heroku
- `deploy_streamlit_cloud.sh` - Helper script (optional)
- `DEPLOYMENT.md` - General deployment guide (keep if you want reference)
- `QUICK_DEPLOY.md` - Quick reference (keep if you want)
- `streamlit_requirements.txt` - Duplicate of requirements.txt

## 🗑️ FILES TO EXCLUDE FROM GIT

These are already in `.gitignore` (don't commit):

- `audio_history/` - Generated audio files
- `*.wav` - Audio output files
- `__pycache__/` - Python cache
- `.venv/` - Virtual environment
- `.env` - Environment variables

## 📝 Quick Summary

**Minimum files to deploy:**
```
app.py
tajik_tts.py
requirements.txt
.gitignore
```

**Recommended (includes docs):**
```
app.py
tajik_tts.py
requirements.txt
.gitignore
.streamlit/config.toml
README.md
STREAMLIT_DEPLOY.md
```

## 🚀 Ready to Deploy?

1. Make sure you have the required files above
2. Follow `STREAMLIT_DEPLOY.md` for step-by-step instructions
3. Push to GitHub
4. Deploy on share.streamlit.io

That's it! 🎉

