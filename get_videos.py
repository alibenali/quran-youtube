import requests
import urllib.request
from random import randint

headers = {
    'Authorization': '563492ad6f91700001000001d5d0453e7bbd44b1bb78938d5293d247',
}

domain = 'nature'
params = (
    ('query', domain),
    ('per_page', '100'),
    ('page', '1'),
    ('min_width', '1280'),
)

response = requests.get('https://api.pexels.com/videos/search', headers=headers, params=params)
data = response.json()

for video in data['videos']:
    for videoFiles in video['video_files']:
        if videoFiles['width'] == 1280 and videoFiles['height'] == 720:
            videoLink = videoFiles['link']
            urllib.request.urlretrieve(videoLink, 'videos/'+str(domain)+'/new'+str(randint(99999999,999999999999))+'.mp4') 
