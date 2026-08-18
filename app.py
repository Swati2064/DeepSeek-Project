from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
import streamlit as st

st.title("Swati Jadhav Bot using DeepSeek-R1")

template = """
Question: {question}

Answer: Let's think step by step.
"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="deepseek-r1:1.5b")

chain = prompt | model

question = st.text_input("Enter your question")

if question:
    try:
        response = chain.invoke({"question": question})
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")