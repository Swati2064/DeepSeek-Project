import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Streamlit page configuration
st.set_page_config(
    page_title="NareshIT Bot using DeepSeek-R1",
    page_icon="🤖"
)

st.title("🤖 NareshIT Bot using DeepSeek-R1")

# Prompt Template
template = """
Question: {question}

Answer: Let's think step by step.
"""

prompt = ChatPromptTemplate.from_template(template)

# Load Ollama model
llm = OllamaLLM(
    model="deepseek-r1:1.5b"      # Change if your model name is different
)

# Create chain
chain = prompt | llm

# User Input
question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = chain.invoke({"question": question})
                st.success("Answer")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")