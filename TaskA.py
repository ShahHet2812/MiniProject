import streamlit as st
from transformers import pipeline
code_explainer = pipeline("text2text-generation", model="Salesforce/codegen-350M-mono")
st.set_page_config(page_title="AI-Powered Code Explainer", layout="wide")
def explain_code(code):
    response = code_explainer(f"Explain this code: {code}")
    return response[0]['generated_text']
st.title("AI-Powered Code Explainer")
st.write("Enter your code in any programming language, and get a simple explanation.")
user_code = st.text_area("Paste your code here:")
if st.button("Explain Code"):
    if user_code.strip():
        explanation = explain_code(user_code)
        st.subheader("Explanation:")
        st.write(explanation)
    else:
        st.warning("Please enter some code to analyze.")