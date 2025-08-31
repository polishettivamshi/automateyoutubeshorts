from pytrends.request import TrendReq
import requests

def get_google_trends():
    pytrends = TrendReq(hl="en-US", tz=360)
    pytrends.build_payload(kw_list=["AI", "technology", "science", "fun facts", "history"])
    trending = pytrends.trending_searches(pn="united_states")
    return trending[0].tolist()[:5]  # top 5 trends

def get_youtube_trending():
    url = "https://www.youtube.com/feed/trending"
    response = requests.get(url)
    if response.status_code == 200:
        # A simple way to extract trending video titles
        titles = []
        for line in response.text.splitlines():
            if 'title' in line and 'simpleText' in line:
                cleaned = line.split('"')[3]
                if len(cleaned) > 5:
                    titles.append(cleaned)
        return titles[:5]
    return []

def get_trending_topics():
    try:
        topics = get_google_trends()
        if topics:
            return topics
    except:
        pass
    return get_youtube_trending()
