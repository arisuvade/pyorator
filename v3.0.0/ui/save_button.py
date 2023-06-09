import customtkinter as ctk


class SaveButton(ctk.CTkButton):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            width=100,
            height=30,
            border_width=0,
            corner_radius=8,
            text="Save",
            fg_color="#00688B",
            hover_color="#00008B",
            **kwargs,
        )
