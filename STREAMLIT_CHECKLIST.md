# ✅ Streamlit Cloud Deployment Checklist

## Required Files (Must Have)

- [x] `app.py` - Main application file
- [x] `tajik_tts.py` - TTS module
- [x] `requirements.txt` - Python dependencies
- [x] `.streamlit/config.toml` - Streamlit configuration (optional but recommended)
- [x] `.gitignore` - Excludes unnecessary files

## Optional but Recommended

- [x] `README.md` - Project documentation
- [x] `STREAMLIT_DEPLOY.md` - Deployment guide

## Files NOT Needed for Streamlit Cloud (Can Delete)

- `Dockerfile` - For Docker deployment only
- `Procfile` - For Heroku only
- `runtime.txt` - For Heroku only
- `.dockerignore` - For Docker only
- `deploy_streamlit_cloud.sh` - Helper script (optional)
- `DEPLOYMENT.md` - General deployment guide (keep if you want)
- `QUICK_DEPLOY.md` - Quick reference (keep if you want)

## Pre-Deployment Checklist

- [ ] Test locally: `streamlit run app.py`
- [ ] Verify all imports work
- [ ] Check that `requirements.txt` is complete
- [ ] Ensure no hardcoded absolute paths
- [ ] Remove any local test files (test_output.wav, etc.)
- [ ] Commit all files to git
- [ ] Push to GitHub

## Quick Deploy Steps

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Ready for Streamlit Cloud"
   git push
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to https://share.streamlit.io
   - Sign in with GitHub
   - Click "New app"
   - Select your repo
   - Main file: `app.py`
   - Click "Deploy"

3. **Wait 2-5 minutes** for deployment

4. **Share your URL!** 🎉

## Important Notes

- ✅ Model downloads automatically (first use may be slow)
- ✅ Works on all devices (mobile, tablet, desktop)
- ✅ HTTPS enabled automatically
- ✅ Free tier available (with limitations)
- ⚠️ App may sleep after 1 hour inactivity (free tier)
- ⚠️ Audio history is session-based (not persistent)

