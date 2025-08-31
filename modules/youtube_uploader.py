from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_to_youtube(video_file, title, description, hashtags, thumbnail="ai_image.jpg"):
    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/youtube.upload"])
    youtube = build("youtube", "v3", credentials=creds)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": f"{title} | {hashtags.split()[0]}",
                "description": f"{description}\n\n{hashtags}",
                "tags": hashtags.split()
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload(video_file, chunksize=-1, resumable=True)
    )
    response = request.execute()

    youtube.thumbnails().set(
        videoId=response["id"],
        media_body=MediaFileUpload(thumbnail)
    ).execute()

    print(f"✅ Uploaded: https://youtube.com/watch?v={response['id']}")
