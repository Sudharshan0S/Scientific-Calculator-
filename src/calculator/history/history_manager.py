class HistoryManager:
    def __init__(self):
        self.history = []
        self.limit = 30

    def add_history(self, calculation):
        self.history.append(calculation)

        if len(self.history) > self.limit:
            self.history.pop(0)

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()
