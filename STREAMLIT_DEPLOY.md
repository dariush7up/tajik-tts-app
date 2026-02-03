# Deploy to Streamlit Cloud - Step by Step

## 📋 Required Files (Already Included)

✅ `app.py` - Main application  
✅ `tajik_tts.py` - TTS module  
✅ `requirements.txt` - Dependencies  
✅ `.streamlit/config.toml` - Streamlit config (optional)  
✅ `.gitignore` - Git ignore rules  

## 🚀 Deployment Steps

### Step 1: Initialize Git (if not already done)

```bash
git init
git add .
git commit -m "Initial commit - Tajik TTS app"
```

### Step 2: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click "New repository"
3. Name it (e.g., `tajik-tts-app`)
4. **Don't** initialize with README (you already have files)
5. Click "Create repository"

### Step 3: Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace:
- `YOUR_USERNAME` with your GitHub username
- `YOUR_REPO_NAME` with your repository name

### Step 4: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your **GitHub account**
3. Click **"New app"** button
4. Fill in:
   - **Repository**: Select your repository
   - **Branch**: `main` (or `master`)
   - **Main file**: `app.py`
   - **App URL**: Choose a name (e.g., `tajik-tts`)
5. Click **"Deploy"**

### Step 5: Wait for Deployment

- First deployment: ~2-5 minutes
- Model download: Additional 1-2 minutes on first use
- You'll see progress in the deployment log

### Step 6: Access Your App

Once deployed, you'll get a URL like:
```
https://YOUR-APP-NAME.streamlit.app
```

Share this URL with anyone - they can access it from any device!

---

## ⚠️ Important Notes

### Model Download
- The model (~140MB) downloads automatically on first use
- First request may take 1-2 minutes
- Subsequent requests are faster

### Resource Limits (Free Tier)
- Apps may sleep after 1 hour of inactivity
- Wake up takes ~30 seconds
- Consider upgrading for always-on

### File Storage
- Audio history is stored in session (lost on refresh)
- For persistent storage, consider cloud storage (future enhancement)

### Dependencies
All dependencies are in `requirements.txt`:
- transformers (for MMS-TTS model)
- torch (PyTorch)
- scipy (audio processing)
- streamlit (web framework)
- pydub (audio combining)

---

## 🔧 Troubleshooting

### Deployment Fails
- Check that `app.py` exists
- Verify `requirements.txt` is correct
- Check deployment logs for errors

### Model Download Timeout
- First request may timeout - just refresh
- Model caches after first download
- Consider upgrading to paid tier for more resources

### App Not Loading
- Check deployment status in Streamlit Cloud dashboard
- Review logs for errors
- Verify all files are pushed to GitHub

### Audio Not Working
- Check browser console for errors
- Verify ffmpeg dependencies (handled automatically)
- Try different browser

---

## 📱 Mobile Access

Your app works on:
- ✅ iPhone/iPad (Safari, Chrome)
- ✅ Android phones/tablets (Chrome, Firefox)
- ✅ Desktop browsers (Chrome, Firefox, Safari, Edge)

Just share the URL - no app installation needed!

---

## 🔄 Updating Your App

1. Make changes to your files
2. Commit and push:
   ```bash
   git add .
   git commit -m "Update app"
   git push
   ```
3. Streamlit Cloud auto-updates (takes ~1-2 minutes)

---

## 💡 Tips

- **Custom Domain**: Upgrade to add custom domain
- **Private Repos**: Requires paid Streamlit Cloud plan
- **Environment Variables**: Add in Streamlit Cloud settings if needed
- **Secrets**: Use Streamlit secrets for API keys (not needed for this app)

---

## ✅ Checklist Before Deploying

- [ ] All files committed to git
- [ ] Pushed to GitHub
- [ ] `app.py` is the main file
- [ ] `requirements.txt` includes all dependencies
- [ ] Tested locally with `streamlit run app.py`
- [ ] No hardcoded paths (use relative paths)
- [ ] `.gitignore` excludes sensitive files

---

## 🎉 You're Ready!

Once deployed, your app will be:
- ✅ Accessible from any device
- ✅ HTTPS enabled (secure)
- ✅ Auto-updating on git push
- ✅ Free (with limitations)

Enjoy your deployed Tajik TTS app! 🎙️

