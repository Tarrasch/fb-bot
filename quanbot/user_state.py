
class UserState(object):

    def __init__(self):
        self.place_filters = {}
        return

    def reset(self):
        self.place_filters = {}

    def state_is_empty(self):
        return bool(self.place_filters)
