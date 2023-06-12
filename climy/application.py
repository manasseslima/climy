import sys
from climy.command import Command
from climy.option import Option


class Application:
    def __init__(
            self,
            name: str = '',
            title: str = '',
            description: str = '',
            version: str = '0.0.0'
    ):
        self.commands: dict[str, Command] = {}
        self.options: dict[str, Option] = {}
        self.path: str = ''
        self.name = name
        self.title = title
        self.description = description
        self.version = version
        self.help_item_tabsize = 25

    def add_command(self, name: str, command: Command):
        self.commands[name] = command

    def add_option(
            self,
            name: str,
            description: str,
            *,
            short: str = '',
            variable: str = ''
    ):
        option = Option(name=name, description=description, short=short)
        option.variable = variable
        self.options[name] = option

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
        text = "\033[1m{title}\033[0m (version {version})".format(title=self.title, version=self.version)
        text += "\r\n\r\n\033[1mUsage:\033[0m\r\n  {name} <command> [options] [arguments]".format(name=self.name)
        text += self.generate_help_options_session()
        text += "\r\n\r\n\033[1mCommands:\033[0m\r\n  {opt}".format(opt=self.generate_help_commands_session())
        print(text)

    @staticmethod
    def generate_help_session(name, content):
        text = "\r\n\r\n\033[1m{name}:\033[0m{content}".format(name=name, content=content)
        return text

    def generate_help_options_session(self):
        key = '-h, --help'
        desc = 'Print this help.'
        content = '\r\n  \033[36m{key: <25}\033[0m {desc}'.format(key=key, desc=desc)
        for option in self.options.values():
            key = f'-{option.short}, --{option.name}' if option.short else f'--{option.name}'
            if option.variable:
                key += f'=[{option.variable.upper()}]'
            item = '\r\n  \033[36m{key: <25}\033[0m {desc}'.format(key=key, desc=option.description)
            content += item
        text = self.generate_help_session('Options', content=content)
        return text

    def generate_help_commands_session(self):
        size = self.help_item_tabsize
        text = '\r\n  '.join([f'\033[36m{n.ljust(size)}\033[0m {c.description}' for n, c in self.commands.items()])
        return text
