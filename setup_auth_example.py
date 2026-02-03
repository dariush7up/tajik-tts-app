"""
Example: How to use Facebook MMS-TTS for Tajik

This file shows different ways to use the MMS-TTS model.
No authentication needed - it runs locally!
"""

# ============================================
# Basic Usage
# ============================================
from tajik_tts import synthesize_tajik_text

text = "Субҳ барвақт бедор шудам. Ба ошхона рафтам ва чой нӯшидем."
output = synthesize_tajik_text(text, "output.wav")

# That's it! No API keys, no authentication needed!


# ============================================
# With Reproducibility (Fixed Seed)
# ============================================
from tajik_tts import synthesize_tajik_text

text = "Субҳ барвақт бедор шудам."

# Same seed = same audio output
output1 = synthesize_tajik_text(text, "output1.wav", seed=42)
output2 = synthesize_tajik_text(text, "output2.wav", seed=42)  # Identical to output1

# Different seed = different audio (natural variation)
output3 = synthesize_tajik_text(text, "output3.wav", seed=123)  # Different from output1


# ============================================
# Batch Processing
# ============================================
from tajik_tts import synthesize_tajik_text_batch

texts = [
    "Субҳ барвақт бедор шудам.",
    "Ба ошхона рафтам ва чой нӯшидем.",
    "Субҳона омода кардам ва ба хона хӯрок хӯрдем.",
    "Баъд ба бозор рафтам."
]

output_files = synthesize_tajik_text_batch(
    texts,
    output_dir="outputs",
    prefix="tajik_audio"
)
# Creates: outputs/tajik_audio_001.wav, outputs/tajik_audio_002.wav, etc.


# ============================================
# In Jupyter Notebook
# ============================================
from tajik_tts import synthesize_tajik_text
from IPython.display import Audio
import scipy.io.wavfile

# Generate audio
text = "Субҳ барвақт бедор шудам."
output_file = synthesize_tajik_text(text, "output.wav")

# Play in notebook
sampling_rate, audio_data = scipy.io.wavfile.read(output_file)
Audio(audio_data, rate=sampling_rate)


# ============================================
# Get Model Information
# ============================================
from tajik_tts import get_model_info

info = get_model_info()
print(info)
# Output: {'model_name': 'facebook/mms-tts-tgk', 'sampling_rate': 16000, ...}


# ============================================
# Processing from JSON Dataset
# ============================================
import json
from tajik_tts import synthesize_tajik_text_batch

# Load your dataset
with open("sample_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Generate audio for all sentences
all_texts = data.get("tojikon_sentences", []) + data.get("names_sentences", [])

output_files = synthesize_tajik_text_batch(
    all_texts,
    output_dir="generated_audio",
    prefix="tajik"
)
