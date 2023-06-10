import sys
from climy.command import Command


class Application:
    def __init__(
            self,
            name: str = '',
            title: str = '',
            description: str = '',
            version: str = '0.0.0'
    ):
        self.commands: dict[str, Command] = {}
        self.path: str = ''
        self.name = name
        self.title = title
        self.description = description
        self.version = version
        self.help_item_tabsize = 20

    def add_command(self, name: str, command: Command):
        self.commands[name] = command

    def run(self):
        args = sys.argv
        self.path = args.pop(0)
        if not args or args[0] in ['-h', '--help', 'help']:
            self.generate_help()
            return
        name = args.pop(0)
        command = self.commands.get(name, None)
        if command:
            command.run()

    def generate_help(self):
        text = f"{self.title} (version {self.version})"
        text += "\r\n\r\nUsage:\r\n  {name} <command> [options] [arguments]".format(name=self.name)
        text += "\r\n\r\nOptions:\r\n  {txt} Display this help".format(txt="-h, --help".ljust(self.help_item_tabsize))
        text += "\r\n\r\nCommands:\r\n  {opt}".format(opt=self.generate_help_commands_session())
        print(text)

    def generate_help_commands_session(self):
        size = self.help_item_tabsize
        text = '\r\n  '.join([f'{n.ljust(size)}{c.description}' for n, c in self.commands.items()])
        return text







