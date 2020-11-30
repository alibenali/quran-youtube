import subprocess
import os, random
from youtube.upload_videos import video as video
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from moviepy.editor import AudioFileClip, VideoFileClip, concatenate_videoclips
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

try:
    os.remove("test.mp4")
except:
    pass
    
    
randomAudio = random.choice(os.listdir("C:\\Users\\Ali\\Desktop\\EXP\\pexelsAPI\\audios"))
audioPath = "audios/"+randomAudio
audio = MP3(audioPath)
print(audio.info.length)
print(randomAudio)     





clipDuration = 0
videos = []
while (clipDuration < audio.info.length):
    videoName = random.choice(os.listdir("C:\\Users\\Ali\\Desktop\\EXP\\pexelsAPI\\videos\\nature"))
    videoPath = 'videos/nature/' + videoName
    clip = VideoFileClip(videoPath)
    clipDuration = clipDuration + clip.duration
    videos.append(clip)
    print(videoName)
    print(clipDuration)
    
video_clip = concatenate_videoclips(videos)
audio_clip = AudioFileClip(audioPath)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile('test.mp4')

end_video = audio.info.length + 3
ffmpeg_extract_subclip("test.mp4", 0, end_video, targetname="final.mp4")

audioInfo = EasyID3(audioPath)
videoTitle =  str(audioInfo['artist']) + str(audioInfo['title'])
videoTitle = ''.join(e for e in videoTitle if (e.isalnum() or e == " " or e == "&" or e == "-" or e == "(" or e == ")"))
print(videoTitle)
videoDesc = videoTitle + "\n\n صلي على الحبيب المصطفى"
videoTags = ['Quraan', 'Coraan']
daVideo = video(videoTitle, videoDesc, videoTags, 'creativeCommon', 'public', 'final.mp4')
daVideo.upload()




