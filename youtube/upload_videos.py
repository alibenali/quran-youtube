import datetime
from youtube.Google import Create_Service
from googleapiclient.http import MediaFileUpload
import socket

class video:
    def __init__(self, title, description, tags, dalicense, privacyStatus, video):
        self.title = title
        self.description = description
        self.tags = tags
        self.dalicense = dalicense
        self.privacyStatus = privacyStatus
        self.video = video
        socket.setdefaulttimeout(60000)

    
    def upload(self):
        CLIENT_SECRET_FILE = 'youtube/client_secret_788030058778-fp90f83q4tdauhh329pmk5uk6vhspmrc.apps.googleusercontent.com.json'
        API_NAME = 'youtube'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        upload_date_time = datetime.datetime(2020, 12, 25, 12, 30, 0).isoformat() + '.000Z'

        request_body = {
            'snippet': {
                'categoryI': 19,
                'title': self.title,
                'description': self.description,
                'tags': self.tags
            },
            'status': {
                'license': self.dalicense,
                'privacyStatus': self.privacyStatus,
                # 'publishAt': upload_date_time,
                'selfDeclaredMadeForKids': False, 
            },
            'notifySubscribers': True
        }

        mediaFile = MediaFileUpload(self.video)

        response_upload = service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediaFile
        ).execute()


        # service.thumbnails().set(
            # videoId=response_upload.get('id'),
            # media_body=MediaFileUpload('thumbnail.png')
        # ).execute()