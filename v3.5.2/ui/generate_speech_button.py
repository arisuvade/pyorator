import customtkinter as ctk


class GenerateSpeechButton(ctk.CTkButton):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            width=100,
            height=30,
            border_width=0,
            corner_radius=8,
            text="Generate Speech",
            fg_color="forest green",
            hover_color="dark green",
            **kwargs,
        )
