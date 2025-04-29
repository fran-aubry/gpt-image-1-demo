# Import the packages
from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

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
  n=1,
  size="1024x1024",
  quality="high",
)

# Save the image into a file named output.png
image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output.png", "wb") as f:
  f.write(image_bytes)