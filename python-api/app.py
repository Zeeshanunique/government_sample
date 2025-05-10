import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="Government Document Translator",
    page_icon="🔤",
    layout="centered"
)

# Title and branding
st.title("🇮🇳 Government Document Translator")
st.markdown("### English to Hindi Translation Service")

# Simple description
st.markdown("""
This tool instantly translates English government document text to formal Hindi.
Just type or paste your text below and get immediate translation.
""")

# Main translation interface
query = st.text_area("Enter English text:", height=150, 
                     placeholder="Type your English text here for translation...")

# API URL (with option to change if needed)
with st.expander("Advanced Settings"):
    api_url = st.text_input("API URL", value="http://localhost:8000")

# Translation function
def get_translation(text, url="http://localhost:8000"):
    if not text.strip():
        return None, "Please enter some text to translate."
    
    try:
        response = requests.post(
            f"{url}/translate",
            json={"text": text, "preserve_formatting": True}
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

# Translate button
if st.button("Translate", type="primary", use_container_width=True):
    if not query:
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner('Translating...'):
            translation, error = get_translation(query, api_url)
            
            if error:
                st.error(error)
            else:
                # Show results in a nice card
                st.success("Translation completed!")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("English")
                    st.info(query)
                
                with col2:
                    st.subheader("Hindi")
                    st.markdown(
                        f"""<div style="background-color: #f0f7fa; padding: 16px; border-radius: 10px; 
                        border-left: 5px solid #2e7d32; color: #333333; font-weight: 500; font-size: 16px;">
                        {translation}
                        </div>""", 
                        unsafe_allow_html=True
                    )
                
                # Copy option
                st.text_area("Copy translation:", value=translation, height=100)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 12px;'>Powered by Custom Machine Learning Translation Model</div>", 
    unsafe_allow_html=True
)