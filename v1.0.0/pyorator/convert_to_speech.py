from gtts import gTTS


def convert_to_speech(text, language):
    match language:
        case "Japanese":
            lang = "ja"
        case "Korean":
            lang = "ko"
        case _:
            lang = "en"

    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("test.mp3")
