import os
import sys
import base64
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def analyze_image(image_path):
    """Send an image to OpenAI GPT-4o and get the analysis results."""
    
    # Get API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)
    
    try:
        # Read and encode the image
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Please describe in french this image in detail. What do you see?"},
                        {"type": "image_url", 
                         "image_url": {
                             "url": f"data:image/jpeg;base64,{base64_image}"
                         }
                        }
                    ]
                }
            ],
            "max_tokens": 1000
        }
        
        # Send request to OpenAI API
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload
        )
        
        # Parse response
        if response.status_code == 200:
            response_data = response.json()
            return response_data["choices"][0]["message"]["content"]
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            print(response.text)
            return None
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python vision_app.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found")
        sys.exit(1)
    
    print(f"Analyzing image: {image_path}...")
    analysis = analyze_image(image_path)
    
    if analysis:
        print("\nImage Analysis Result:")
        print("-" * 50)
        print(analysis)
        print("-" * 50)
    else:
        print("Failed to analyze the image")

if __name__ == "__main__":
    main()