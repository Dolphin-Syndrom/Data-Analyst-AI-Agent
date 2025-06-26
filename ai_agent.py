
import os
import pandas as pd
import streamlit as st
from pandasai import SmartDataframe
from pandasai.llm.local_llm import LocalLLM

# You can modify these to suit your needs
OLLAMA_API_BASE = "http://localhost:11434/v1"  # Change if Ollama is running on a different host/port
MODEL_NAME = "llama3"  # Change to any model available in your Ollama installation


st.set_page_config(
    page_title="Data Analyst Agent",
    layout="wide"
)

# Initialize the LLM
@st.cache_resource
def load_llm():
    return LocalLLM(
        api_base=OLLAMA_API_BASE,
        model=MODEL_NAME
    )

def main():
    """Main application function."""
    st.title("Data Analyst Agent")
    
    st.markdown("""
    Upload a CSV file and ask questions about your data in natural language.
    The AI will analyze your data and provide insights.
    """)
    
    with st.sidebar:
        st.header("About")
        st.info("""
        This application uses PandasAI with Ollama to analyze your data.
        Make sure Ollama is running with the specified model.
        """)
        
        # Model information
        st.header("Model Configuration")
        st.write(f"Using model: **{MODEL_NAME}**")
        st.write(f"Ollama API: **{OLLAMA_API_BASE}**")
        
    # File upload section
    uploaded_file = st.file_uploader("Upload CSV file", type="csv", help="Select a CSV file to analyze")

    if uploaded_file is not None:
        try:
            # Load and display data
            data = pd.read_csv(uploaded_file)
            
            st.subheader("Data Preview")
            st.dataframe(data.head(5), use_container_width=True)
            
            # Display basic statistics
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Rows:** {data.shape[0]}")
            with col2:
                st.write(f"**Columns:** {data.shape[1]}")
            
            # Initialize the SmartDataframe with the local LLM
            model = load_llm()
            df = SmartDataframe(data, config={"llm": model})
            
            # Query input
            st.subheader("Ask Questions About Your Data")
            query = st.text_area(
                "Enter your question:",
                height=100,
                placeholder="Example: What is the average value? Show me a summary of the data. Which category has the highest count?"
            )
            
            # Process query
            if st.button("Analyze", type="primary"):
                if query:
                    with st.spinner("Processing your query... (this may take a moment)"):
                        try:
                            result = df.chat(query)
                            st.subheader("Analysis Result")
                            st.write(result)
                        except Exception as e:
                            st.error(f"Error processing query: {str(e)}")
                else:
                    st.warning("Please enter a question to analyze your data.")
        
        except Exception as e:
            st.error(f"Error reading the file: {str(e)}")

if __name__ == "__main__":
    main()