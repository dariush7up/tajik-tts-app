# Deployment Guide for Tajik TTS Application

This guide covers various deployment options for your Streamlit TTS application.

## 🚀 Quick Comparison

| Platform | Difficulty | Cost | Setup Time | Best For |
|----------|-----------|------|------------|----------|
| **Streamlit Cloud** | ⭐ Easy | Free | 5 min | Quick deployment, testing |
| **Docker + Cloud Run** | ⭐⭐ Medium | Pay-per-use | 15 min | Production, scalable |
| **Heroku** | ⭐⭐ Medium | $7-25/mo | 20 min | Simple production |
| **AWS/GCP/Azure** | ⭐⭐⭐ Advanced | Variable | 30+ min | Enterprise, high traffic |
| **Self-hosted** | ⭐⭐⭐ Advanced | Server cost | 30+ min | Full control |

---

## Option 1: Streamlit Cloud (Recommended for Start) ⭐

**Best for:** Quick deployment, testing, sharing with users

### Pros:
- ✅ **Free** (with limitations)
- ✅ **Easiest setup** - just connect GitHub
- ✅ **Automatic HTTPS**
- ✅ **Works on all devices**
- ✅ **No server management**

### Cons:
- ⚠️ Limited resources (may be slow with large models)
- ⚠️ Public repos only (free tier)
- ⚠️ Model download on first use (may timeout)

### Steps:

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/tts-tajik.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file: `app.py`
   - Click "Deploy"

3. **Wait for deployment** (~2-5 minutes)

### Important Notes:
- Model downloads on first use (may take time)
- Free tier has resource limits
- Consider using model caching

---

## Option 2: Docker + Google Cloud Run ⭐⭐

**Best for:** Production deployment, scalable, pay-per-use

### Pros:
- ✅ **Pay only when used** (very cheap)
- ✅ **Auto-scaling**
- ✅ **HTTPS included**
- ✅ **Works on all devices**
- ✅ **No server management**

### Cons:
- ⚠️ Requires Docker knowledge
- ⚠️ Cold starts (first request slower)

### Steps:

1. **Create Dockerfile:**
   ```dockerfile
   FROM python:3.11-slim

   WORKDIR /app

   # Install system dependencies
   RUN apt-get update && apt-get install -y \
       ffmpeg \
       && rm -rf /var/lib/apt/lists/*

   # Copy requirements
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy application
   COPY . .

   # Expose port
   EXPOSE 8501

   # Run Streamlit
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Create .dockerignore:**
   ```
   __pycache__
   *.pyc
   .venv
   venv
   .git
   audio_history/
   *.wav
   .env
   ```

3. **Build and deploy:**
   ```bash
   # Install gcloud CLI
   # Build Docker image
   docker build -t gcr.io/YOUR_PROJECT/tts-tajik .
   
   # Push to Google Container Registry
   docker push gcr.io/YOUR_PROJECT/tts-tajik
   
   # Deploy to Cloud Run
   gcloud run deploy tts-tajik \
     --image gcr.io/YOUR_PROJECT/tts-tajik \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --memory 2Gi \
     --timeout 300
   ```

---

## Option 3: Heroku ⭐⭐

**Best for:** Simple production deployment

### Pros:
- ✅ Easy setup
- ✅ Good documentation
- ✅ Add-ons available

### Cons:
- ⚠️ Costs $7-25/month
- ⚠️ Sleeps after inactivity (free tier)

### Steps:

1. **Create Procfile:**
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Create runtime.txt:**
   ```
   python-3.11.13
   ```

3. **Create setup.sh:**
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   " > ~/.streamlit/config.toml
   ```

4. **Update requirements.txt** (add buildpack requirements if needed)

5. **Deploy:**
   ```bash
   heroku create tts-tajik
   heroku buildpacks:add heroku/python
   heroku buildpacks:add https://github.com/heroku/heroku-buildpack-ffmpeg
   git push heroku main
   ```

---

## Option 4: AWS/GCP/Azure (Advanced) ⭐⭐⭐

### AWS (EC2 + Elastic Beanstalk)

1. **Launch EC2 instance** (t2.medium or larger)
2. **Install dependencies:**
   ```bash
   sudo apt update
   sudo apt install python3-pip ffmpeg
   pip3 install -r requirements.txt
   ```
3. **Run with systemd** or use Elastic Beanstalk

### Google Cloud Platform (App Engine)

1. **Create app.yaml:**
   ```yaml
   runtime: python311
   instance_class: F2
   
   handlers:
   - url: /.*
     script: auto
   ```

2. **Deploy:**
   ```bash
   gcloud app deploy
   ```

### Azure (App Service)

1. **Create App Service** via Azure Portal
2. **Configure deployment** from GitHub
3. **Set startup command:**
   ```
   streamlit run app.py --server.port=8000 --server.address=0.0.0.0
   ```

---

## Option 5: Self-Hosted (VPS) ⭐⭐⭐

**Best for:** Full control, custom setup

### Steps:

1. **Rent VPS** (DigitalOcean, Linode, Vultr, etc.)
2. **Install dependencies:**
   ```bash
   sudo apt update
   sudo apt install python3-pip ffmpeg nginx
   pip3 install -r requirements.txt
   ```

3. **Run with systemd:**
   Create `/etc/systemd/system/tts-tajik.service`:
   ```ini
   [Unit]
   Description=Tajik TTS Streamlit App
   After=network.target

   [Service]
   Type=simple
   User=youruser
   WorkingDirectory=/path/to/app
   ExecStart=/usr/bin/streamlit run app.py --server.port=8501
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

4. **Setup Nginx reverse proxy:**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       location / {
           proxy_pass http://localhost:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Host $host;
       }
   }
   ```

5. **Enable HTTPS** with Let's Encrypt:
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d yourdomain.com
   ```

---

## 🎯 Recommendations by Use Case

### For Testing/Sharing:
→ **Streamlit Cloud** (free, easiest)

### For Production (Low-Medium Traffic):
→ **Google Cloud Run** (pay-per-use, scalable)

### For Production (High Traffic):
→ **AWS/GCP with load balancer**

### For Full Control:
→ **Self-hosted VPS**

---

## ⚠️ Important Considerations

### 1. Model Size (~140MB)
- First download may timeout on free tiers
- Consider pre-downloading model in Docker image
- Use model caching

### 2. Memory Requirements
- Model needs ~500MB RAM
- Recommend at least 1GB for app
- Cloud Run: Use 2GB memory

### 3. Cold Starts
- First request after inactivity is slower
- Model loads on first use
- Consider keeping instance warm

### 4. File Storage
- Audio history stored locally (lost on restart)
- Consider cloud storage (S3, GCS) for persistence
- Or use database for metadata

### 5. Dependencies
- `ffmpeg` required (install in Docker/system)
- PyTorch can be large (~1GB)
- Consider CPU-only PyTorch for smaller size

---

## 🔧 Optimization Tips

### 1. Pre-download Model in Docker:
```dockerfile
# Add to Dockerfile
RUN python -c "from transformers import VitsModel; VitsModel.from_pretrained('facebook/mms-tts-tgk')"
```

### 2. Use CPU-only PyTorch:
```dockerfile
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### 3. Add Health Check:
```python
# Add to app.py
@app.route('/health')
def health():
    return {'status': 'ok'}
```

### 4. Environment Variables:
- Set `STREAMLIT_SERVER_HEADLESS=true`
- Configure `STREAMLIT_SERVER_PORT`
- Add any API keys if needed

---

## 📱 Mobile Compatibility

All options work on mobile browsers, but:
- ✅ Streamlit is responsive
- ✅ Touch-friendly interface
- ⚠️ Large models may be slow on mobile
- ⚠️ Audio playback works on all devices

---

## 🧪 Testing Before Deployment

1. **Test locally:**
   ```bash
   streamlit run app.py
   ```

2. **Test with Docker:**
   ```bash
   docker build -t tts-tajik .
   docker run -p 8501:8501 tts-tajik
   ```

3. **Check all features:**
   - Text input
   - Audio generation
   - History saving
   - Download functionality

---

## 📞 Support

For deployment issues:
- Streamlit Cloud: [community.streamlit.io](https://community.streamlit.io)
- Docker: Check logs with `docker logs`
- Cloud platforms: Check platform-specific documentation

