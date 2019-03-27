"""
We have to insert, remove and getRandom in O(1).
For first two operations hashmap is a perfect candidate.
For getRandom, use an array to save the values.

for every insert, check if element is already there in the array.
If not there, then append the element to the the end of the list
and save the element as key and index as value in the hashmap.

For remove, check if the element is there in the hashmap.
If yes, then get the index of the element from tha hashmap, pop the element from the hashmap
copy the last element in the array to the index and save the last element's new index in the hashmap

For getRandom, generate a random number between 0 to len(array) - 1 and return element at that index.
"""

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = {}
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.set:
            return False

        self.values.append(val)
        self.set[val] = len(self.values) - 1

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val not in self.set:
            return False

        index = self.set[val]
        del self.set[val]

        lastValue = self.values[-1]

        if lastValue != val:
            self.values[index] = lastValue
            self.set[lastValue] = index

        self.values.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.values[random.randint(0, len(self.values) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()