# https://exercism.io/my/solutions/81280896a44f4b0a979905962a236259


def flatten(iterable):
    flattened = []
    for item in iterable:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        elif item is not None:
            flattened.append(item)
    return flattened
