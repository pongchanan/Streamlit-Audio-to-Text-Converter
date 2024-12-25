from pydub import AudioSegment, silence
import streamlit as st
import speech_recognition as sr

recog = sr.Recognizer()

final_result = ""

# Specify the exact path to the ffmpeg.exe file
AudioSegment.converter = "C:/Users/pongc/Downloads/ffmpeg-master-latest-win64-gpl/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe"

st.markdown("<h1 style='text-align: center;'>Audio to text converter</h1>", unsafe_allow_html=True)
st.markdown("---")

audio = st.file_uploader("Upload your audio file", type=["mp3", "wav"])
if audio:
    st.audio(audio)
    audio_segment = AudioSegment.from_file(audio)
    chunks = silence.split_on_silence(audio_segment, min_silence_len=500, silence_thresh=audio_segment.dBFS-20, keep_silence=100)
    
    for index, chunk in enumerate(chunks):
        chunk.export(str(index)+".wav", format="wav")
        with sr.AudioFile(str(index)+".wav") as source:
            recorded = recog.record(source)
            try:
                text = recog.recognize_google(recorded)
                final_result = final_result + " " + text
            except:
                final_result = final_result + " " +  "Unaudioable"
        
    st.text_area("text", value=final_result)