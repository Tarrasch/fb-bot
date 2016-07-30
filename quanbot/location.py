class Location(object):

    def __init__(self, district=None):
        self.district = district

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def clone(self, **kwargs):
        cpy = Location(district=self.district)
        for k, v in kwargs.items():
            setattr(cpy, k, v)
        return cpy

    @staticmethod
    def parse_district(message):
        if message == 'q5':
            return 'Quận 5'
        elif message == 'q3':
            return 'Quận 3'
        return None

    def try_update(self, message):
        new_district = self.parse_district(message)
        if new_district:
            return self.clone(district=new_district)
        return None
