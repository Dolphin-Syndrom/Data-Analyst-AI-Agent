# Data-Analyst-AI-Agent
Data Analysis with PandasAI using local LLMs through Ollama

## Features

- 📊 Upload and analyze CSV files
- 💬 Ask questions about your data in plain English
- 🤖 Powered by local language models via Ollama
- 📈 Instant data insights without coding

## Requirements

- Python 3.11
- Ollama installed and running locally

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dolphin-Syndrom/Data-Analyst-AI-Agent
   cd Data-Analyst-AI-Agent
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Setting up Ollama

1. Install Ollama following the instructions at [ollama.ai](https://ollama.ai).

2. Pull the required model:
   ```bash
   ollama pull llama3  # Default model used in this application
   ```

3. Ensure Ollama is running:
   ```bash
   ollama serve
   ```
   This will start the Ollama server on http://localhost:11434.

## Configuration

You can customize the application by modifying the following variables in the ai_agent.py file:

```python
# You can modify these to suit your needs
OLLAMA_API_BASE = "http://localhost:11434/v1"  # Change if Ollama is running on a different host/port
MODEL_NAME = "llama3"  # Change to any model available in your Ollama installation
```

- `OLLAMA_API_BASE`: Change if your Ollama instance is running on a different host or port
- `MODEL_NAME`: Change to use a different model (must be available in your Ollama installation)

## Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run ai_agent.py
   ```

2. Open your browser and navigate to http://localhost:8501

### Using Different Models

The application defaults to using "llama3", but you can use any model available in your Ollama installation:

1. Pull a different model:
   ```bash
   ollama pull mistral
   ```

2. Update the `MODEL_NAME` variable in ai_agent.py.

