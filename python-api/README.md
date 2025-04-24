# Government Document Translation API

This directory contains a translation API service that converts English text to Hindi with a formal tone suitable for government documents.

## Features

- English to Hindi translation optimized for government documents
- Preserves technical terms and proper nouns
- Maintains original text formatting
- Simple REST API with FastAPI
- User-friendly web interface with Streamlit

## Setup and Installation

1. Ensure you have Python 3.8+ installed
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in this directory with your Gemini API key:
   ```
   GEMINI_API_KEY=your_key_here
   ```

## Running the API Service

Start the FastAPI server with:

```
uvicorn main:app --reload
```

The API will be available at:
- API Endpoint: http://localhost:8000/translate
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

## Running the Streamlit Interface

The Streamlit interface provides a user-friendly web UI for translation:

```
streamlit run app.py
```

The web interface will open automatically in your browser at http://localhost:8501

## API Usage Examples

### Using curl

```bash
curl -X POST "http://localhost:8000/translate" \
  -H "Content-Type: application/json" \
  -d '{"text": "Please submit your application form by the end of this month.", "preserve_formatting": true}'
```

### Using Python requests

```python
import requests

response = requests.post(
    "http://localhost:8000/translate",
    json={
        "text": "Please submit your application form by the end of this month.",
        "preserve_formatting": True
    }
)

result = response.json()
print(result["translation"])
```

## Notes

- The translation service requires an internet connection to access Google's Gemini API
- Set appropriate rate limits if using in production to avoid exceeding Gemini API quotas
