class KeyboardSupport:
    @staticmethod
    def handle_keypress(event, callback):
        callback(event.char)
