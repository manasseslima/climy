from climy import Application
from acme.commands.envcom import command as init
from acme.commands.initcom import command as env


app = Application(
    name='acme',
    title='ACME App',
    description='A teste application',
    version='0.1.0',
)
app.add_command('init', init)
app.add_command('env', env)
app.run()
