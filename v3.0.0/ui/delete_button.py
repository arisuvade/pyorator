import customtkinter as ctk


class DeleteButton(ctk.CTkButton):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            width=100,
            height=30,
            border_width=0,
            corner_radius=8,
            text="Delete",
            fg_color="#8B2222",
            hover_color="#640000",
            **kwargs,
        )
