import random

def generate_hashtags(idea):
    # Extract keywords from the idea
    words = idea.lower().split()
    keywords = [word for word in words if len(word) > 3 and word not in ['about', 'that', 'this', 'with', 'your', 'will']]
    
    if not keywords:
        keywords = ['ai', 'technology', 'facts', 'future']
    
    # Create hashtags based on keywords
    hashtags = []
    for keyword in keywords[:3]:
        hashtags.extend([
            f"#{keyword}",
            f"#{keyword}facts",
            f"#{keyword}shorts",
            f"#{keyword}trending"
        ])
    
    # Add some general popular hashtags
    popular_hashtags = [
        "#viral", "#trending", "#shorts", "#youtubeshorts", 
        "#facts", "#didyouknow", "#learnontiktok", "#education",
        "#tech", "#innovation"
    ]
    
    # Combine and limit to 10 hashtags
    all_hashtags = hashtags + popular_hashtags
    return " ".join(all_hashtags[:10])