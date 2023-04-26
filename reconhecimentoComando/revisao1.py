from gtts import gTTS
from playsound import playsound
msg = 'É nóis que voa, bruxão'

audio = gTTS(msg, lang='pt')
audio.save('bruxao.mp3')
playsound('bruxao.mp3')
