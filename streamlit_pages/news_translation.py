import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translator(input_text, tokenizer, model):
    input_ids = tokenizer.encode(input_text, return_tensors="pt", padding=True)
    outputs = model.generate(input_ids)
    decoded_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded_text

def app():
    max_length = 100
    output_language = ["Hindi", "Marathi"]
    model_links = {"Hindi": "Helsinki-NLP/opus-mt-en-hi", "Marathi": "Helsinki-NLP/opus-mt-en-mr"}
    input_text = st.text_input("Enter News for Translation (Max {} characters):".format(max_length))
    selected_link = st.selectbox("Select Target Language for Translation:", options=output_language)
    link = model_links[selected_link]
    if len(input_text.split(" ")) <= max_length:
        if input_text:
            with st.spinner("Translating news..."):
                tokenizer = AutoTokenizer.from_pretrained(link)
                model = AutoModelForSeq2SeqLM.from_pretrained(link)
                result = translator(input_text, tokenizer, model)
                st.write("**Translation**")
                st.success(result)
        else:
            st.info("Please enter news text for translation.")
    else:
        st.error("Input text exceeds maximum length ({} characters). Please try again.".format(max_length))