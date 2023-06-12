

class Option:
    def __init__(
            self,
            name: str,
            description: str,
            short: str = ''
    ):
        self.name = name
        self.description = description
        self.short = short
        self.variable = ''
