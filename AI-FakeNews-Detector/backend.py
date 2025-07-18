import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# --- Configuration ---
# Load environment variables from a .env file
load_dotenv(dotenv_path="key.env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the API key is available
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

# Configure the Generative AI client
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
# Adjust safety settings if you encounter blocking for news content
model = genai.GenerativeModel('gemini-1.5-flash-latest')


# --- Core Functions ---

def classify_news(article_text: str):
    """
    Analyzes news text to classify it as REAL or FAKE and provides a confidence score.
    
    Returns:
        tuple: (is_fake: bool, confidence: float)
    """
    prompt = f"""
    Analyze the following news article. Determine if it is REAL or FAKE news. 
    Provide a confidence score for your classification from 0.0 (low confidence) to 1.0 (high confidence).
    You MUST respond ONLY with a valid JSON object in the following format:
    {{"classification": "REAL_OR_FAKE", "confidence": 0.0_TO_1.0}}

    Article:
    ---
    {article_text}
    ---

    JSON Response:
    """
    
    try:
        response = model.generate_content(prompt)
        # Clean up the response to extract the JSON part
        json_response = response.text.strip().replace("```json", "").replace("```", "")
        
        # Parse the JSON string into a Python dictionary
        data = json.loads(json_response)
        
        classification = data.get("classification", "FAKE").upper()
        confidence = float(data.get("confidence", 0.5))
        
        is_fake = (classification == "FAKE")
        
        return is_fake, confidence
        
    except (json.JSONDecodeError, AttributeError, ValueError) as e:
        print(f"Error processing Gemini response: {e}")
        # Return a default value in case of an error
        return True, 0.5 


def generate_real_version(fake_news_text: str):
    """
    Takes a piece of fake news and rewrites it to be factually accurate.
    
    Returns:
        str: The rewritten, factual version of the news.
    """
    prompt = f"""
    The following news article has been identified as FAKE. 
    Your task is to rewrite it as a factual, neutral, and realistic news report based on the likely real events it is twisting.
    If the original story is entirely baseless with no connection to reality, state that there are no factual events corresponding to the claims.
    Focus on clarity and objectivity.

    Original Fake Article:
    ---
    {fake_news_text}
    ---

    Factual and Realistic Version:
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating real version: {e}")
        return "Could not generate a factual version due to an API error."