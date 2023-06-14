from climy import Application
from acme.commands.envcom import command as init
from acme.commands.initcom import command as env


app = Application(
    name='acme',
    title='ACME App',
    description='A teste application',
    version='0.1.0',
)
app.add_command(init)
app.add_command(env)
app.add_option('host', 'The server allow host IP number.', short='t', var_type='str')
app.add_option('port', 'Service port.', short='p', var_type='int')
app.add_option('path', 'Execution code path.', var_type='str', var_name='path')
app.run()
