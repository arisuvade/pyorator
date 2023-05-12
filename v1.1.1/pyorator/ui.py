import customtkinter as ctk

from ui.title_label import TitleLabel
from ui.text_entry import TextEntry
from ui.file_name_entry import FileNameEntry
from ui.language_options import LanguageOptions
from ui.generate_speech_button import GenerateSpeechButton
from ui.theme_switch import ThemeSwitch
from ui.error_label import ErrorLabel
from pyorator.convert_to_speech import convert_to_speech


class UI(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Window
        self.wm_title("PyOrator")
        self.geometry("300x220")
        self.resizable(False, False)

        # Title
        self.title = TitleLabel(self)
        self.title.place(relx=0.5, rely=0.05, anchor="center")

        # Text
        self.text_entry = TextEntry(self)
        self.text_entry.place(relx=0.5, rely=0.20, anchor="center")

        # File name
        self.file_name_entry = FileNameEntry(self)
        self.file_name_entry.place(relx=0.5, rely=0.35, anchor="center")

        # Language
        self.language_options = LanguageOptions(self)
        self.language_options.place(relx=0.5, rely=0.53, anchor="center")

        # Generate speech
        self.generate_speech_button = GenerateSpeechButton(
            self, command=self.convert_to_speech
        )
        self.generate_speech_button.place(relx=0.5, rely=0.70, anchor="center")

        # Theme switch
        self.theme_switch = ThemeSwitch(self)
        self.theme_switch.place(relx=0.5, rely=0.85, anchor="center")

        # Error
        self.error_label = ErrorLabel(self)
        self.error_label.place(relx=0.5, rely=0.95, anchor="center")

    def convert_to_speech(self):
        convert_to_speech(
            self.error_label,
            self.text_entry.get(),
            self.file_name_entry.get(),
            self.language_options.language.get(),
        )
