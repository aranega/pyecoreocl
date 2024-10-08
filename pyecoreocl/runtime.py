from typing import Iterable


class OCLTuple(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


def is_unique(lst):
    seen = []
    return not any(i in seen or seen.append(i) for i in lst)


def geta(o, attr):
    if isinstance(o, Iterable) and not isinstance(o, (str, bytes)):
        return (getattr(e, attr) for e in o)
    return getattr(o, attr)


def flatten(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


def closure(source, body):
    def recurse(source, acc):
        for element in source:
            if element in acc:
                yield from acc
            else:
                result = body(element)
                if result is None:
                    yield from acc
                elif isinstance(result, Iterable):
                    acc.extend(r for r in result if r not in acc)
                    yield from acc
                    yield from (
                        r for r in flatten(recurse(result, acc)) if r not in acc
                    )
                else:
                    if result not in acc:
                        acc.append(result)
                    yield from acc
                    yield from (
                        r for r in flatten(recurse([result], acc)) if r not in acc
                    )

    return recurse(source, [])
