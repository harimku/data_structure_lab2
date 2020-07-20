import pandas as pd 
from array import *
from DLinkedList import DList


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
        self.curr_size += 1
        self.ArrayListAppend(last_val)

    def ArrayListInsertAfter(self, index, newItem):
        if (self.allocationSize == self.curr_size):
            self.ArrayListResize(len(self.list) * 2)
        # move everything over by 1
        last_val = self.list[len(self.list)-1]
        for i in range(len(self.list)-1, index + 1, -1):
            self.list[i] = self.list[i - 1]
        self.list[index + 1] = newItem
        self.curr_size += 1
        # self.ArrayListAppend(last_val)

    def ArrayListSearch(self, item):
        for i in range(len(self.list)):
            if (self.list[i] == item):
                return i
        return -1
    
    def ArrayListRemoveAt(self, index):
        if (index >= 0 and index < len(self.list)):
            for i in range(index, self.curr_size-1):
                self.list[i] = self.list[i + 1]
            self.list[self.curr_size-1] = 0  #last element set to 0
    
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




class HashTable(object):

    def __init__(self, arr_size):
        if(isinstance(arr_size, float)):
            arr_size = int(arr_size)
        self.table = DynamicArray(maximum=arr_size)
        self.collisions = 0

    def getSize(self):
        return len(self.table)

    def getCollisions(self):
        return self.collisions
    
    def get(self, key):
        hash = getHash(key)
        return table[hash].getValue 
    
    def set(self, value):
        hash = getHash(value)
        element = HashElement()
        element.setKeyValue(hash, value)
        key = table[hash].getKey()
        if hash > 
        if (key > 0):
            table[hash].dll.Append(element)
            self.collisions += 1
            table[hash].used += 1
        else:
            table.ArrayListInsertAfter(hash, element)
        return None


    def getHash(self, key):
        return HashMidSquare(key)

    def HashMidSquare(key):
        squaredKey = key * key   
        lowBitsToRemove = (32 - R) / 2
        extractedBits = squaredKey >> lowBitsToRemove
        extractedBits = extractedBits & (0xFFFFFFFF >> (32 - R)) 
        return extractedBits % N





def main():   
    data = pd.read_csv("./Customer.csv") 
    # print(data)

    maximum = len(data) * 1.25
    ht = HashTable(maximum)
    

if __name__ == '__main__':
    main()