"""
Tajik Text-to-Speech Web Application

A Streamlit web app for generating Tajik speech from text using Facebook MMS-TTS model.
"""

import streamlit as st
import os
import tempfile
from pathlib import Path
from datetime import datetime
import shutil
from tajik_tts import synthesize_tajik_text, get_model_info

# Initialize session state for audio history
if 'audio_history' not in st.session_state:
    st.session_state.audio_history = []

# Page configuration
st.set_page_config(
    page_title="Tajik Text-to-Speech",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f0f2f6;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎙️ Tajik Text-to-Speech Generator</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Audio History Section
    st.markdown("---")
    st.subheader("📚 Audio History")
    
    if len(st.session_state.audio_history) > 0:
        st.caption(f"Saved: {len(st.session_state.audio_history)}/5")
        
        # Display history (newest first)
        for idx, audio_item in enumerate(reversed(st.session_state.audio_history)):
            with st.expander(f"🎵 {audio_item['timestamp']}", expanded=False):
                st.caption(f"Text: {audio_item['text'][:50]}...")
                st.caption(f"Chars: {audio_item['char_count']} | Seed: {audio_item.get('seed', 'Random')}")
                
                # Play audio
                if os.path.exists(audio_item['file_path']):
                    audio_bytes = open(audio_item['file_path'], "rb").read()
                    st.audio(audio_bytes, format="audio/wav")
                    
                    # Download button
                    st.download_button(
                        label="📥 Download",
                        data=audio_bytes,
                        file_name=audio_item['file_name'],
                        mime="audio/wav",
                        key=f"download_{idx}",
                        use_container_width=True
                    )
                else:
                    st.warning("⚠️ File not found")
        
        # Clear history button
        if st.button("🗑️ Clear History", use_container_width=True):
            # Delete old files
            for item in st.session_state.audio_history:
                if os.path.exists(item['file_path']):
                    try:
                        os.remove(item['file_path'])
                    except:
                        pass
            st.session_state.audio_history = []
            st.rerun()
    else:
        st.info("No audio history yet. Generate some audio to see it here!")
    
    st.markdown("---")
    
    # Model information
    with st.expander("📊 Model Information", expanded=False):
        try:
            info = get_model_info()
            if "error" not in info:
                st.write(f"**Model:** {info.get('model_name', 'N/A')}")
                st.write(f"**Sampling Rate:** {info.get('sampling_rate', 'N/A')} Hz")
                st.write(f"**Language:** {info.get('language', 'N/A')}")
                st.write(f"**Type:** {info.get('model_type', 'N/A')}")
                st.markdown(f"[View on Hugging Face]({info.get('source', '#')})")
        except Exception as e:
            st.error(f"Could not load model info: {e}")
    
    st.markdown("---")
    
    # Generation parameters
    st.subheader("🎛️ Generation Parameters")
    
    # Voice style info
    with st.expander("ℹ️ About Voice Options", expanded=False):
        st.info("""
        **Note:** The MMS-TTS model is a single-voice model. It doesn't support 
        different voice styles (narrator, boy voice, etc.). Each MMS-TTS model 
        is trained with one voice per language.
        
        **Available options:**
        - **Seed variation**: Creates natural variation in the same voice
        - **Speed adjustment**: Post-processing option (coming soon)
        """)
    
    # Seed for reproducibility/variation
    st.markdown("#### 🎲 Seed Parameter")
    
    with st.expander("❓ What does the seed do?", expanded=True):
        st.markdown("""
        **The seed controls randomness in voice generation:**
        
        - **Same seed + same text = identical audio** (reproducible)
        - **Different seed + same text = natural variation** (same voice, different tone/rhythm)
        
        **How to use it:**
        - **For consistent results**: Use a fixed seed (e.g., 42) - same text always sounds the same
        - **For variation**: Use different seeds (e.g., 42, 123, 999) - same text sounds slightly different each time
        - **For random results**: Don't use a seed - each generation will be unique
        
        **What changes with different seeds:**
        - ✅ Speaking rhythm and pacing
        - ✅ Slight tone variations
        - ✅ Natural prosody differences
        - ❌ Voice identity (always the same voice)
        - ❌ Language or pronunciation
        
        **Example:** Generate "Салом" with seed 42, then try 123 - you'll hear the same voice but with different rhythm!
        """)
    
    use_seed = st.checkbox(
        "Use fixed seed (for reproducible results)", 
        value=False,
        help="Enable to get the same audio output every time for the same text"
    )
    
    seed_value = None
    if use_seed:
        # Initialize session state for seed if not exists
        if 'seed_value' not in st.session_state:
            st.session_state.seed_value = 42
        
        seed_value = st.number_input(
            "Seed value",
            min_value=0,
            max_value=999999,
            value=st.session_state.seed_value,
            help="Enter any number (0-999999). Same seed = same audio. Different seed = natural variation.",
            key="seed_input"
        )
        
        # Update session state
        st.session_state.seed_value = seed_value
        
        # Show quick seed buttons
        st.caption("Quick seed examples (click to try):")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button("🎯 42", use_container_width=True, key="seed_42"):
                st.session_state.seed_value = 42
                st.rerun()
        with col_b:
            if st.button("🎲 123", use_container_width=True, key="seed_123"):
                st.session_state.seed_value = 123
                st.rerun()
        with col_c:
            if st.button("🎪 999", use_container_width=True, key="seed_999"):
                st.session_state.seed_value = 999
                st.rerun()
        
        st.caption("💡 **Tip**: Try generating the same text with different seeds (42, 123, 999) to hear natural variations!")
    else:
        st.info("🎲 **Random mode**: Each generation will be unique (no seed used)")
        st.caption("💡 Enable 'Use fixed seed' above to get reproducible results or try different seeds for variation")
    
    # Text processing options
    st.markdown("---")
    st.subheader("📝 Text Processing")
    
    split_long_text = st.checkbox(
        "Auto-split long text",
        value=True,
        help="Split text into sentences for better quality on long texts"
    )
    
    max_chars_per_chunk = st.slider(
        "Max characters per chunk",
        min_value=100,
        max_value=1000,
        value=500,
        step=50,
        help="Maximum characters per audio chunk when splitting",
        disabled=not split_long_text
    )
    
    st.markdown("---")
    st.subheader("🎚️ Audio Speed Control")
    
    with st.expander("❓ How does speed adjustment work?", expanded=False):
        st.markdown("""
        **Speed Control:**
        - The MMS-TTS model doesn't have built-in speed parameters
        - We use post-processing to change playback speed
        - **0.5x - 0.9x**: Slower speech (good for learning, clear pronunciation)
        - **1.0x**: Normal speed (default)
        - **1.1x - 2.0x**: Faster speech (good for quick listening)
        
        **Note:** Speed adjustment preserves the voice quality but changes the pace.
        This is applied after audio generation, so it works with any generated audio.
        """)
    
    # Speed adjustment (post-processing)
    speed_factor = st.slider(
        "Speech Speed",
        min_value=0.5,
        max_value=2.0,
        value=1.0,
        step=0.1,
        help="Adjust speech speed: 1.0 = normal, <1.0 = slower, >1.0 = faster"
    )
    
    # Show speed indicator
    if speed_factor < 1.0:
        st.info(f"🐢 **Slower**: {speed_factor}x speed ({int((1-speed_factor)*100)}% slower than normal)")
    elif speed_factor > 1.0:
        st.info(f"🐰 **Faster**: {speed_factor}x speed ({int((speed_factor-1)*100)}% faster than normal)")
    else:
        st.caption("🎵 Normal speed (1.0x)")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Enter Tajik Text")
    
    # Text input
    text_input = st.text_area(
        "Type or paste your Tajik text here:",
        height=300,
        placeholder="Салом, ман Ибни Сино ҳастам...",
        help="Enter Tajik text to convert to speech (recommended: up to 10,000 characters)",
        max_chars=50000  # Set a reasonable limit to prevent memory issues
    )
    
    # Character count with warning
    char_count = len(text_input)
    char_display = f"Characters: {char_count}"
    
    # Show warnings for very long text
    if char_count > 10000:
        st.warning(f"⚠️ Very long text ({char_count:,} chars). Processing may take a while and use significant memory.")
    elif char_count > 5000:
        st.info(f"ℹ️ Long text ({char_count:,} chars). Consider splitting into smaller chunks for better quality.")
    
    st.caption(char_display)
    
    # Generate button
    generate_button = st.button("🎵 Generate Audio", type="primary", use_container_width=True)

with col2:
    st.subheader("ℹ️ Instructions")
    st.markdown("""
    <div class="info-box">
    <b>How to use:</b>
    <ol>
        <li>Enter Tajik text in the text area</li>
        <li>Adjust settings in the sidebar (optional)</li>
        <li>Click "Generate Audio"</li>
        <li>Wait for processing (first time may take longer)</li>
        <li>Download the generated audio file</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <b>💡 Tips:</b>
    <ul>
        <li>Long texts are automatically split for better quality</li>
        <li>Use fixed seed for reproducible results</li>
        <li>Different seeds create natural variation in the same voice</li>
        <li>First generation loads the model (~5-10 seconds)</li>
        <li>Subsequent generations are faster</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <b>🎲 Understanding Seeds:</b>
    <ul>
        <li><b>Same seed</b> = Same text always sounds identical (good for consistency)</li>
        <li><b>Different seeds</b> = Same text sounds slightly different (good for variety)</li>
        <li><b>No seed</b> = Random variation each time (good for natural diversity)</li>
    </ul>
    <p><b>Example:</b> Try generating the same text with seeds 42, 123, and 999 to hear the variations!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <b>⚠️ Voice Styles:</b>
    <p>The MMS-TTS model uses a single voice. It doesn't support different 
    voice styles (narrator, boy voice, etc.). However, you can:</p>
    <ul>
        <li>Use different seeds for natural variation in rhythm and tone</li>
        <li>Adjust playback speed for different effects</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Processing and results
if generate_button:
    if not text_input.strip():
        st.error("⚠️ Please enter some text to generate audio!")
    else:
        with st.spinner("🔄 Generating audio... This may take a moment (especially on first use)..."):
            try:
                # Handle long text splitting
                if split_long_text and len(text_input) > max_chars_per_chunk:
                    # Split text into chunks
                    chunks = []
                    sentences = text_input.split('. ')
                    current_chunk = ""
                    
                    for sentence in sentences:
                        if len(current_chunk) + len(sentence) + 2 <= max_chars_per_chunk:
                            current_chunk += sentence + ". "
                        else:
                            if current_chunk:
                                chunks.append(current_chunk.strip())
                            current_chunk = sentence + ". "
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    
                    st.info(f"📄 Text split into {len(chunks)} chunks for better quality")
                    
                    # Generate audio for each chunk
                    audio_files = []
                    progress_bar = st.progress(0)
                    
                    for i, chunk in enumerate(chunks):
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                            chunk_file = tmp_file.name
                        
                        synthesize_tajik_text(
                            chunk,
                            chunk_file,
                            seed=seed_value if use_seed else None
                        )
                        audio_files.append(chunk_file)
                        progress_bar.progress((i + 1) / len(chunks))
                    
                    # Combine audio files
                    try:
                        from pydub import AudioSegment
                        combined = AudioSegment.empty()
                        for audio_file in audio_files:
                            combined += AudioSegment.from_wav(audio_file)
                        
                            # Save combined audio (use absolute path for Streamlit Cloud)
                            output_file = os.path.join(os.getcwd(), "tajik_audio_output.wav")
                        combined.export(output_file, format="wav")
                        
                        # Clean up temporary files
                        for audio_file in audio_files:
                            os.unlink(audio_file)
                        
                        st.success(f"✅ Audio generated successfully! ({len(chunks)} chunks combined)")
                        
                    except (ImportError, FileNotFoundError, Exception) as e:
                        # Fallback: Use scipy to combine WAV files
                        try:
                            import scipy.io.wavfile
                            import numpy as np
                            
                            st.info("📦 Using alternative method to combine audio chunks...")
                            
                            # Read all audio files
                            audio_data_list = []
                            sample_rate = None
                            
                            for audio_file in audio_files:
                                sr, data = scipy.io.wavfile.read(audio_file)
                                if sample_rate is None:
                                    sample_rate = sr
                                elif sr != sample_rate:
                                    # Resample if needed (simple approach: just use first sample rate)
                                    st.warning(f"⚠️ Sample rate mismatch: {sr} vs {sample_rate}. Using {sample_rate} Hz.")
                                
                                audio_data_list.append(data)
                            
                            # Concatenate all audio data
                            combined_audio = np.concatenate(audio_data_list)
                            
                            # Save combined audio (use absolute path for Streamlit Cloud)
                            output_file = os.path.join(os.getcwd(), "tajik_audio_output.wav")
                            scipy.io.wavfile.write(output_file, sample_rate, combined_audio)
                            
                            # Clean up temporary files
                            for audio_file in audio_files:
                                os.unlink(audio_file)
                            
                            st.success(f"✅ Audio generated successfully! ({len(chunks)} chunks combined)")
                            
                        except Exception as fallback_error:
                            # If both methods fail, save first chunk and warn
                            error_msg = str(e) if 'pydub' in str(e) or 'ffprobe' in str(e) else str(fallback_error)
                            st.error(f"❌ Could not combine audio chunks: {error_msg}")
                            st.warning("⚠️ Saving first chunk only. To combine chunks, install ffmpeg: `brew install ffmpeg`")
                            output_file = audio_files[0]
                            # Clean up other files
                            for audio_file in audio_files[1:]:
                                os.unlink(audio_file)
                    
                else:
                    # Single generation (use absolute path for Streamlit Cloud)
                    output_file = os.path.join(os.getcwd(), "tajik_audio_output.wav")
                    synthesize_tajik_text(
                        text_input,
                        output_file,
                        seed=seed_value if use_seed else None
                    )
                    st.success("✅ Audio generated successfully!")
                
                # Apply speed adjustment if needed
                if speed_factor != 1.0:
                    try:
                        from pydub import AudioSegment
                        import numpy as np
                        import scipy.io.wavfile
                        
                        # Load audio
                        audio_segment = AudioSegment.from_wav(output_file)
                        original_duration = len(audio_segment) / 1000.0  # seconds
                        
                        # Method 1: Try using pydub's speedup/slowdown (preserves pitch better)
                        if hasattr(audio_segment, '_spawn'):
                            # Change speed by adjusting frame rate (affects pitch slightly)
                            new_sample_rate = int(audio_segment.frame_rate * speed_factor)
                            audio_segment = audio_segment._spawn(
                                audio_segment.raw_data,
                                overrides={"frame_rate": new_sample_rate}
                            ).set_frame_rate(audio_segment.frame_rate)
                        else:
                            # Fallback: Use scipy for speed adjustment
                            sr, data = scipy.io.wavfile.read(output_file)
                            # Simple resampling approach
                            from scipy import signal
                            num_samples = int(len(data) / speed_factor)
                            indices = np.linspace(0, len(data) - 1, num_samples)
                            data = np.interp(indices, np.arange(len(data)), data).astype(data.dtype)
                            scipy.io.wavfile.write(output_file, sr, data)
                            audio_segment = AudioSegment.from_wav(output_file)
                        
                        audio_segment.export(output_file, format="wav")
                        new_duration = len(audio_segment) / 1000.0  # seconds
                        
                        st.success(f"⚡ Speed adjusted to **{speed_factor}x** (Duration: {original_duration:.1f}s → {new_duration:.1f}s)")
                    except Exception as e:
                        st.warning(f"⚠️ Could not adjust speed: {e}. Using original audio.")
                        import traceback
                        st.caption(f"Error details: {str(e)}")
                
                # Display audio player
                st.markdown("---")
                st.subheader("🎧 Generated Audio")
                
                # Audio player
                audio_bytes = open(output_file, "rb").read()
                st.audio(audio_bytes, format="audio/wav")
                
                # Download button
                st.download_button(
                    label="📥 Download Audio",
                    data=audio_bytes,
                    file_name=f"tajik_speech_{len(text_input)}chars.wav",
                    mime="audio/wav",
                    use_container_width=True
                )
                
                # File info
                file_size = os.path.getsize(output_file) / 1024  # KB
                seed_info = f" | Seed: {seed_value}" if use_seed and seed_value is not None else " | Seed: Random"
                st.caption(f"File size: {file_size:.2f} KB | Format: WAV{seed_info}")
                
                # Show seed hint
                if use_seed and seed_value is not None:
                    st.info(f"💡 **Seed used: {seed_value}** - Generate the same text again with this seed to get identical audio!")
                else:
                    st.info("💡 **Random seed** - Each generation will be unique. Enable 'Use fixed seed' in sidebar for reproducible results.")
                
                # Save to history
                save_to_history = st.checkbox("💾 Save to history", value=True, key="save_checkbox")
                
                if save_to_history:
                    # Create history directory if it doesn't exist
                    # Use /tmp for Streamlit Cloud compatibility
                    history_dir = os.path.join(os.getcwd(), "audio_history")
                    os.makedirs(history_dir, exist_ok=True)
                    
                    # Generate unique filename with timestamp
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    history_filename = f"tajik_audio_{timestamp}.wav"
                    history_filepath = os.path.join(history_dir, history_filename)
                    
                    # Copy file to history directory
                    shutil.copy2(output_file, history_filepath)
                    
                    # Create history item
                    history_item = {
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'text': text_input[:100] + "..." if len(text_input) > 100 else text_input,
                        'full_text': text_input,
                        'char_count': len(text_input),
                        'seed': seed_value if use_seed and seed_value is not None else 'Random',
                        'file_path': history_filepath,
                        'file_name': history_filename,
                        'file_size': file_size
                    }
                    
                    # Add to history (limit to 5)
                    st.session_state.audio_history.append(history_item)
                    
                    # Keep only last 5 items
                    if len(st.session_state.audio_history) > 5:
                        # Remove oldest item and delete its file
                        oldest = st.session_state.audio_history.pop(0)
                        if os.path.exists(oldest['file_path']):
                            try:
                                os.remove(oldest['file_path'])
                            except:
                                pass
                    
                    st.success(f"✅ Saved to history! ({len(st.session_state.audio_history)}/5 items)")
                
            except Exception as e:
                st.error(f"❌ Error generating audio: {str(e)}")
                st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>Powered by <a href="https://huggingface.co/facebook/mms-tts-tgk" target="_blank">Facebook MMS-TTS</a> | 
    <a href="https://huggingface.co/facebook/mms-tts-tgk" target="_blank">Model Card</a></p>
    <p>Model: facebook/mms-tts-tgk | License: CC-BY-NC 4.0</p>
</div>
""", unsafe_allow_html=True)

