import streamlit as st
from peft import AutoPeftModelForCausalLM
from transformers import GenerationConfig, AutoTokenizer
import torch

def app():
    max_length = 150
    input_text = st.text_input("Enter News for Summarization (Max {} characters):".format(max_length), height=200)
    if len(input_text.split(" ")) <= max_length:
        if input_text:
            with st.spinner("Summarizing news..."):
                tokenizer = AutoTokenizer.from_pretrained("/content/mistral-finetuned-news_summarization")
                inputs = tokenizer(f"""
                ###Human: Summarize this following news: {input_text}
                ###Assistant: """, return_tensors="pt").to("cuda")

                model = AutoPeftModelForCausalLM.from_pretrained(
                    "/content/mistral-finetuned-news_summarization",
                    low_cpu_mem_usage=True,
                    return_dict=True,
                    torch_dtype=torch.float16,
                    device_map="cuda"
                )

                generation_config = GenerationConfig(
                    do_sample=True,
                    top_k=1,
                    temperature=0.1,
                    max_new_tokens=25,
                    pad_token_id=tokenizer.eos_token_id
                )
                outputs = model.generate(**inputs, generation_config=generation_config)
                responce = tokenizer.decode(outputs[0], skip_special_tokens=True)

            st.write("**Summary**")
            st.success(responce)
        else:
            st.info("Please enter news text for summarization.")
    else:
        st.error("Input text exceeds maximum length ({} characters). Please try again.".format(max_length))