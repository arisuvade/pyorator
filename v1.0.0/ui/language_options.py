import customtkinter as ctk


class LanguageOptions(ctk.CTkOptionMenu):
    def __init__(self, parent, **kwargs):
        self.language = ctk.StringVar(value="English")
        super().__init__(
            parent,
            values=["English", "Japanese", "Korean"],
            variable=self.language,
            font=("Jetbrains Mono", 14),
            **kwargs,
        )
        self.set("English")
