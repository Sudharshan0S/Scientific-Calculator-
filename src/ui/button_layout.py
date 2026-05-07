import tkinter as tk


class ButtonLayout:

    def __init__(self, root, callback):

        self.root = root

        self.callback = callback

        self.frame = tk.Frame(
            root,
            bg="#1E1E1E"
        )

        self.frame.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=10
        )

        self.toggle_mode = False

        self.normal_buttons = [

            ["Toggle", "⌫", "C", "%", "/"],

            ["7", "8", "9", "*", "("],

            ["4", "5", "6", "-", ")"],

            ["1", "2", "3", "+", "**"],

            ["0", ".", "=", "pi", "e"],

            ["MS", "MR", "MC", "M+", "M-"]

        ]

        self.scientific_buttons = [

            ["Toggle", "⌫", "C", "%", "/"],

            ["sin(", "cos(", "tan(", "log(", "ln("],

            ["sqrt(", "factorial(", "pi", "e", "**"],

            ["7", "8", "9", "*", "("],

            ["4", "5", "6", "-", ")"],

            ["1", "2", "3", "+", "="],

            ["0", ".", "MS", "MR", "MC"]

        ]

        self.render_buttons()

    def clear_buttons(self):

        for widget in self.frame.winfo_children():

            widget.destroy()

    def render_buttons(self):

        self.clear_buttons()

        buttons = (
            self.scientific_buttons
            if self.toggle_mode
            else self.normal_buttons
        )

        for row in buttons:

            row_frame = tk.Frame(
                self.frame,
                bg="#1E1E1E"
            )

            row_frame.pack(
                expand=True,
                fill="both",
                pady=3
            )

            for button in row:

                if button in ["=", "+", "-", "*", "/", "C"]:

                    bg_color = "#FF9500"

                elif button == "Toggle":

                    bg_color = "#505050"

                else:

                    bg_color = "#2D2D2D"

                btn = tk.Button(
                    row_frame,
                    text=button,
                    font=("Segoe UI", 14, "bold"),
                    bg=bg_color,
                    fg="white",
                    activebackground="#3C3C3C",
                    activeforeground="white",
                    relief=tk.FLAT,
                    bd=0,
                    height=2,
                    width=5,
                    cursor="hand2",
                    command=lambda b=button:
                    self.button_action(b)
                )

                btn.pack(
                    side="left",
                    expand=True,
                    fill="both",
                    padx=3
                )

    def button_action(self, value):

        if value == "Toggle":

            self.toggle_mode = (
                not self.toggle_mode
            )

            self.render_buttons()

        else:

            self.callback(value)