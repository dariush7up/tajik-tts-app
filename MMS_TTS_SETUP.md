# Facebook MMS-TTS Setup Guide

This guide explains how to use Facebook's Massively Multilingual Speech (MMS) Text-to-Speech model for Tajik language.

## Model Information

- **Model**: `facebook/mms-tts-tgk`
- **Source**: [Hugging Face Model Page](https://huggingface.co/facebook/mms-tts-tgk)
- **Language**: Tajik (tgk)
- **License**: CC-BY-NC 4.0
- **Model Type**: VITS (Variational Inference with adversarial learning)
- **Size**: ~140MB (downloads automatically on first use)

## Advantages

✅ **Free** - No API keys or billing required  
✅ **Local** - Runs entirely on your machine  
✅ **Privacy** - Your data never leaves your computer  
✅ **Tajik-specific** - Trained specifically for Tajik language  
✅ **Offline** - Works without internet after initial download  

## Installation

### 1. Install Required Packages

```bash
pip install transformers torch scipy accelerate
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

### 2. First Run

The model will automatically download on first use (~140MB). Make sure you have:
- Internet connection (for first download)
- ~200MB free disk space
- Python 3.8 or higher

## Usage

### Basic Usage

```python
from tajik_tts import synthesize_tajik_text

text = "Субҳ барвақт бедор шудам. Ба ошхона рафтам ва чой нӯшидем."
output = synthesize_tajik_text(text, "output.wav")
```

### With Reproducibility (Fixed Seed)

```python
from tajik_tts import synthesize_tajik_text

text = "Субҳ барвақт бедор шудам."
# Same seed = same audio output
output1 = synthesize_tajik_text(text, "output1.wav", seed=42)
output2 = synthesize_tajik_text(text, "output2.wav", seed=42)  # Same as output1
```

### Batch Processing

```python
from tajik_tts import synthesize_tajik_text_batch

texts = [
    "Субҳ барвақт бедор шудам.",
    "Ба ошхона рафтам ва чой нӯшидем.",
    "Субҳона омода кардам ва ба хона хӯрок хӯрдем."
]

output_files = synthesize_tajik_text_batch(
    texts, 
    output_dir="outputs",
    prefix="tajik_audio"
)
```

### In Jupyter Notebook

```python
from tajik_tts import synthesize_tajik_text
from IPython.display import Audio
import scipy.io.wavfile

# Generate audio
text = "Субҳ барвақт бедор шудам."
output_file = synthesize_tajik_text(text, "output.wav")

# Play in notebook
sampling_rate, audio_data = scipy.io.wavfile.read(output_file)
Audio(audio_data, rate=sampling_rate)
```

### Get Model Information

```python
from tajik_tts import get_model_info

info = get_model_info()
print(info)
```

## Performance Tips

1. **First Load**: The model loads on first use (~5-10 seconds). Subsequent calls are faster.
2. **GPU Acceleration**: If you have a GPU, PyTorch will automatically use it for faster generation.
3. **Batch Processing**: Use `synthesize_tajik_text_batch()` for multiple texts to avoid reloading the model.

## Troubleshooting

### Error: "transformers library is not installed"
```bash
pip install transformers torch scipy accelerate
```

### Error: "No internet connection"
- First run requires internet to download the model
- After download, model is cached locally and works offline

### Error: "Out of memory"
- The model requires ~500MB RAM
- Close other applications or use a machine with more memory

### Slow Generation
- First generation is slower (model loading)
- Consider using GPU for faster inference
- Install PyTorch with CUDA: `pip install torch --index-url https://download.pytorch.org/whl/cu118`

### Model Download Issues
- Check internet connection
- Model is downloaded to: `~/.cache/huggingface/hub/`
- You can manually download from: https://huggingface.co/facebook/mms-tts-tgk

## Model Details

- **Architecture**: VITS (Variational Inference with adversarial learning)
- **Sampling Rate**: 16,000 Hz
- **Training**: Trained on Tajik language data
- **Non-deterministic**: Same text can produce slightly different audio (use `seed` parameter for reproducibility)

## Citation

If you use this model, please cite:

```bibtex
@article{pratap2023mms,
    title={Scaling Speech Technology to 1,000+ Languages},
    author={Vineel Pratap and Andros Tjandra and Bowen Shi and Paden Tomasello and Arun Babu and Sayani Kundu and Ali Elkahky and Zhaoheng Ni and Apoorv Vyas and Maryam Fazel-Zarandi and Alexei Baevski and Yossi Adi and Xiaohui Zhang and Wei-Ning Hsu and Alexis Conneau and Michael Auli},
    journal={arXiv},
    year={2023}
}
```

## License

This model is licensed under **CC-BY-NC 4.0** (Creative Commons Attribution-NonCommercial 4.0). See the [model card](https://huggingface.co/facebook/mms-tts-tgk) for details.

