

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
        self.var_name = ''
        self.var_type = 'bool'
        self.value = None
