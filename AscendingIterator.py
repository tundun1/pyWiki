# TODO: Develop an iterator to implement a certain list in the ascending orde
from itertools import callable
class AscendingOrder(object):
    def __init__(self, List1: list):
        self.copy_list = list[List1]

    def __iter__(self):
        return AscendingOrder

    def __next__(self):
        self.minimum_number = self.min(self.copy_list)
        self.copy_list.remove(self.minimum_number)
        return self.minimum_number

list12 = [12,3,43,234,212,212,342,324,12,32,434,53,76]
ascending_order = AscendingOrder(list12)
for number in ascending_order:
    print(number)
