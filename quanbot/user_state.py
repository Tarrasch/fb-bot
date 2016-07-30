class UserState(object):

    static_userids = {}

    @classmethod
    def getIfNew(cls, recipient_id, replies):
        obj = cls.getIfNew_(recipient_id)
        obj.replies = replies

    @classmethod
    def getIfNew_(cls, recipient_id):
        if recipient_id in cls.static_userids:
            return cls.static_userids[recipient_id]
        cls.static_userids[recipient_id] = UserState(recipient_id)
        return cls.static_userids[recipient_id]

    def __init__(self, recipient_id):
        self.reset()
        return

    def reset(self):
        self.place_filters = {}
        self.set_next_behavior(self.greet)

    def state_is_empty(self):
        return bool(self.place_filters)

    def set_next_behavior(self, behavior):
        self._next_behavior = behavior
        pass

    def run_behavior(self, message):
        self._next_behavior(message)
        pass

    def greet(self, message):
        self.set_next_behavior(self.read_location)
        self.ask_where()

    def read_location(self, message):
        return self.greet(message)
