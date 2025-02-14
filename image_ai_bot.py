import os
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to generate an image using OpenAI's DALL·E API
def generate_image(prompt):
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
        "n": 1,  # Number of images to generate
        "size": "512x512",  # Image size
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        image_url = result["data"][0]["url"]
        return image_url
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Function to display the generated image
def display_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()

# Main function
if __name__ == "__main__":
    # Text prompt for image generation
    prompt = input("Enter a text prompt for image generation: ")

    # Generate the image
    image_url = generate_image(prompt)

    if image_url:
        print(f"Image generated successfully! URL: {image_url}")
        display_image(image_url)
    else:
        print("Failed to generate image.")