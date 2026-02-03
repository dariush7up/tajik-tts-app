"""
Facebook MMS-TTS for Tajik Language

This module provides functions to generate audio from Tajik text using 
Facebook's Massively Multilingual Speech (MMS) Text-to-Speech model.

Model: facebook/mms-tts-tgk (specifically trained for Tajik)
Source: https://huggingface.co/facebook/mms-tts-tgk

Requirements:
    - transformers (Hugging Face library)
    - torch (PyTorch)
    - scipy (for saving audio files)
    
Setup:
    1. Install: pip install transformers torch scipy
    2. No API key needed - runs locally!
"""

import os
from typing import Optional

try:
    from transformers import VitsModel, AutoTokenizer
    import torch
    import scipy.io.wavfile
except ImportError:
    VitsModel = None
    AutoTokenizer = None
    torch = None
    scipy = None


# Global variables to cache the model (load once, use many times)
_model = None
_tokenizer = None


def _load_model():
    """Load the MMS-TTS model and tokenizer (cached for performance)."""
    global _model, _tokenizer
    
    if _model is None or _tokenizer is None:
        if VitsModel is None:
            raise ImportError(
                "transformers library is not installed. "
                "Install it with: pip install transformers torch scipy"
            )
        
        print("📥 Loading MMS-TTS Tajik model (first time may take a moment)...")
        _model = VitsModel.from_pretrained("facebook/mms-tts-tgk")
        _tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-tgk")
        print("✅ Model loaded successfully!")
    
    return _model, _tokenizer


def synthesize_tajik_text(
    text: str,
    output_file: str = "output.wav",
    seed: Optional[int] = None
) -> str:
    """
    Generate audio from Tajik text using Facebook MMS-TTS model.
    
    Args:
        text: Tajik text to synthesize
        output_file: Output audio file path (will be saved as WAV)
        seed: Random seed for reproducibility (optional). If None, uses random seed.
    
    Returns:
        output_file: Path to the generated audio file
    
    Raises:
        ImportError: If required libraries are not installed
        Exception: If model loading or generation fails
    """
    # Check if required libraries are installed
    if VitsModel is None or torch is None or scipy is None:
        raise ImportError(
            "Required libraries are not installed. "
            "Install with: pip install transformers torch scipy"
        )
    
    try:
        # Load model (cached after first load)
        model, tokenizer = _load_model()
        
        # Tokenize input text
        inputs = tokenizer(text, return_tensors="pt")
        
        # Set random seed if provided (for reproducibility)
        if seed is not None:
            torch.manual_seed(seed)
        
        # Generate speech waveform
        with torch.no_grad():
            output = model(**inputs).waveform
        
        # Convert tensor to numpy array
        audio_data = output.squeeze().cpu().numpy()
        
        # Get sampling rate from model config
        sampling_rate = model.config.sampling_rate
        
        # Save as WAV file
        scipy.io.wavfile.write(output_file, rate=sampling_rate, data=audio_data)
        
        print(f"✅ Audio generated successfully: {output_file}")
        print(f"   Sampling rate: {sampling_rate} Hz")
        print(f"   Duration: ~{len(audio_data) / sampling_rate:.2f} seconds")
        
        return output_file
        
    except Exception as e:
        error_msg = f"❌ Error generating audio: {str(e)}"
        print(error_msg)
        print("\n💡 Troubleshooting:")
        print("1. Make sure you have internet connection (first time download)")
        print("2. Check that transformers, torch, and scipy are installed")
        print("3. Verify you have enough disk space (model is ~140MB)")
        print("4. If using GPU, make sure PyTorch is installed with CUDA support")
        raise Exception(error_msg) from e


def synthesize_tajik_text_batch(
    texts: list,
    output_dir: str = "outputs",
    prefix: str = "audio",
    seed: Optional[int] = None
) -> list:
    """
    Generate audio for multiple Tajik texts.
    
    Args:
        texts: List of Tajik texts to synthesize
        output_dir: Directory to save output files
        prefix: Prefix for output filenames (e.g., "audio_001.wav")
        seed: Random seed for reproducibility (optional)
    
    Returns:
        List of output file paths
    """
    import os
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    output_files = []
    for i, text in enumerate(texts, 1):
        output_file = os.path.join(output_dir, f"{prefix}_{i:03d}.wav")
        output_files.append(synthesize_tajik_text(text, output_file, seed=seed))
    
    print(f"\n✅ Generated {len(output_files)} audio files in {output_dir}/")
    return output_files


def get_model_info():
    """
    Get information about the loaded model.
    
    Returns:
        Dictionary with model information
    """
    try:
        model, tokenizer = _load_model()
        return {
            "model_name": "facebook/mms-tts-tgk",
            "sampling_rate": model.config.sampling_rate,
            "model_type": "VITS (Variational Inference with adversarial learning)",
            "language": "Tajik (tgk)",
            "source": "https://huggingface.co/facebook/mms-tts-tgk"
        }
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    # Test the function
    test_text = "Салом, ман Ибни Сино ҳастам, ҳарчанд бисёриҳо маро ҳамчун Ависенна мешиносанд. Ман падари тибби муосир ҳастам. Кори ман дар тиб асосан дар бораи пешгирии бемориҳо буд, на табобат, ки ин дар ҷаҳони имрӯза муҳим аст. Ман маслиҳатҳои зиёдеро дар бораи истифодаи гиёҳдармонӣ ва нуқтаҳои фаъоли биологӣ барои бемориҳои гуногун боқӣ гузоштам"
    try:
        output = synthesize_tajik_text(test_text, "test_output.wav")
        print(f"\n🎵 Test audio saved to: {output}")
        
        # Display model info
        print("\n📊 Model Information:")
        info = get_model_info()
        for key, value in info.items():
            print(f"   {key}: {value}")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
