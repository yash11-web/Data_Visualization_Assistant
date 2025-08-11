# LLM Data Visualizer

##  About
It is an intelligent data visualization tool that allows users to generate insightful plots using natural language commands. Built with Streamlit, it uses a locally hosted LLaMA GGUF model (via llama-cpp) to understand user queries and convert them into Python code using Matplotlib, Seaborn, or Plotly for interactive plots. This tool bridges the gap between non-technical users and complex data visualizations without writing code.


##  Features
-  **CSV Upload** – Import your dataset directly.
-  **LLM-Powered Visualization** – Ask in plain English (e.g., "Show me a bar chart of sales by region").
-  **Multiple Chart Types** – Supports bar charts, line charts, scatter plots, histograms, etc.
-  **Clear Visual Hierarchy** – Well-structured dashboard with clean layout and labeled charts.
-  **Strategic Use of Color** – Improves readability and user experience.
-  **Runs Locally** – No internet or API required; uses a local LLaMA `.gguf` model.

##  How It Works
1. **Upload** your CSV file through the Streamlit interface.
2. **Enter a Visualization Request** in natural language.
3. The **local LLaMA model** processes your request and generates Python code using Matplotlib/Seaborn.
4. The code runs in the background, and the **resulting chart** is displayed in the dashboard.
5. All processing happens **locally** for speed, privacy, and offline use.


### Requirements
- Python 3.10+
- Streamlit
- pandas
- matplotlib
- seaborn
- llama-cpp-python
