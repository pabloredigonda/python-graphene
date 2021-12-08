from core.shared.domain.Event import Event


class AggregateRoot:
    def __init__(self):
        self.events = []  # type: List[Event]

    def record(self, event: Event):
        self.events.append(event)

    def pullDomainEvents(self):
        events = self.events
        self.events = []
        return events



