# https://exercism.io/my/solutions/2010abfcf75c4b70820e003197657991


def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError('Invalid length.')

    return [series[i:i+length] for i in range(len(series) - length + 1)]
