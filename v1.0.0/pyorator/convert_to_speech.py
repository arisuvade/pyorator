from gtts import gTTS


def convert_to_speech(error_label, text, language):
    # Clear error message
    error_label.configure(text="")

    match language:
        case "Japanese":
            lang = "ja"
        case "Korean":
            lang = "ko"
        case _:
            lang = "en"

    try:
        speech = gTTS(text=text, lang=lang, slow=False)
        speech.save("test.mp3")
    except AssertionError:
        error_label.configure(text="Error: The text can't be empty.")
