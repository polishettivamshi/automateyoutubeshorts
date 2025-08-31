import os
from dotenv import load_dotenv
import openai
from PIL import Image, ImageDraw, ImageFont

# Import modules
from modules.idea_generator import generate_idea
from modules.hashtags import generate_hashtags
from modules.image_generator import generate_image
from modules.tts_generator import generate_tts
from modules.video_editor import create_video
from modules.youtube_uploader import upload_to_youtube

# Load ENV
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_placeholder_image():
    """Create a placeholder image if it doesn't exist"""
    if not os.path.exists("assets/placeholder.jpg"):
        if not os.path.exists("assets"):
            os.makedirs("assets")
        
        img = Image.new('RGB', (1024, 1024), color=(70, 130, 180))
        d = ImageDraw.Draw(img)
        try:
            fnt = ImageFont.truetype("arial.ttf", 60)
            d.text((300, 450), "YouTube Short", font=fnt, fill=(255, 255, 255))
        except:
            # If font not available, just create a colored image
            pass
        img.save("assets/placeholder.jpg")
        print("📁 Created placeholder image")

if __name__ == "__main__":
    # Create placeholder image if needed
    create_placeholder_image()
    
    # 1. Generate Idea
    idea = generate_idea()
    print("💡 Idea:", idea)

    # 2. Generate Hashtags
    hashtags = generate_hashtags(idea)
    print("📌 Hashtags:", hashtags)

    # 3. Generate Image
    image = generate_image(idea)
    print("🖼️ Image Created")

    # 4. Generate TTS
    audio = generate_tts(idea)
    print("🎙️ Voice Created")

    # 5. Create Video
    video = create_video(image, audio)
    print("🎬 Video Created")

    # 6. Upload to YouTube
    upload_to_youtube(video, f"AI Shorts: {idea}", f"Watch how AI imagines: {idea}", hashtags)
    print("📢 Upload Completed")