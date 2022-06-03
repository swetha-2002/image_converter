import speech_recognition as sp_rg
import moviepy.editor as mpy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

no_sec_video = 52*60
print("The video is {} seconds".format(no_sec_video))
l=list(range(0,no_sec_video+1,60))

d ={}
for i in range(len(l)-1):
  ffmpeg_extract_subclip("video.mp4",l[i]-2*(l[i]!=0),l[i+1],targetname = "chunks/cut{}.mp4".format(i+1))
  clip = mpy.VideoFileClip(r"chunks/cut{}.mp4".format(i+1))
  clip.audio.write_audiofile(r"converted/converted{}.wav".format(i+1))
  recog = sp_rg.AudioFile("converted/converted{}.wav".format(i+1))
  with audio as source:
    recog.adjust_fro_ambient_noise(source)
    audio_file = recog.record(source)
 result = recog.recognize_google(audio_file)
 d['chunk{}'.format(i+1)]=result
  
