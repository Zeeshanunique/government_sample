from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Government Language Translator API",
    description="API for translating English text to Hindi with a formal tone suitable for government documents",
    version="1.0.0"
)

# Configure Gemini AI
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

class TranslationRequest(BaseModel):
    text: str
    preserve_formatting: Optional[bool] = True

class TranslationResponse(BaseModel):
    translation: str
    source_text: str
    success: bool
    error: Optional[str] = None

@app.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")

        # Create prompt with formatting preference
        prompt = (
            f"Translate the following English text to Hindi. "
            f"Maintain formal tone suitable for government documents, "
            f"preserving any technical terms or proper nouns"
        )
        if request.preserve_formatting:
            prompt += " and maintain the original text formatting"
        prompt += f': "{request.text.strip()}"'

        # Generate translation
        response = model.generate_content(prompt)
        translation = response.text.strip()

        if not translation:
            raise HTTPException(
                status_code=500,
                detail="Translation service returned empty response"
            )

        return TranslationResponse(
            translation=translation,
            source_text=request.text,
            success=True
        )

    except Exception as e:
        error_message = str(e)
        if "API key" in error_message.lower():
            error_message = "Invalid API key configuration"
        elif "quota" in error_message.lower():
            error_message = "API quota exceeded"
        
        return TranslationResponse(
            translation="",
            source_text=request.text,
            success=False,
            error=error_message
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy", "api_key_configured": bool(GEMINI_API_KEY)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
