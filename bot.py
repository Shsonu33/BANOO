import os
import time
import openai
from instabot import Bot
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
INSTAGRAM_USERNAME = os.getenv("riya455817")
INSTAGRAM_PASSWORD = os.getenv("Monu@360")
OPENAI_API_KEY = os.getenv("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")

# Validate environment variables
if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD or not OPENAI_API_KEY:
    raise ValueError("Missing environment variables! Check your .env file.")

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

# Initialize and login to Instagram bot
bot = Bot()
bot.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

# Function to generate AI-generated Instagram captions
def generate_caption(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a creative social media assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

# Example usage
if __name__ == "__main__":
    prompt = "Write a fun Instagram caption about a sunset."
    caption = generate_caption(prompt)
    print("Generated Caption:", caption)

    # Optional: Upload an image with caption
    image_path = "sunset.jpg"  # Ensure this file exists in your project folder
    if os.path.exists(image_path):
        bot.upload_photo(image_path, caption=caption)
    else:
        print("Image file not found:", image_path)