import streamlit as st
from asr_model import ASRModel
from language_identification import LanguageIdentifier
from sentiment_analysis import SentimentAnalyzer

st.title("Multilingual Speech-to-Text and Sentiment Analysis")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
if uploaded_file:
    asr = ASRModel()
    transcription = asr.transcribe(uploaded_file)
    st.write("Transcription:", transcription)
    
    lang_identifier = LanguageIdentifier()
    language = lang_identifier.detect_language(transcription[0])
    st.write("Detected Language:", language)
    
    sentiment_analyzer = SentimentAnalyzer()
    sentiment = sentiment_analyzer.analyze_sentiment(transcription[0])
    st.write("Sentiment:", sentiment)
