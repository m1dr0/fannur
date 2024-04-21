import subprocess
import os
import sys
import token
from huggingface_hub import notebook_login
from pyannote.audio import Pipeline
import speechbrain
import re
from pydub import AudioSegment
import whisper



# auth_token = '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'

# pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization-3.1', use_auth_token = auth_token)

# def millisec(timeStr):
#   spl = timeStr.split(":")
#   s = (int)((int(spl[0]) * 60 * 60 + int(spl[1]) * 60 + float(spl[2]) )* 1000)
#   return s

# DEMO_FILE = 'test.wav'
# dz = pipeline(DEMO_FILE)  

# with open("diarization.txt", "w") as text_file:
#     text_file.write(str(dz))

# print(*list(dz.itertracks(yield_label = True))[:10], sep="\n")

# dzs = open('diarization.txt').read().splitlines()

# groups = []
# g = []
# lastend = 0

# for d in dzs:   
#   if g and (g[0].split()[-1] != d.split()[-1]):      #same speaker
#     groups.append(g)
#     g = []
  
#   g.append(d)
  
#   end = re.findall('[0-9]+:[0-9]+:[0-9]+\.[0-9]+', string=d)[1]
#   end = millisec(end)
#   if (lastend > end):       #segment engulfed by a previous segment
#     groups.append(g)
#     g = [] 
#   else:
#     lastend = end
# if g:
#   groups.append(g)
# print(*groups, sep='\n')

# audio = AudioSegment.from_wav("audio.wav")
# gidx = -1
# for g in groups:
#   start = re.findall('[0-9]+:[0-9]+:[0-9]+\.[0-9]+', string=g[0])[0]
#   end = re.findall('[0-9]+:[0-9]+:[0-9]+\.[0-9]+', string=g[-1])[1]
#   start = millisec(start) #- spacermilli
#   end = millisec(end)  #- spacermilli
#   print(start, end)
#   gidx += 1
#   audio[start:end].export(str(gidx) + '.wav', format='wav')

model = whisper.load_model("large")
model.transcribe(r'C:\Users\hm1dr\OneDrive\Рабочий стол\diplom\venv\0.wav')
