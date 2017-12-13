from threading import Lock
from Position import Position

class Positions(object):
    def __init__(self):
        self.dict = {}
        self.lock = Lock()

    def has_key(self, key):
        return self.dict.has_key(key)

    def get_or_create(self, symbol):
        with self.lock:
            if self.dict.has_key(symbol):
                return self.dict[symbol]
            else:
                p = Position(symbol)
                self.dict[symbol] = p
                return p

    def __str__(self):
        s = ''
        i = 0
        with self.lock:
            for key, val in self.dict.iteritems():
                s += '{}. {} {} {}\n'.format(
                    i, val.qty, key, val.dollar_value()
                )
                i = i + 1
        return s

    def __len__(self):
        return len(self.dict)
