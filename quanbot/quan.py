import json
from random import shuffle


class Quan(object):

    @classmethod
    def load_all_qds(cls):
        with open('data/quans.json') as data_file:
            return json.load(data_file)['list']

    @classmethod
    def get_all_qds(cls):
        return cls.load_all_qds()

    @classmethod
    def search(cls, location):
        candidates = [qd for qd in cls.get_all_qds()
                      if cls.matches(qd, location)]
        shuffle(candidates)
        return candidates[0:2]

    @classmethod
    def matches(cls, qd, location):
        return location.district in qd['address']
