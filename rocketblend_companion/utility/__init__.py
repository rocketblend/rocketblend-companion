name = __name__.partition(".")[0]


def new_type(name="object", default=None, inherent=(), attribute={}, **keyed_argument):
    space = type(name, inherent, attribute)
    space.__new__ = default if default else lambda self: self

    for key, argument in keyed_argument.items():
        setattr(space, key, argument)

    return space
