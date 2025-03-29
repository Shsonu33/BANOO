import os import time import openai from instabot import Bot from dotenv import load_dotenv

Load API keys from .env file

load_dotenv() OPENAI_API_KEY = os.getenv("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") IG_USERNAME = os.getenv("riya455817") IG_PASSWORD = os.getenv("Monu@360")

OpenAI API Setup

openai.api_key = OPENAI_API_KEY

def generate_reply(message): """Generate AI-powered reply using OpenAI's GPT model.""" try: response = openai.ChatCompletion.create( model="gpt-4o", messages=[ {"role": "system", "content": "You are a friendly and flirty chatbot that gives engaging replies."}, {"role": "user", "content": message}, ], max_tokens=50 ) return response["choices"][0]["message"]["content"].strip() except Exception as e: return "Sorry, I couldn't process that right now. Try again later!"

Instagram Bot Setup

bot = Bot() bot.login(username=IG_USERNAME, password=IG_PASSWORD)

def check_messages(): """Check for new messages and reply automatically.""" while True: messages = bot.get_messages() for user_id, msgs in messages.items(): for msg in msgs: reply = generate_reply(msg) bot.send_message(reply, user_id) print(f"Replied to {user_id}: {reply}") time.sleep(30)  # Wait before checking again

if name == "main": check_messages()

