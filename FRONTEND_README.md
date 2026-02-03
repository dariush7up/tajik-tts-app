# Tajik TTS Web Application

A beautiful web interface for generating Tajik text-to-speech audio using Facebook's MMS-TTS model.

## Features

✨ **User-Friendly Interface**
- Clean, modern web interface
- Real-time text input with character counter
- Audio preview player
- One-click audio download

🎛️ **Customizable Parameters**
- Fixed seed for reproducible results
- Automatic text splitting for long texts
- Adjustable chunk size for processing

📊 **Model Information**
- Display model details in sidebar
- Link to Hugging Face model page
- Real-time generation status

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This includes:
- `streamlit` - Web framework
- `transformers` - Hugging Face models
- `torch` - PyTorch for model inference
- `scipy` - Audio file handling
- `pydub` - Audio processing (for combining chunks)

### 2. Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## Usage

### Basic Usage

1. **Enter Text**: Type or paste Tajik text in the text area
2. **Adjust Settings** (optional):
   - Enable fixed seed for reproducible results
   - Adjust text splitting options
3. **Generate**: Click "Generate Audio" button
4. **Download**: Click "Download Audio" to save the file

### Advanced Features

#### Fixed Seed
- Enable "Use fixed seed" checkbox
- Set a seed value (0-999999)
- Same seed + same text = identical audio
- Different seed = natural variation

#### Long Text Processing
- Enable "Auto-split long text" (default: ON)
- Adjust "Max characters per chunk" slider
- Text is automatically split into sentences
- Audio chunks are combined into single file

## Application Structure

```
app.py                 # Main Streamlit application
tajik_tts.py          # TTS generation module
requirements.txt      # Python dependencies
```

## Deployment

### Local Development
```bash
streamlit run app.py
```

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Deploy to Other Platforms

The app can be deployed to:
- **Heroku**: Add `Procfile` with `web: streamlit run app.py --server.port=$PORT`
- **Docker**: Create Dockerfile with Streamlit
- **AWS/GCP/Azure**: Use container services

## Customization

### Change Theme

Edit the CSS in `app.py`:
```python
st.markdown("""
<style>
    .main-header {
        color: #your-color;
    }
</style>
""", unsafe_allow_html=True)
```

### Add More Parameters

Edit the sidebar section in `app.py` to add more model parameters.

### Change Model

To use a different model, update `tajik_tts.py`:
```python
_model = VitsModel.from_pretrained("your-model-name")
```

## Troubleshooting

### App won't start
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8+)

### Model download issues
- First run requires internet connection
- Model downloads to `~/.cache/huggingface/hub/`
- Check disk space (~200MB needed)

### Audio generation slow
- First generation loads model (~5-10 seconds)
- Subsequent generations are faster
- Consider using GPU for faster inference

### Long text issues
- Enable "Auto-split long text"
- Reduce "Max characters per chunk"
- Check available memory

## Performance Tips

1. **First Load**: Model loads on first generation (~5-10s)
2. **Caching**: Model stays in memory for faster subsequent generations
3. **GPU**: Install PyTorch with CUDA for faster inference
4. **Text Splitting**: Use for texts >500 characters

## Browser Compatibility

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ⚠️ Mobile browsers (may have limitations)

## Security Notes

- The app runs locally by default
- No data is sent to external servers (except model download)
- Audio files are generated on your machine
- Consider authentication for production deployments

## License

- Application code: Your license
- Model: CC-BY-NC 4.0 (see [model card](https://huggingface.co/facebook/mms-tts-tgk))

## Support

For issues or questions:
1. Check [MMS_TTS_SETUP.md](MMS_TTS_SETUP.md) for model setup
2. Review Streamlit documentation: https://docs.streamlit.io
3. Check model page: https://huggingface.co/facebook/mms-tts-tgk

