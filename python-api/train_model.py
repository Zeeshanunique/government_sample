import requests
import pandas as pd
import json
import time

# Configuration
API_URL = "http://localhost:8000"
TRAINING_DATA_FILE = "govt_training_data.csv"

def load_csv_data(file_path):
    """Load training data from CSV file"""
    try:
        df = pd.read_csv(file_path)
        if 'english' not in df.columns or 'hindi' not in df.columns:
            print(f"Error: CSV must contain 'english' and 'hindi' columns")
            return []
        
        # Convert to list of dictionaries
        training_pairs = []
        for _, row in df.iterrows():
            if isinstance(row['english'], str) and isinstance(row['hindi'], str):
                if row['english'].strip() and row['hindi'].strip():
                    training_pairs.append({
                        "english": row['english'].strip(),
                        "hindi": row['hindi'].strip()
                    })
        
        print(f"Loaded {len(training_pairs)} training pairs from {file_path}")
        return training_pairs
    except Exception as e:
        print(f"Error loading CSV: {str(e)}")
        return []

def check_api_status():
    """Check if the API is running"""
    try:
        response = requests.get(f"{API_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"API Status: {data.get('status', 'Unknown')}")
            print(f"Model Status: {data.get('model_status', 'Unknown')}")
            print(f"Word Map Size: {data.get('word_map_size', 0)}")
            print(f"Phrase Map Size: {data.get('phrase_map_size', 0)}")
            return True
        else:
            print(f"API returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("Connection error: Could not connect to the API. Make sure the API server is running.")
        return False
    except Exception as e:
        print(f"Error checking API status: {str(e)}")
        return False

def add_training_data(training_pairs):
    """Add training data to the model"""
    try:
        # Process in batches to avoid overwhelming the API
        batch_size = 10
        total_pairs = len(training_pairs)
        
        for i in range(0, total_pairs, batch_size):
            end_idx = min(i + batch_size, total_pairs)
            batch = training_pairs[i:end_idx]
            
            print(f"Adding batch {i//batch_size + 1} ({len(batch)} pairs)...")
            
            response = requests.post(
                f"{API_URL}/train/add-data",
                json={"training_pairs": batch}
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"Success! Total pairs now: {data.get('pairs_count', 0)}")
            else:
                print(f"Failed to add training data: {response.status_code}")
                return False
            
            # Small delay to prevent overwhelming the API
            time.sleep(1)
        
        return True
    except Exception as e:
        print(f"Error adding training data: {str(e)}")
        return False

def rebuild_model():
    """Rebuild the translation model"""
    try:
        print("Rebuilding model...")
        response = requests.post(f"{API_URL}/train/rebuild-model")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Model rebuilt successfully: {data.get('message', '')}")
            print(f"Word Map Size: {data.get('word_map_size', 0)}")
            print(f"Phrase Map Size: {data.get('phrase_map_size', 0)}")
            return True
        else:
            print(f"Failed to rebuild model: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error rebuilding model: {str(e)}")
        return False

def test_translation(test_sentences):
    """Test the trained model with some sample sentences"""
    print("\nTesting the trained model...")
    
    for sentence in test_sentences:
        try:
            response = requests.post(
                f"{API_URL}/translate",
                json={"text": sentence, "preserve_formatting": True}
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    print(f"\nEnglish: {sentence}")
                    print(f"Hindi:   {data.get('translation', '')}")
                else:
                    print(f"Translation error: {data.get('error', 'Unknown error')}")
            else:
                print(f"API returned status code: {response.status_code}")
        
        except Exception as e:
            print(f"Error testing translation: {str(e)}")

def main():
    print("====== Government Document Translation Model Training ======")
    
    # Check API status
    if not check_api_status():
        print("Exiting due to API connectivity issues.")
        return
    
    # Load training data
    training_pairs = load_csv_data(TRAINING_DATA_FILE)
    if not training_pairs:
        print("No training data found. Exiting.")
        return
    
    # Add training data
    if not add_training_data(training_pairs):
        print("Failed to add all training data.")
    
    # Rebuild model for good measure
    rebuild_model()
    
    # Check final status
    print("\nFinal API Status:")
    check_api_status()
    
    # Test the model with some new phrases
    test_sentences = [
        "Please submit your application before the deadline.",
        "You are requested to attend the meeting on Friday.",
        "The government has announced a new policy for farmers.",
        "Your income tax returns must be filed by July 31st.",
        "This document requires your signature on all pages."
    ]
    
    test_translation(test_sentences)

if __name__ == "__main__":
    main()