import os
from googleapiclient.discovery import build
from src.constants import API_KEY

class MyException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Hесуществующий id видео"

    def __str__(self):
        return self.message


class Video:
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, video_id: str, ):
        self.video_id = video_id
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=video_id).execute()
        try:
            if len(self.video_response['items']) == 0:
                raise MyException

            self.title = self.video_response['items'][0]['snippet']['title']
            self.url_video = f"https://youtu.be/{self.video_id}"
            self.viewCount = self.video_response['items'][0]['statistics']['viewCount']
            self.likeCount = self.video_response['items'][0]['statistics']['likeCount']

        except MyException:
            self.title = None
            self.url_video = None
            self.viewCount = None
            self.likeCount = None

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f'{self.title}'