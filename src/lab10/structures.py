try:
    from src.lab10.linked import LinkedList
except ImportError:
    from linked import LinkedList

class Stack:
    def __init__(self):
        # Это создает атрибут _list при создании объекта
        self._list = LinkedList()

    def push(self, item):
        self._list.insert_at_beginning(item)

    def pop(self):
        if self.is_empty():
            return "Стек пуст"
        return self._list.remove_from_beginning()

    def is_empty(self):
        return self._list.is_empty()

class Queue:
    def __init__(self):
        self._list = LinkedList()

    def enqueue(self, item):
        self._list.insert_at_end(item)

    def dequeue(self):
        if self.is_empty():
            return "Очередь пуста"
        return self._list.remove_from_beginning()

    def is_empty(self):
        return self._list.is_empty()