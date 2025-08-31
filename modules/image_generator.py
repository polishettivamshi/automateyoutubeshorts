import openai
import requests
import os

def generate_image(prompt, output_file="ai_image.jpg"):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024"
    )
    img_url = response['data'][0]['url']
    img_data = requests.get(img_url).content
    with open(output_file, "wb") as f:
        f.write(img_data)
    return output_file