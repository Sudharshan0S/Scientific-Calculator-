import tkinter as tk
from src.ui.display_screen import DisplayScreen
from src.ui.button_layout import ButtonLayout
from src.ui.history_panel import HistoryPanel
from src.calculator.parser.expression_parser import ExpressionParser
from src.calculator.validation.validator import Validator
from src.calculator.history.history_manager import HistoryManager
from src.calculator.memory.memory import memory_store
from src.calculator.memory.memory import memory_recall
from src.calculator.memory.memory import memory_clear
from src.calculator.memory.memory import memory_add
from src.calculator.security.safe_eval import set_angle_mode
from src.calculator.utils.logger import log_message
from src.calculator.utils.constants import WINDOW_TITLE

class ScientificCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry("520x780")
        self.root.configure(bg="#1E1E1E")
        self.root.state("zoomed")
        self.root.resizable(True, True)

        self.history_manager = HistoryManager()

        self.display = DisplayScreen(self.root)

        self.angle_mode = tk.StringVar(value="DEG")

        self.create_angle_mode_selector()

        self.buttons = ButtonLayout(
            self.root,
            self.button_click
        )

        self.history_panel = HistoryPanel(
            self.root,
            self.load_history_expression
        )

        self.root.bind("<Key>", self.key_pressed)

    def create_angle_mode_selector(self):
        mode_frame = tk.Frame(
            self.root,
            bg="#1E1E1E"
        )

        mode_frame.pack(
            fill="x",
            padx=18,
            pady=(0, 8)
        )

        left_frame = tk.Frame(
            mode_frame,
            bg="#1E1E1E"
        )

        left_frame.pack(anchor="w")

        deg_radio = tk.Radiobutton(
            left_frame,
            text="DEG",
            variable=self.angle_mode,
            value="DEG",
            command=self.change_angle_mode,
            font=("Segoe UI", 10, "bold"),
            bg="#1E1E1E",
            fg="white",
            selectcolor="#2D2D2D",
            activebackground="#1E1E1E",
            activeforeground="white",
            cursor="hand2"
        )

        rad_radio = tk.Radiobutton(
            left_frame,
            text="RAD",
            variable=self.angle_mode,
            value="RAD",
            command=self.change_angle_mode,
            font=("Segoe UI", 10, "bold"),
            bg="#1E1E1E",
            fg="white",
            selectcolor="#2D2D2D",
            activebackground="#1E1E1E",
            activeforeground="white",
            cursor="hand2"
        )

        deg_radio.pack(side="left", padx=(0, 10))
        rad_radio.pack(side="left")

    def change_angle_mode(self):
        selected_mode = self.angle_mode.get()
        set_angle_mode(selected_mode)

    def button_click(self, value):
        if value == "=":
            self.calculate()

        elif value == "C":
            self.display.clear()

        elif value == "⌫":
            current = self.display.get_value()
            self.display.set_value(current[:-1])

        elif value == "MS":
            try:
                current_text = self.display.get_value()

                if "=" in current_text:
                    current_text = current_text.split("=")[-1].strip()

                current_value = float(current_text)

                memory_store(current_value)

            except:
                self.display.set_value("Memory Error")

        elif value == "MR":
            recalled_value = memory_recall()
            self.display.set_value(str(recalled_value))

        elif value == "MC":
            memory_clear()

        elif value == "M+":
            try:
                current_text = self.display.get_value()

                if "=" in current_text:
                    current_text = current_text.split("=")[-1].strip()

                current_value = float(current_text)

                updated_memory = memory_add(current_value)

                self.display.set_value(str(updated_memory))

            except:
                self.display.set_value("Memory Error")

        elif value == "M-":
            try:
                current_text = self.display.get_value()

                if "=" in current_text:
                    current_text = current_text.split("=")[-1].strip()

                current_value = float(current_text)

                updated_memory = memory_add(-current_value)

                self.display.set_value(str(updated_memory))

            except:
                self.display.set_value("Memory Error")

        else:
            self.display.append_value(value)

    def key_pressed(self, event):
        allowed = "1234567890+-*/().%"

        if event.char in allowed:
            self.display.append_value(event.char)

        elif event.keysym == "Return":
            self.calculate()

        elif event.keysym == "BackSpace":
            current = self.display.get_value()
            self.display.set_value(current[:-1])

    def calculate(self):
        expression = self.display.get_value()

        if not Validator.validate(expression):
            self.display.set_value("Input Required")
            return

        try:
            result = ExpressionParser.evaluate(expression)

            final_output = f"{expression} = {result}"

            self.display.set_value(str(result))

            self.history_manager.add_history(final_output)

            self.history_panel.add_item(final_output)

            log_message(final_output)

        except ZeroDivisionError:
            self.display.set_value("Cannot Divide By Zero")

        except SyntaxError:
            self.display.set_value("Invalid Syntax")

        except NameError:
            self.display.set_value("Invalid Function")

        except ValueError:
            self.display.set_value("Math Error")

        except OverflowError:
            self.display.set_value("Number Too Large")

        except TypeError:
            self.display.set_value("Invalid Operation")

        except Exception:
            self.display.set_value("Calculation Error")

    def load_history_expression(self, expression):
        self.display.set_value(expression)

    def run(self):
        self.root.mainloop()