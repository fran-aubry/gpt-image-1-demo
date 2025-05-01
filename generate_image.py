# Import the packages
from openai import OpenAI
from dotenv import load_dotenv
import os
import base64
import time

# Load the API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Ask the user to input a prompt in the terminal
print("What do you want to generate?")
prompt = input("> ")
print("Generating image...")
# Send the prompt to the API
img = client.images.generate(
  model="gpt-image-1",
  prompt=prompt,
  background="transparent",
  n=1,
  quality="low",
  size="1024x1024",
  moderation="auto",
  output_format="png",
)
print("Prompt tokens:", img.usage.input_tokens_details.text_tokens)
print("Input images tokens:", img.usage.input_tokens_details.image_tokens)
print("Output image tokens:", img.usage.output_tokens)

# Save the image into a file named output.png
image_bytes = base64.b64decode(img.data[0].b64_json)
with open(f"output_{int(time.time())}.png", "wb") as f:
  f.write(image_bytes)