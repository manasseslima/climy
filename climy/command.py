

class Command:
    def __init__(
            self,
            description: str
    ):
        self.description = description

    def run(self):
        ...
