from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
        except IndexError:
            raise StopIteration
        self._index += 1
        return item


class MyList(Iterable):
    def __init__(self):
        self._items: List[Any] = []

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self):
        return MyIterator(self._items)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._items})"


if __name__ == "__main__":
    my_list = MyList()
    my_list.add("Felipe")
    my_list.add("Ana")
    my_list.add("Lucas")
    print(my_list)

    for i in my_list:
        print(i)
