class UserState(object):

    def __init__(self, replies):
        self.replies = replies
        self.reset()
        return

    def reset(self):
        self.location = ''
        self.negations = []
        self.set_next_behavior(self.greet)

    def set_next_behavior(self, behavior):
        self._next_behavior = behavior.__name__
        pass

    def run_behavior(self, message):
        message = message.strip()
        getattr(self, self._next_behavior)(message)
        pass

    def greet(self, message):
        self.reset()
        self.set_next_behavior(self.read_location)
        self.replies.ask_where()

    def read_location(self, message):
        new_location = self._parse_district(message)
        if new_location:
            self.location = new_location
            success = self._suggestions()
            if success:
                self.set_next_behavior(self.suggest_and_iterate)
            else:
                self.set_next_behavior(self.greet)
        else:
            self.replies.failed_read_location()
            self.set_next_behavior(self.read_location)

    def suggest_and_iterate(self, message):
        mnegation = self._find_negation(message)
        if mnegation:
            self.negations.append(mnegation)
        success = self._suggestions()
        if success:
            self.set_next_behavior(self.suggest_and_iterate)
        else:
            self.set_next_behavior(self.greet)

    def _suggestions(self):
        return self.replies.give_suggestions(
                self.location,
                self.negations
                )

    def _find_negation(self, message):
        if message[0:6] == 'Không ':
            return message[6:]
        return None

    @staticmethod
    def _parse_district(message):
        if message == 'q5':
            return 'Quận 5'
        elif message == 'q3':
            return 'Quận 3'
        return None

