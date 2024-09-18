from typing import Iterable


class OCLTuple(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


def is_unique(lst):
    seen = []
    return not any(i in seen or seen.append(i) for i in lst)


def geta(o, attr):
    if isinstance(o, Iterable):
        return (getattr(e, attr) for e in o)
    return getattr(o, attr)


def flatten(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x
