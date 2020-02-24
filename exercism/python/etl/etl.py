# https://exercism.io/my/solutions/18c9c2b906624be88d7795c0da207542


def transform(legacy_data):
    new_data = dict()
    for k, v_lst in legacy_data.items():
        new_data.update({v.lower(): k for v in v_lst})
    return new_data
