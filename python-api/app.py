import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Title and description
st.title("Government Document Translator")
st.subheader("English to Hindi Translation for Government Documents")

# Introduction
st.markdown("""
This application translates English text to Hindi with a formal tone suitable for government documents.
It preserves technical terms, proper nouns, and maintains formatting as needed.
""")

# Input area
input_text = st.text_area("Enter English text to translate:", height=200)

# Options
col1, col2 = st.columns(2)
with col1:
    preserve_formatting = st.checkbox("Preserve original formatting", value=True)
with col2:
    api_url = st.text_input("API URL", value="http://localhost:8000/translate")

# Translation function
def translate_text(text, preserve_format=True, url="http://localhost:8000/translate"):
    if not text.strip():
        return None, "Please enter some text to translate."
    
    try:
        response = requests.post(
            url,
            json={"text": text, "preserve_formatting": preserve_format}
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                return data.get("translation"), None
            else:
                return None, f"Translation error: {data.get('error', 'Unknown error')}"
        else:
            return None, f"API returned status code: {response.status_code}"
    
    except requests.exceptions.ConnectionError:
        return None, "Connection error: Could not connect to the API. Make sure the API server is running."
    except Exception as e:
        return None, f"Error: {str(e)}"

# Display API status
if st.button("Check API Status"):
    try:
        response = requests.get(api_url.replace("/translate", "/health"))
        if response.status_code == 200:
            status_data = response.json()
            if status_data.get("status") == "healthy":
                if status_data.get("api_key_configured"):
                    st.success("✅ API is up and running with API key configured")
                else:
                    st.warning("⚠️ API is running but the API key is not configured")
        else:
            st.error(f"❌ API returned status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the API. Make sure the API server is running.")
    except Exception as e:
        st.error(f"❌ Error checking API status: {str(e)}")

# Translation button
if st.button("Translate"):
    with st.spinner('Translating...'):
        translation, error = translate_text(input_text, preserve_formatting, api_url)
        
        if error:
            st.error(error)
        elif translation:
            st.success("Translation completed!")
            
            # Display the translation in a container with styling
            st.subheader("Hindi Translation:")
            # Fix: Using raw strings to avoid backslash issue in f-string
            translated_text = translation.replace('\n', '<br>')
            st.markdown(
                f"""
                <div style="background-color: #f0f0f0; padding: 20px; border-radius: 10px; border-left: 5px solid #4CAF50; color: #333333; font-weight: 500; font-size: 16px;">
                    {translated_text}
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Add a copy button (indirectly, since direct clipboard interaction is limited)
            st.text_area("Copy translation from here:", value=translation, height=200)

# Instructions for running the API
with st.expander("How to run the translation API"):
    st.markdown("""
    1. Make sure you have set the `GEMINI_API_KEY` in your `.env` file
    2. Open a terminal and run the FastAPI server:
       ```
       cd path/to/python-api
       uvicorn main:app --reload
       ```
    3. The API should be running at http://localhost:8000
    4. You can now use this Streamlit interface to translate text
    """)

# Footer
st.markdown("---")
st.markdown("Powered by Google Gemini AI and FastAPI")