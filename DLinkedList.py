import random

__all__ = [
    'Node',
    'DList'
    ]

# node definition
class Node:
    def __init__(self):
        self.data = None
        self.previous = None
        # introduce a 'next' node for doubly linked list
        self.next = None
    def get(self):
        return self.data
    def getPrev(self):
        return self.previous
    def getNext(self):
        return self.next
    def setPrev(self,previous):
        self.previous = previous
    def setNext(self, new_next):
        self.next = new_next
    def set(self,data):
        self.data = data
    node = property(get,set)
    prev = property(getPrev,setPrev)
    next = property(getNext, setNext)

class DList:
    def __init__(self):
        self.tail = None
        # introduce 'head' node for double link
        self.head = None

    # appends to tail of list
    def Append(self,data):
        pdata = Node()
        pdata.node = data
        if (self.tail == None):
            self.tail = pdata
            if (self.head is None):
                self.head = pdata
            elif(self.head is not None):
                self.head.next = self.tail
                self.tail.prev = self.head
        else:
            # tail exists
            if (self.head is not None):
                self.tail.next = pdata
            pdata.prev = self.tail
            self.tail = pdata

    # prepends to head of list
    def Prepend(self,data):
        pdata = Node()
        pdata.node = data
        if (self.head == None):
            self.head = pdata         
        else:
            self.head.prev = pdata
            pdata.next = self.head
            self.head = pdata

    # inserts data after found data
    def InsertAfter(self, find, data):
        if find is None:
            return None
        if not isinstance(find, int):
            print('Find argument must be int')

        pdata = Node()
        pdata.node = data

        # look for find
        if(self.tail.node == find):
            self.tail.next = pdata
            pdata.prev = self.tail
            self.tail = pdata
            return pdata

        runner = self.tail
        while(runner):
            if runner.prev is not None and runner.prev.node is not None and runner.prev.node == find:
                break
            runner = runner.prev
        if runner is None:
            return None

        runner.prev.next = pdata
        pdata.prev = runner.prev
        pdata.next = runner
        runner.prev = pdata
        return pdata

    # inserts data before found data
    def InsertBefore(self, find, data):
        if find is None:
            return None
        if not isinstance(find, int):
            print('Find argument must be int')

        pdata = Node()
        pdata.node = data

        # look for find
        if(self.head.node == find):
            self.head.prev = pdata
            pdata.next = self.head
            self.head = pdata
            return pdata

        runner = self.tail
        while(runner):
            if runner.prev is not None and runner.node == find:
                break
            runner = runner.prev

        if runner is None:
            return None
        
        pdata.prev = runner.prev
        runner.prev = pdata
        pdata.prev.next = pdata
        pdata.next = runner
        return pdata
            
    # finds data node and returns it
    def Search(self,data):
        runner = self.tail
        while(runner):
            if runner.node == data:
                break 
            runner = runner.prev
        if runner is None:
            print('There is no such element in the list')
            return None
        if (runner):
            return runner
        else: 
            return None
                
    # deletes a node from the list
    def Delete(self,data):
        if (self.head == None):
            print('There is no element to delete')
            return None
        if (self.head.node == data):
            if(self.head == self.tail):
                self.tail = None
                self.head = None
                return None
            self.head = self.head.next
            if(self.head is None):
                return None
            self.head.prev = None
            return None

        runner = self.head
        while(runner):
            if runner.next is not None and runner.next.node is not None and runner.next.node == data:
                break 
            runner = runner.next
        if runner is None:
            print('There is no such element in the list.')
            return None
        if (runner.next == self.tail):
            self.tail = runner
            self.tail.next = None
        else:
            runner.next = runner.next.next
            runner.next.prev = runner

    # returns number of nodes in list
    def Count(self):
        temp = self.tail
        count = 0
        while (temp): 
            count += 1
            temp = temp.prev
        return count 

    # returns true if list is empty
    def IsEmpty(self):
        if(self.head is None and self.tail is None):
            return True
        else:
            return False

    # prints list from tail of list
    def Output(self):
        rover = self.tail
        count = 0

        while (rover != None):
            if rover.next is None:
                next_out = 'NULL'
            else:
                next_out = str(rover.next.node)
            if rover.prev is None:
                prev_out = 'NULL'
            else:
                prev_out = str(rover.prev.node)
            
            print('Node {} : data={}, prev_data={}, next_data={}'.format(str(count), str(rover.node), prev_out, next_out))
            count += 1
            rover = rover.prev
        
        if count == 0:
            print('<Empty List>')

    # for printing Radix Sort output
    def output(self):
        rover = self.head
        count = 0

        while (rover != None):  
            print('Node {} : data={}'.format(str(count), str(rover.node)))
            count += 1
            rover = rover.next
        

 

def main():       
    # Automated Test
    print('=============== Doubly Linked List Implementation ===============')
    print('Operation: Creating List')
    dll = DList()
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: Append({})'.format(str(1)))
    print('Operation: Append({})'.format(str(2)))
    print('Operation: Append({})'.format(str(3)))
    print('Operation: Append({})'.format(str(3)))
    print('Operation: Append({})'.format(str(3)))
    dll.Append(1)
    dll.Append(2)
    dll.Append(3)
    dll.Append(3)
    dll.Append(3)
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: Prepend({})'.format(str(0)))
    dll.Prepend(0)
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: InsertAfter({},{})'.format(str(1),str(-1841)))
    dll.InsertAfter(1,-1841)
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: InsertBefore({},{})'.format(str(1),str(-777)))
    dll.InsertBefore(1,-777)
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: Delete({})'.format(str(777)))
    dll.Delete(-777)
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: Delete({})'.format(str(3)))
    dll.Delete(3)
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: Search({})'.format(str(-777)))
    val = dll.Search(-777)
    if val is not None:
        print('Node found with value {}'.format(str(val.node)))
    else:
        print('Node not Found')
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: Search({})'.format(str(-1841)))
    val = dll.Search(-1841)
    if val is not None:
        print('Node found with value {}'.format(str(val.node)))
    else:
        print('Node not Found')
    print('')
    print('Operation: Search({})'.format(str(99999)))
    val = dll.Search(99999)
    if val is not None:
        print('Node found with value {}'.format(str(val.node)))
    else:
        print('Node not Found')
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: IsEmpty()')
    val = dll.IsEmpty()
    if val:
        print('List is empty')
    else:
        print('List is not empty')
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: Delete(2)')
    print('Operation: Delete(3)')
    print('Operation: Delete(3)')
    print('Operation: Delete(-1841)')
    print('Operation: Delete(1)')
    print('Operation: Delete(0)')
    dll.Delete(2)
    dll.Delete(3)
    dll.Delete(3)
    dll.Delete(-1841)
    dll.Delete(1)
    dll.Delete(0)
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Operation: IsEmpty()')
    dll.IsEmpty()
    val = dll.IsEmpty()
    if val:
        print('List is empty')
    else:
        print('List is not empty')
    print('')
    print('Current List:')
    dll.Output()
    print('=================================================================')
    print('Program Finished')


if __name__ == '__main__':
    main()