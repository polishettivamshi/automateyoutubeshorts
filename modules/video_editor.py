import subprocess
import os

def create_video(image_file, audio_file, music_file="assets/music.mp3", output_file="short.mp4"):
    command = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", image_file,
        "-i", audio_file, "-i", music_file,
        "-filter_complex", "[0:v]scale=720:1280,setsar=1[v];[1:a][2:a]amix=inputs=2:duration=shortest[a]",
        "-map", "[v]", "-map", "[a]",
        "-t", "60", output_file
    ]
    subprocess.run(command, check=True)
    return output_file
