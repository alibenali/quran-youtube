import requests
import urllib.request
from random import randint

headers = {
    'Authorization': '563492ad6f91700001000001d5d0453e7bbd44b1bb78938d5293d247',
}

domain = 'nature'
params = (
    ('query', domain),
    ('per_page', '50'),
    ('page', '1'),
    ('min_width', '1280'),
    ('max_width', '1280'),
    ('min_height', '720'),
    ('max_height', '720'),
    ('min_duration', '40'),

)

response = requests.get('https://api.pexels.com/videos/search', headers=headers, params=params)
data = response.json()

for video in data['videos']:
    videoLink = video['video_files'][0]['link']
    urllib.request.urlretrieve(videoLink, 'videos/'+str(domain)+'/'+str(randint(99999999,999999999999))+'.mp4') 
