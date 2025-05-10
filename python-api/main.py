from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List, Any
import os
from pathlib import Path
import json
import re

# Initialize FastAPI app
app = FastAPI(
    title="Government Language Translator API",
    description="API for translating English text to Hindi with a formal tone suitable for government documents",
    version="1.0.0"
)

# Model paths and configurations
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)
TRANSLATION_MAP_PATH = MODEL_DIR / "translation_map.json"
PHRASE_MAP_PATH = MODEL_DIR / "phrase_map.json"
TRAINING_DATA_PATH = MODEL_DIR / "training_data.json"

# Global variables for the translation model
word_translation_map = {}
phrase_translation_map = {}
is_model_loaded = False

def load_model():
    """Load translation maps if they exist"""
    global word_translation_map, phrase_translation_map, is_model_loaded
    
    if TRANSLATION_MAP_PATH.exists():
        with open(TRANSLATION_MAP_PATH, 'r', encoding='utf-8') as f:
            word_translation_map = json.load(f)
    
    if PHRASE_MAP_PATH.exists():
        with open(PHRASE_MAP_PATH, 'r', encoding='utf-8') as f:
            phrase_translation_map = json.load(f)
    
    is_model_loaded = True
    print(f"Model loaded: {len(word_translation_map)} word mappings and {len(phrase_translation_map)} phrase mappings")

# Load model at startup
@app.on_event("startup")
async def startup_event():
    load_model()

class TranslationRequest(BaseModel):
    text: str
    preserve_formatting: Optional[bool] = True

class TranslationResponse(BaseModel):
    translation: str
    source_text: str
    success: bool
    error: Optional[str] = None

class TrainingDataRequest(BaseModel):
    training_pairs: List[Dict[str, str]]  # List of {english: "...", hindi: "..."}

class TrainingDataResponse(BaseModel):
    success: bool
    message: str
    pairs_count: int

def simple_tokenize(text):
    """Simple tokenization function that splits text into words"""
    # Remove punctuation and split by whitespace
    return re.sub(r'[^\w\s]', '', text.lower()).split()

def preprocess_text(text):
    """Clean and tokenize text"""
    # Preserve paragraph breaks for formatting
    paragraphs = text.split('\n\n')
    processed_paragraphs = []
    
    for paragraph in paragraphs:
        # Simple sentence splitting by periods, question marks, and exclamation marks
        sentences = re.split(r'[.!?]+', paragraph)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        processed_paragraphs.append(sentences)
    
    return processed_paragraphs

def extract_phrases(text, max_phrase_length=4):
    """Extract potential phrases from text for phrase-based translation"""
    tokens = simple_tokenize(text)
    phrases = []
    
    # Extract phrases of different lengths
    for phrase_len in range(2, min(max_phrase_length + 1, len(tokens) + 1)):
        for i in range(len(tokens) - phrase_len + 1):
            phrase = ' '.join(tokens[i:i+phrase_len])
            phrases.append(phrase)
    
    return phrases

def translate_text_with_model(text):
    """Translate English text to Hindi using the trained statistical model"""
    try:
        if not is_model_loaded:
            load_model()
        
        # Process text by paragraphs to preserve formatting
        paragraphs = preprocess_text(text)
        translated_paragraphs = []
        
        for paragraph in paragraphs:
            translated_sentences = []
            
            for sentence in paragraph:
                if not sentence:
                    continue
                    
                # Check if the entire sentence is in the phrase map
                if sentence.lower() in phrase_translation_map:
                    translated_sentences.append(phrase_translation_map[sentence.lower()])
                    continue
                
                # Extract phrases and check for matches
                phrases = extract_phrases(sentence)
                
                # Sort phrases by length in descending order for better matching
                phrases.sort(key=len, reverse=True)
                
                # First try to translate any phrases we can find
                sentence_lower = sentence.lower()
                translated_sentence = sentence
                
                for phrase in phrases:
                    if phrase in phrase_translation_map:
                        # Simple replacement strategy
                        translated_sentence = translated_sentence.lower().replace(phrase, phrase_translation_map[phrase])
                
                # Then translate individual words
                tokens = simple_tokenize(translated_sentence)
                for i, token in enumerate(tokens):
                    if token.lower() in word_translation_map:
                        tokens[i] = word_translation_map[token.lower()]
                
                # Combine the translated tokens into a sentence
                word_translated_sentence = " ".join(tokens)
                translated_sentences.append(word_translated_sentence)
            
            # Combine translated sentences into a paragraph
            translated_paragraphs.append(". ".join(translated_sentences))
        
        # Return the translated text with paragraph formatting preserved
        return "\n\n".join(translated_paragraphs)
    
    except Exception as e:
        print(f"Translation error: {str(e)}")
        raise e

@app.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")

        # Process the text based on formatting preference
        input_text = request.text.strip()
        
        translation = translate_text_with_model(input_text)

        if not translation:
            raise HTTPException(
                status_code=500,
                detail="Translation model returned empty response"
            )

        return TranslationResponse(
            translation=translation,
            source_text=request.text,
            success=True
        )

    except Exception as e:
        error_message = str(e)
        
        return TranslationResponse(
            translation="",
            source_text=request.text,
            success=False,
            error=error_message
        )

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "model_status": "loaded" if is_model_loaded else "not_loaded",
        "word_map_size": len(word_translation_map),
        "phrase_map_size": len(phrase_translation_map)
    }

@app.post("/train/add-data", response_model=TrainingDataResponse)
async def add_training_data(request: TrainingDataRequest):
    try:
        # Load existing training data or create new
        training_data = []
        if TRAINING_DATA_PATH.exists():
            with open(TRAINING_DATA_PATH, 'r', encoding='utf-8') as f:
                training_data = json.load(f)
        
        # Add new pairs
        for pair in request.training_pairs:
            if "english" in pair and "hindi" in pair:
                training_data.append({
                    "english": pair["english"].strip(),
                    "hindi": pair["hindi"].strip()
                })
        
        # Save updated training data
        with open(TRAINING_DATA_PATH, 'w', encoding='utf-8') as f:
            json.dump(training_data, f, ensure_ascii=False, indent=2)
        
        # Immediately update the translation maps
        update_translation_maps(training_data)
        
        return TrainingDataResponse(
            success=True,
            message="Training data added and model updated",
            pairs_count=len(training_data)
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add training data: {str(e)}")

def update_translation_maps(training_data):
    """Update word and phrase translation maps based on training data"""
    global word_translation_map, phrase_translation_map
    
    # Create maps for words and phrases
    new_word_map = {}
    new_phrase_map = {}
    
    for item in training_data:
        english_text = item["english"].lower()
        hindi_text = item["hindi"]
        
        # Add the entire sentence/paragraph as a phrase for exact matches
        new_phrase_map[english_text] = hindi_text
        
        # Split into sentences for better granularity
        eng_sentences = re.split(r'[.!?]+', english_text)
        eng_sentences = [s.strip() for s in eng_sentences if s.strip()]
        
        hindi_sentences = re.split(r'[।.!?]+', hindi_text)
        hindi_sentences = [s.strip() for s in hindi_sentences if s.strip()]
        
        # If we have the same number of sentences, map them directly
        if len(eng_sentences) == len(hindi_sentences):
            for eng_sent, hindi_sent in zip(eng_sentences, hindi_sentences):
                new_phrase_map[eng_sent] = hindi_sent
        
        # Extract individual words
        eng_words = simple_tokenize(english_text)
        hindi_words = hindi_text.split()
        
        # Simple word-to-word mapping (this is very basic and needs improvement)
        if len(eng_words) <= 10 and len(hindi_words) <= 10 and abs(len(eng_words) - len(hindi_words)) <= 3:
            for eng_word in eng_words:
                if eng_word.lower() not in new_word_map:
                    # For simplicity, just map to first Hindi word we haven't mapped yet
                    for hindi_word in hindi_words:
                        if hindi_word not in new_word_map.values():
                            new_word_map[eng_word.lower()] = hindi_word
                            break
    
    # Update the global maps
    word_translation_map.update(new_word_map)
    phrase_translation_map.update(new_phrase_map)
    
    # Save the updated maps
    with open(TRANSLATION_MAP_PATH, 'w', encoding='utf-8') as f:
        json.dump(word_translation_map, f, ensure_ascii=False, indent=2)
    
    with open(PHRASE_MAP_PATH, 'w', encoding='utf-8') as f:
        json.dump(phrase_translation_map, f, ensure_ascii=False, indent=2)
    
    print(f"Translation maps updated: {len(word_translation_map)} words, {len(phrase_translation_map)} phrases")

@app.post("/train/rebuild-model")
async def rebuild_model():
    """Rebuild the translation maps from scratch using all training data"""
    try:
        # Check if we have training data
        if not TRAINING_DATA_PATH.exists():
            raise HTTPException(status_code=400, detail="No training data available. Add data first.")
        
        with open(TRAINING_DATA_PATH, 'r', encoding='utf-8') as f:
            training_data = json.load(f)
        
        # Clear existing maps and rebuild
        global word_translation_map, phrase_translation_map
        word_translation_map = {}
        phrase_translation_map = {}
        
        update_translation_maps(training_data)
        
        return {
            "success": True,
            "message": f"Model rebuilt successfully with {len(training_data)} pairs",
            "word_map_size": len(word_translation_map),
            "phrase_map_size": len(phrase_translation_map)
        }
    
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=f"Error rebuilding model: {str(e)}")

@app.get("/train/data-status")
async def get_training_data_status():
    if not TRAINING_DATA_PATH.exists():
        return {"exists": False, "count": 0}
    
    try:
        with open(TRAINING_DATA_PATH, 'r', encoding='utf-8') as f:
            training_data = json.load(f)
        
        return {
            "exists": True,
            "count": len(training_data),
            "sample": training_data[:3] if training_data else [],
            "word_map_size": len(word_translation_map),
            "phrase_map_size": len(phrase_translation_map)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading training data: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
