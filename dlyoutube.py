# pip install yt_dlp

import yt_dlp
def download_youtube_video(url, save_path="."):#ฟังก์ชัน
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',#ใส่ชื่อตัวแปร
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
video_url = input("Enter the YouTube video URL: ")#ใส่ลิ้งค์ยูทูป
download_youtube_video(video_url, save_path=".") #้รียกใช้ฟังก์ชัน
