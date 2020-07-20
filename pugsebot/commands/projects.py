"""Defines projects command."""

from utils.command_base import CommandBase
from utils.request import get_json
from utils.time import UM_DIA_EM_SEGUNDOS

CACHE_EXPIRES = UM_DIA_EM_SEGUNDOS * 7

class Projects(CommandBase):
    def __init__(self):
        super().__init__(
            name='projects',
            help_text='Mostra os projetos do PUGSE no GitHub',
            reply_function_name='reply_text',
            schedule_interval=None,
            expire=CACHE_EXPIRES,
        )

    def function(self, update=None, context=None):
        """Lists all PUG-SE projects."""
        
        repo_url = 'http://api.github.com/orgs/pug-se/repos'
        text = 'Os projetos da comunidade estão no '
        text += f'<a href="{repo_url}">GitHub</a>\n\n'

        url = 'https://api.github.com/orgs/pug-se/repos'
        info_dict = get_json(url)
        i = 1
        for info in info_dict:
            name = info['name']
            description = info['description']
            url = info['html_url']
            text += f'{i}) <a href="{url}">{name}</a>: {description}\n'
            i += 1
        return text
