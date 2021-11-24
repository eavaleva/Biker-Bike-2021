from csv import DictReader
from typing import Type


def readData(location: str, objectType:Type):
    objects = []

    with open(location, 'r') as data:
        reader = DictReader(data)

        for row in reader:
            objects.append(objectType(row))

    return objects
