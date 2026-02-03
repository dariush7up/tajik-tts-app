# Quick Deployment Guide

## 🚀 Fastest Option: Streamlit Cloud (5 minutes)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Deploy Tajik TTS app"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 2: Deploy
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select repository
5. Main file: `app.py`
6. Click "Deploy"

**Done!** Your app will be live in ~2-5 minutes.

---

## 🐳 Docker Deployment (15 minutes)

### For Google Cloud Run:

```bash
# Build
docker build -t gcr.io/YOUR_PROJECT/tts-tajik .

# Push
docker push gcr.io/YOUR_PROJECT/tts-tajik

# Deploy
gcloud run deploy tts-tajik \
  --image gcr.io/YOUR_PROJECT/tts-tajik \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 2Gi \
  --timeout 300
```

### For Any Docker Host:

```bash
docker build -t tts-tajik .
docker run -p 8501:8501 tts-tajik
```

Access at `http://localhost:8501`

---

## ⚠️ Important Notes

1. **Model Download**: First request may be slow (model downloads)
2. **Memory**: Need at least 1GB RAM (2GB recommended)
3. **ffmpeg**: Included in Dockerfile, install separately for other methods
4. **HTTPS**: All cloud platforms provide HTTPS automatically

---

## 📱 Mobile Compatibility

✅ Works on all devices (iOS, Android, tablets)
✅ Responsive design
✅ Touch-friendly interface

---

## 🔧 Troubleshooting

**App won't start:**
- Check logs: `docker logs <container>`
- Verify port is exposed: `-p 8501:8501`
- Check memory limits (need 2GB+)

**Model download timeout:**
- Pre-download in Dockerfile (already done)
- Increase timeout settings
- Use larger instance

**Audio not working:**
- Verify ffmpeg is installed
- Check file permissions
- Review error logs

