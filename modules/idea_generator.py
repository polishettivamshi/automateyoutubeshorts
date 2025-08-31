from modules.trends import get_trending_topics
import random

def generate_idea():
    trending_topics = get_trending_topics()
    topic = trending_topics[0] if trending_topics else "AI technology"
    
    # Template-based idea generation (no API needed)
    templates = [
        f"Amazing facts about {topic} that will blow your mind!",
        f"The truth about {topic} that nobody tells you",
        f"3 incredible things about {topic} you need to know",
        f"Why {topic} is changing the world right now",
        f"Secret facts about {topic} revealed!",
        f"How {topic} is transforming our daily lives",
        f"Top 5 mind-blowing facts about {topic}",
        f"The future of {topic} and what it means for you",
        f"Unexpected ways {topic} is being used today",
        f"Breaking down {topic} in 60 seconds"
    ]
    
    return random.choice(templates)