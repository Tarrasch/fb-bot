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
    def search(cls, location, negations):
        candidates = [qd for qd in cls.get_all_qds()
                      if cls.matches(qd, location, negations)]
        shuffle(candidates)
        return candidates[0:3]

    @classmethod
    def matches(cls, qd, location, negations):
        return (location in qd['address']
                and qd['maindish'] not in negations)
