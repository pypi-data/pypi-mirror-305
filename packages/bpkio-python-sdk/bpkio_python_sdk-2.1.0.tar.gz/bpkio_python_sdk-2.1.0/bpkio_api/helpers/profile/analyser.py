class Message:
    def __init__(self, level: str, message: str):
        self.level = level
        self.message = message

    def __repr__(self) -> str:
        return f"{self.level}: {self.message}"


class WarningMessage(Message):
    def __init__(self, message: str):
        super().__init__("warning", message)


class ErrorMessage(Message):
    def __init__(self, message: str):
        super().__init__("error", message)


class InfoMessage(Message):
    def __init__(self, message: str):
        super().__init__("info", message)
