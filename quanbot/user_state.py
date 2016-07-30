import quanbot.location


class UserState(object):

    static_userids = {}

    @classmethod
    def getIfNew(cls, recipient_id, replies):
        obj = cls.getIfNew_(recipient_id)
        obj.replies = replies
        return obj

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
        self.location = quanbot.location.Location()
        self.set_next_behavior(self.greet)

    def state_is_empty(self):
        return bool(self.place_filters)

    def set_next_behavior(self, behavior):
        self._next_behavior = behavior
        pass

    def run_behavior(self, message):
        message = message.strip()
        self._next_behavior(message)
        pass

    def greet(self, message):
        self.reset()
        self.set_next_behavior(self.read_location)
        self.replies.ask_where()

    def read_location(self, message):
        new_location = self.location.try_update(message)
        if new_location:
            self.location = new_location
            success = self.replies.give_suggestions(self.location)
            if success:
                self.set_next_behavior(self.suggest_and_iterate)
            else:
                self.set_next_behavior(self.greet)
        else:
            self.replies.failed_read_location()
            self.set_next_behavior(self.read_location)

    def suggest_and_iterate(self, message):
        success = self.replies.give_suggestions(self.location)
        if success:
            self.set_next_behavior(self.suggest_and_iterate)
        else:
            self.set_next_behavior(self.greet)
