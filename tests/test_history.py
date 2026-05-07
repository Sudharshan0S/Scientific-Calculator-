from src.calculator.history.history_manager import HistoryManager

history = HistoryManager()
history.add_history("2+2=4")

print(history.get_history())
