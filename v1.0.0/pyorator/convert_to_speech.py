from gtts import gTTS


language = "en"
text = "Hello, humans! I will destroy humanity!"

speech = gTTS(text=text, lang=language, slow=False)
speech.save("test1.mp3")
