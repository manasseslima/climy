import sys
from climy.command import Command


class Application(Command):
    def __init__(
            self,
            name: str,
            description: str,
            title: str = '',
            version: str = '0.0.0'
    ):
        self.title = title
        self.version = version
        self.workdir: str = ''
        super().__init__(name=name, description=description, title=title)

    def generate_help(self, text: str = ''):
        text += "\033[1m{title}\033[0m (version {version})".format(title=self.title, version=self.version)
        text = super().generate_help(text=f'{text}\r\n\r\n')
        return text

    def run(self):
        self.args = [*sys.argv]
        self.workdir = self.args.pop(0)
        super().run()
