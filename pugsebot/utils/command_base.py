import abc

from .cache import Cache
from .schedule import Schedule

class CommandBase():
    def __init__(
            self,
            name,
            help_text,
            reply_function_name,
            schedule_interval,
            expire=None,):
        self.name = name
        self.help_text = help_text
        self.reply_function_name = reply_function_name
        self.interval = schedule_interval
        self.expire = expire

    @abc.abstractmethod
    def function(self, update=None, context=None):
        raise NotImplementedError

    def get_result(self, update=None, context=None):
        if self.expire:
            cached_item = Cache.get_value(self.name)
            if cached_item is None:
                text = self.function(update, context)
                cached_item = Cache.set_value(
                    self.name, text,
                    self.expire,
                )
            result = cached_item.result
        else:
            result = self.function(update, context)
        return result

    def do_command(self, update=None, context=None):
        return {
            'update': update,
            'response': self.get_result(update, context),
        }

    def get_schedule(self):
        if self.interval:
            return Schedule(
                self.name + '_function',
                self.get_result,
                self.reply_function_name,
                self.interval,
            )
        return None
