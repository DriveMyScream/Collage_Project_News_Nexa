import streamlit as st
from transformers import pipeline
from utils.utils import *

def app():
    @st.cache(allow_output_mutation=True)
    def load_classifier():
        return pipeline("text-classification", "DriveMyScream/bert-base-uncased-finetuned-fake_news_classification", framework="tf")

    classifier = load_classifier()
    max_length = 30 

    input_text = st.text_area("Enter News Text for Classification (Max 30 characters):")
    if len(input_text.split(" ")) <= max_length:
        if input_text:
            with st.spinner("Classifying news..."):
                clean_news = fake_news_first_remove_words_from_text(input_text)
                clean_news = clean_text(clean_news)
                clean_news = fake_news_sec_remove_words_from_text_second(clean_news)
                result = classifier(clean_news)[0]
            st.write("**Classification**")
            st.success("Prediction: " + result['label'])
            st.info("Confidence Score: {:.2f}".format(result['score']))
            st.markdown("---")
        else:
            st.info("Please enter news text for classification.")
    else:
        st.error("Input text exceeds maximum length ({} characters). Please try again.".format(max_length))