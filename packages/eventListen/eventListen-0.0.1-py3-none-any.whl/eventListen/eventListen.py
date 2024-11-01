from typing import Any, Callable

from proto import proto

with proto("Events") as Events:
    @Events
    def new(self):
        self.events = {}
        return
    
    @Events
    def observe(self, func: Callable[[], Any]):
        self.events[func.__name__] = func
        return func

    @Events
    def trigger(self, event, *args, **kwargs) -> Any:
        if event in self.events:
            return self.events[event](*args, **kwargs)
        else:
            raise NameError("Event %s not found." % event)


