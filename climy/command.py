from climy.manager import Manager


class Command(Manager):
    def __init__(
            self,
            name: str,
            description: str,
            handler: callable = None
    ):
        self.name = name
        self.description = description
        self.handler = handler
        self.app = None
        super().__init__(name=name, description=description, )

    def run(self):
        ...
        ret = self.handler()
        return ret
