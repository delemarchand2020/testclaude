import os
import base64
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class OpenAIService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        self.base_url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def analyze_image(self, image_data, prompt="Please describe in french this image in detail. What do you see?"):
        """Analyze an image using OpenAI GPT-4o model"""
        try:
            # Encode image to base64
            base64_image = base64.b64encode(image_data).decode("utf-8")
            
            payload = {
                "model": "gpt-4o",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
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
                self.base_url,
                headers=self.headers,
                json=payload
            )
            
            # Parse response
            if response.status_code == 200:
                response_data = response.json()
                return {
                    "success": True,
                    "content": response_data["choices"][0]["message"]["content"]
                }
            else:
                return {
                    "success": False,
                    "error": f"API request failed with status code {response.status_code}: {response.text}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"An error occurred: {str(e)}"
            }