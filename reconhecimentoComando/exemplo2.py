import speech_recognition as sr
recon = sr.Recognizer()

with sr.Microphone() as mic:
    print("Fale algo...")
    audio = recon.adjust_for_ambient_noise(mic)
    print("Aguarde...reconhecendo áudio...")
    print(recon.recognize_google(audio, language='pt'))