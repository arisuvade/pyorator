import customtkinter as ctk


class TitleLabel(ctk.CTkLabel):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text="Enter the text and file name",
            font=("Jetbrains Mono", 14, "bold"),
            **kwargs,
        )

        # Update title every 5 seconds
        self.after(5000, self.update_title)

    def update_title(self):
        self.configure(text="Hover the mouse to end")
        self.master.after(5000, self.reset_title)

    def reset_title(self):
        self.configure(text="Enter the text and file name")
        self.master.after(5000, self.update_title)
