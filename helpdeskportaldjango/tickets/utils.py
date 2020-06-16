from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)

    def __eq__(self, other):
        return str(self).lower() == str(other).lower()

    def __str__(self):
        return '%s' % self.name


def mul(a, b):
    return a * b
