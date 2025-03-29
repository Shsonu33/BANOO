import os
from instabot import Bot
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure credentials are set
if not USERNAME or not PASSWORD:
    raise ValueError("Instagram username or password is missing. Please set them in the .env file.")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key is missing. Please set it in the .env file.")

# Initialize bot and login
bot = Bot()
bot.login(username=USERNAME, password=PASSWORD)

# Example: Upload a photo
PHOTO_PATH = "test.jpg"
CAPTION = "This is an automated post. #bot"

if os.path.exists(PHOTO_PATH):
    bot.upload_photo(PHOTO_PATH, caption=CAPTION)
    print("Photo uploaded successfully!")
else:
    print(f"Photo file {PHOTO_PATH} not found.")

# Logout
bot.logout()