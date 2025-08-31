from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder():
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

if __name__ == "__main__":
    create_placeholder()
    print("✅ Placeholder image created at assets/placeholder.jpg")