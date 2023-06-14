import sys
from climy.manager import Manager


class Application(Manager):
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

    def generate_help(self):
        text = "\033[1m{title}\033[0m (version {version})".format(title=self.title, version=self.version)
        text += super().generate_help()
        return text

    def run(self):
        self.args = [*sys.argv]
        self.workdir = self.args.pop(0)
        if not self.args or self.args[0] in ['-h', '--help', 'help']:
            text = self.generate_help()
            print(text)
            return
        command = self.commands.get(self.args[0], None)
        if command:
            command.args = self.args[1:]
            command.run()
        else:
            for arg in self.args:
                pair = arg.split('=')
                idx = 0
                if pair[0].startswith('--'):
                    idx = 2
                elif pair[0].startswith('-'):
                    idx = 1
                key = pair[0][idx:]
                name = self.options_short.get(key, key)
                option = self.options.get(name, None)
                if not option:
                    self.vars = name
                    continue
                option.value = pair.pop(1)
