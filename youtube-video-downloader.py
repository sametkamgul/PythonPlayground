from pytube import YouTube
yt_url = 'https://www.youtube.com/watch?v=0HRett4kOpM'
yt = YouTube(yt_url)
yt = yt.get('mp4', '720p')
yt.download('outputImages')
