import streamlit as st
st.set_page_config(page_title="LLM Data Visualizer", layout="wide")  # FIRST command

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from llama_cpp import Llama

# Load local GGUF model (only once)
@st.cache_resource
def load_llm():
    return Llama(
        model_path="/Users/yashwanththota/Documents/RAG/Llama-3.2-3B-Instruct-Q6_K_L.gguf",
        n_ctx=4096,
        n_threads=6,
        n_gpu_layers=5,
        chat_format="chatml"
    )

llm = load_llm()

# UI
st.title("Data Visualization Assistant")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
user_query = st.text_input("What do you want to visualize? (e.g., 'scatter plot of Age vs Salary')")

if uploaded_file and user_query:
    try:
        df = pd.read_csv(uploaded_file)
        st.subheader("📄 Uploaded Data Preview")
        st.dataframe(df.head())

        sample_csv = df.head().to_csv(index=False)
        prompt = f"""
You are a Python data visualization expert.
The user uploaded a dataset and wants to visualize it.

Here is a sample of the CSV:
{sample_csv}

User's request:
{user_query}

Generate Python code using matplotlib or seaborn to show the requested chart.
Assume the DataFrame is already loaded as `df`.
Only return executable Python code. No markdown, no explanation, no text. End with plt.show()
"""

        #  Get output from the local LLM
        output = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )
        raw_code = output["choices"][0]["message"]["content"]

        # 🧼 Clean up the code
        cleaned_code = re.sub(r"```(python)?", "", raw_code).strip("` \n")

        st.subheader("Generated Python Code")
        st.code(cleaned_code, language="python")

        st.subheader("Visualization Output")
        plt.figure()
        exec(cleaned_code, {"df": df, "plt": plt, "sns": sns})
        st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f"⚠️ Failed to visualize: {e}")
