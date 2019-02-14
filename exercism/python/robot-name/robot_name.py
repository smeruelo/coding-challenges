from string import ascii_uppercase, digits
from random import choices


MAX_NAMES = pow(len(ascii_uppercase), 2) * pow(len(digits), 3)
existing_robots = set()


class Robot(object):
    def __init__(self):
        self.name = self.assign_name()

    def assign_name(self):
        if len(existing_robots) < MAX_NAMES:
            name = ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))
            while name in existing_robots:
                name = ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))
            existing_robots.add(name)
            self.name = name
            return name
        else:
            raise Exception("No unique names available.")

    def reset(self):
        self.name = self.assign_name()
