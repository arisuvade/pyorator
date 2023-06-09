from gtts import gTTS


def convert_to_speech(error_label, text, file_name):
    # Clear error message
    error_label.configure(text="")

    try:
        speech = gTTS(text=text, slow=False)
        if file_name:
            speech.save(f"{file_name}.mp3")
        else:
            raise AssertionError
    except AssertionError:
        error_label.configure(text="Error: Text and file name can't be empty")
