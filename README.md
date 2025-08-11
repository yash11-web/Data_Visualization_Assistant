# LLM Data Visualizer

##  About
LLM Data Visualizer is a **Streamlit-based dashboard** that lets users upload CSV files and generate custom data visualizations using **natural language prompts**. It uses a **local LLaMA GGUF model** to understand requests and generate Python plotting code, making it possible to create charts without manual coding.

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
