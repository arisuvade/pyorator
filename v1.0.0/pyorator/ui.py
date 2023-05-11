import customtkinter as ctk

from ui.title_label import TitleLabel
from ui.text_entry import TextEntry
from ui.language_options import LanguageOptions
from ui.generate_speech_button import GenerateSpeechButton
from ui.error_label import ErrorLabel
from pyorator.convert_to_speech import convert_to_speech


class UI(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Window
        self.wm_title("PyOrator")
        self.geometry("300x260")
        self.resizable(False, False)

        # Title
        self.title = TitleLabel(self)
        self.title.place(relx=0.5, rely=0.05, anchor="center")

        # Text
        self.text_entry = TextEntry(self)
        self.text_entry.place(relx=0.5, rely=0.17, anchor="center")

        # Language
        self.language_options = LanguageOptions(self)
        self.language_options.place(relx=0.5, rely=0.31, anchor="center")

        # Generate speech
        self.generate_speech_button = GenerateSpeechButton(
            self, command=self.convert_to_speech
        )
        self.generate_speech_button.place(relx=0.5, rely=0.55, anchor="center")

        # Error
        self.error_label = ErrorLabel(self)
        self.error_label.place(relx=0.5, rely=0.97, anchor="center")

    def convert_to_speech(self):
        convert_to_speech(
            self.error_label,
            self.text_entry.get(),
            self.language_options.language.get(),
        )
