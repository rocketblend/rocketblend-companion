from typing import Any, Callable, Tuple, Type

name = __name__.partition(".")[0]


def new_type(
    name: str = "object",
    default: Callable[..., Any] | None = None,
    inherent: Tuple[type, ...] = (),
    attributes: dict[str, Any] | None = None,
    **keyed_arguments: Any
) -> Type[Any]:
    if attributes is None:
        attributes = {}

    # Ensure that default is a callable appropriate for __new__
    if default is not None and callable(default):
        attributes["__new__"] = default
    else:
        # Define a standard __new__ if default is not provided or not callable
        def __new__(cls, *args, **kwargs):
            instance = super(cls, cls).__new__(cls)
            return instance

        attributes["__new__"] = __new__

    # Create the new type
    space = type(name, inherent, attributes)

    # Add any additional keyed arguments as attributes to the class
    for key, argument in keyed_arguments.items():
        setattr(space, key, argument)

    return space
