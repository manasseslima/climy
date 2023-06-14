from climy.option import Option


class Manager:
    def __init__(
            self,
            name: str,
            description: str,
            title: str = ''
    ):
        self.commands: dict[str, Manager] = {}
        self.options: dict[str, Option] = {}
        self.options_short: dict[str, str] = {}
        self.name = name
        self.title = title
        self.description = description
        self.help_item_tabsize = 25
        self.args = ''
        self.vars = []

    def add_command(
            self,
            command: 'Manager',
            *,
            name: str = ''
    ):
        name = name or command.name
        self.commands[name] = command

    def add_option(
            self,
            name: str,
            description: str,
            *,
            short: str = '',
            var_type: str = 'bool',
            var_name: str = ''
    ):
        option = Option(name=name, description=description, short=short)
        option.var_name = var_name
        option.var_type = var_type
        self.options[name] = option
        if short:
            self.options_short[short] = name

    def run(self):
        args = ''
        if not args or args[0] in ['-h', '--help', 'help']:
            text = self.generate_help()
            print(text)
            return

    def generate_help(self):
        text = ''
        text += "\r\n\r\n\033[1mUsage:\033[0m\r\n  {name} <command> [options] [arguments]".format(name=self.name)
        text += self.generate_help_options_session()
        text += "\r\n\r\n\033[1mCommands:\033[0m\r\n  {opt}".format(opt=self.generate_help_commands_session())
        return text

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
            if option.var_type != 'bool':
                var_name = option.var_name or option.name
                key += f'=[{var_name.upper()}]'
            item = '\r\n  \033[36m{key: <25}\033[0m {desc}'.format(key=key, desc=option.description)
            content += item
        text = self.generate_help_session('Options', content=content)
        return text

    def generate_help_commands_session(self):
        size = self.help_item_tabsize
        text = '\r\n  '.join([f'\033[36m{n.ljust(size)}\033[0m {c.description}' for n, c in self.commands.items()])
        return text
