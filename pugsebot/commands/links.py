from utils import Command

REPLY_MESSAGE = (
    "Alguns links úteis sobre Python e o PUG-SE:\n"
    "http://se.python.org.br/\n" \
    "https://www.python.org/\n" \
    "https://wiki.python.org.br/PythonBrasil\n" \
    "https://pythonbrasil.org.br/\n"
)

class Links(Command):
    def __init__(self):
        super().__init__(
            name='links',
            help_text='Mostrar links úteis sobre Python e da PUG-SE.',
            reply_function_name='reply_text',
            schedule_interval=None,
        )

    def function(self, update=None, context=None):
        text = REPLY_MESSAGE
        return text
