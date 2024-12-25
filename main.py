from pydub import AudioSegment, silence

# Specify the exact path to the ffmpeg.exe file
AudioSegment.converter = "C:/Users/pongc/Downloads/ffmpeg-master-latest-win64-gpl/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe"

import streamlit as st

st.markdown("<h1 style='text-align: center;'>Audio to text converter</h1>", unsafe_allow_html=True)
st.markdown("---")

audio = st.file_uploader("Upload your audio file", type=["mp3", "wav"])
if audio:
    audio_segment = AudioSegment.from_file(audio)
    chunks = silence.split_on_silence(audio_segment, min_silence_len=100, silence_thresh=audio_segment.dBFS-20, keep_silence=100)
    
    for chunk in chunks:
        print(chunk)
