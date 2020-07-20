"""Defines say command."""

from utils.command_base import CommandBase

class Say(CommandBase):
    def __init__(self):
        super().__init__(
            name='say',
            help_text='Broadcast de mensagens',
            reply_function_name='send_text',
            schedule_interval=None,
        )

    def function(self, update=None, context=None):
        """Forwards a message to the group 
            defined at utils.environment.TARGET_CHAT_ID."""
            
        text = ''
        if update:
            text = update.message.text.replace(
                '/say ', ''
            ).strip()
        return text
