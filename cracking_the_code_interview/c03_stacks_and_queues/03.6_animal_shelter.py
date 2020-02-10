# Problem: Animal Shelter
# An animal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest" (based on
# arrival time) of all animals at the shelter, or they can select whether they
# would prefer a dog or a cat (and will receive the oldest animal of that
# type). They cannot select which specific animal they would like. Create the
# data structures to maintain this system and implement operations such as
# enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in
# Linked list data structure.

from itertools import count
from c03_stacks_and_queues.queue import Queue


class Shelter():
    def __init__(self):
        self._dogs = Queue()
        self._cats = Queue()
        self._counter = count()

    def enqueue_dog(self, dog):
        self._dogs.add((dog, next(self._counter)))
        return self

    def enqueue_cat(self, cat):
        self._cats.add((cat, next(self._counter)))
        return self

    def dequeue_dog(self):
        if self._dogs.is_empty():
            raise EmptyShelter('There are no dogs.')
        dog, _ = self._dogs.remove()
        return dog

    def dequeue_cat(self):
        if self._cats.is_empty():
            raise EmptyShelter('There are no cats.')
        cat, _ = self._cats.remove()
        return cat

    def dequeue_any(self):
        if self.is_empty():
            raise EmptyShelter('There are no animals.')
        elif self._dogs.is_empty():
            return self.dequeue_cat()
        elif self._cats.is_empty():
            return self.dequeue_dog()

        dog, count_dog = self._dogs.peek()
        cat, count_cat = self._cats.peek()
        if count_dog < count_cat:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def is_empty(self):
        return self._dogs.is_empty() and self._cats.is_empty()

    def __repr__(self):
        return f'dogs: {repr(self._dogs)}\ncats: {repr(self._cats)}'


class EmptyShelter(Exception):
    pass
