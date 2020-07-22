import pandas as pd
import math 
import hashlib
from array import *
from DLinkedList import DList

class Customer():
    def __init__(self, first, last, id):
        self.first = str(first)
        self.last = str(last)
        self.id = str(id)

    def __str__(self):
        return str(self.__dict__)

class DynamicArray():
    def __init__(self, maximum=1):
        # create dynamic array 
        self.list = [0] * maximum
        self.allocationSize = maximum
        self.curr_size = 0

    def ArrayListResize(self, newAllocationSize):
        for i in range(newAllocationSize - len(self.list)):
            self.list.append(0)
        self.allocationSize = newAllocationSize

    def ArrayListAppend(self, newItem): 
        if (self.allocationSize == self.curr_size):
            self.ArrayListResize(len(self.list) * 2)
        self.list[self.curr_size] = newItem
        self.curr_size += 1

    def ArrayListPrepend(self, newItem):
        if (self.allocationSize == self.curr_size):
            self.ArrayListResize(len(self.list) * 2)
        #inserting newItem at [0]
        last_val = self.list[self.curr_size - 1]
        for i in range(self.curr_size-1, 0, -1):
            self.list[i] = self.list[i - 1]
        self.list[0] = newItem
        self.ArrayListInsertAfter(self.curr_size-1, last_val)
        self.curr_size += 1

    def ArrayListInsertAfter(self, index, newItem):
        if (self.allocationSize == self.curr_size):
            self.ArrayListResize(len(self.list) * 2)
        if(index + 1 < len(self.list)):
            if(self.list[index + 1] != 0):
                self.list[index + 1].dll.Append(newItem)
            else: 
                self.list[index + 1] = newItem
            self.curr_size += 1
        else:
            print('Index out of bounds in InsertAfter, skipping')

    def ArrayListSearch(self, item):
        for i in range(len(self.list)):
            if (self.list[i] == item):
                return i
        return -1
    
    def ArrayListRemoveAt(self, index):
        if (index >= 0 and index < len(self.list)):
            for i in range(len(self.list)-1):
                self.list[i] = self.list[i + 1]
            self.curr_size -= 1
    
    def __len__(self):
        return len(self.list)


class HashElement():

    def __init__(self):
        self.key = 0
        self.value = ''
        self.dll = DList()
        self.used = 0
    
    def HashElement(self, k=0, str='', u=0):
        self.key = k
        self.value = str
        self.used = u

    def setKeyValue(self, k, str):
        self.key = k
        self.value = str
        self.used += 1
    
    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.value

    def Append(self, element):
        self.dll.Append(element)
        self.used += 1



class HashTable(object):

    def __init__(self, arr_size):
        if(isinstance(arr_size, float)):
            arr_size = int(arr_size)
        self.maximum = arr_size
        self.table = DynamicArray(maximum=arr_size)
        self.collisions = 0

    def getSize(self):
        return self.table.curr_size

    def getCollisions(self):
        return self.collisions
    
    def get(self, key):
        return self.table.list[key]

    def getHash(self, key):
        return self.BetterHash(key)

    def HashMidSquare(self, key):
        _sum = ord(key[0]) - ord('A') + 1
        for c in range(1,len(key)):
            _sum += (ord(key[c]) - ord('a') + 1)
        squaredKey = int(_sum * _sum)
        R = (math.log(abs(_sum) / math.log(2)))
        lowBitsToRemove = int((32 - R) // 2)
        extractedBits = squaredKey >> lowBitsToRemove
        extractedBits = extractedBits & (0xFFFFFFFF >> int((32 - R)))
        return extractedBits % self.maximum

    def BetterHash(self, key):
        # python's default hash will hash to some value in range of 0 to sys.maxint
        val = hash(key)
        # compress to range between 0 to maximum
        return val % self.maximum

    def set(self, customer):
        value = customer.id.replace("-","")
        index = self.getHash(value)
        element = HashElement()
        element.setKeyValue(index, customer)
        if self.table.list[index] != 0 and self.table.list[index].getKey() > 0:
            self.table.list[index].Append(element)
            self.collisions += 1
            self.table.list[index].used += 1
        else:
            self.table.ArrayListInsertAfter(index-1, element)
        return index


def main():
    '''
    ##Test for Dynamic Array Operations
    arr = DynamicArray(6)
    print(arr.list)
    arr.ArrayListAppend(100)
    print(arr.list)
    arr.ArrayListAppend(200)
    print(arr.list)
    arr.ArrayListAppend(300)
    print(arr.list)
    arr.ArrayListAppend(400)
    print(arr.list)
    arr.ArrayListPrepend(5)
    print(arr.list)
    arr.ArrayListPrepend(1)
    print(arr.list)
    x = arr.ArrayListSearch(100)
    print(x)
    arr.ArrayListRemoveAt(0)
    print(arr.list)
    '''

    # colors
    fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
    bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"

    data = pd.read_csv("./Customer.csv", header=None)
    factor = input('Pick a factor that you would like to scale the hash table by (e.g. 1, 1.5, 1.25, etc.) : ')
    maximum = int(len(data) * float(factor))
    ht = HashTable(maximum)
    first_hash = 0
    for index,row in data.iterrows():
        cust = Customer(row[1],row[0],row[2])
        first_hash = ht.set(cust)
    
    used = 0
    for i in range(ht.maximum):
        hentry = ht.get(i)
        if (hentry != 0):
            if (hentry.getKey() > 0):
                used += 1
                if(hentry.used > 1):
                    str_out = "\n[" + str(hentry.getKey) + "]" + "\t" + str(hentry.getValue())
                    print(fg(str_out, 1))
                else:
                    str_out = "\n[" + str(hentry.getKey) + "]" + "\t" + str(hentry.getValue())
                    print(fg(str_out, 2))
        else:
            print(fg(".", 4))
    print(fg("\nStatistics:",3))
    print(fg('\tMaximum = ' + str(ht.maximum), 3))
    print(fg('\tUsed = ' + str(float(used) / float(ht.getSize() * 100.0 )) + "%", 3))
    print(fg('\tCollisions = ' + str(float(ht.getCollisions()) / float(len(data)) * 100.0) + "%", 3))
    

if __name__ == '__main__':
    main()