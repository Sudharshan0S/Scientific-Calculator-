import tkinter as tk


class DisplayScreen:

    def __init__(self, root):

        self.display_frame = tk.Frame(
            root,
            bg="#1E1E1E"
        )

        self.display_frame.pack(
            fill="x",
            padx=15,
            pady=(15, 5)
        )

        self.entry = tk.Entry(
            self.display_frame,
            font=("Segoe UI", 28, "bold"),
            bg="#2B2B2B",
            fg="white",
            bd=0,
            relief=tk.FLAT,
            justify="right",
            insertbackground="white"
        )

        self.entry.pack(
            fill="both",
            ipadx=8,
            ipady=20
        )

    def get_value(self):

        return self.entry.get()

    def set_value(self, value):

        self.entry.delete(0, tk.END)

        self.entry.insert(0, str(value))

    def append_value(self, value):

        current = self.entry.get()

        self.entry.delete(0, tk.END)

        self.entry.insert(0, current + str(value))

    def clear(self):

        self.entry.delete(0, tk.END)