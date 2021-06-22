#### Linked Lists

class Node():

    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        # return str(self.value)
        # This shows pointers as well for educational purposes:
        return "(" + str(self.value) + ", next: " + str(id(self.next)) + ")"


class Linked_list():

    def __init__(self, seq=None):
        self.next = None
        self.len = 0
        if seq != None:
            for x in seq[::-1]:
                self.add_at_start(x)

    def __repr__(self):
        out = ""
        p = self.next
        while p != None:
            out += str(p) + ", "  # str(p) envokes __repr__ of class Node
            p = p.next
        return "[" + out[:-2] + "]"

    def __len__(self):
        ''' called when using Python's len() '''
        return self.len

    def add_at_start(self, val):
        ''' add node with value val at the list head '''
        p = self
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.len += 1

    def find(self, val):
        ''' find (first) node with value val in list '''
        p = self.next
        # loc = 0     # in case we want to return the location
        while p != None:
            if p.value == val:
                return p
            else:
                p = p.next
                # loc=loc+1   # in case we want to return the location
        return None

    def __getitem__(self, loc):
        ''' called when using L[i] for reading
            return node at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        p = self.next
        for i in range(0, loc):
            p = p.next
        return p

    def __setitem__(self, loc, val):
        ''' called when using L[loc]=val for writing
            assigns val to node at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        p = self.next
        for i in range(0, loc):
            p = p.next
        p.value = val
        return None

    def insert(self, loc, val):
        ''' add node with value val after location 0<=loc<len of the list '''
        assert 0 <= loc <= len(self)
        p = self
        for i in range(0, loc):
            p = p.next
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.len += 1

    def delete(self, loc):
        ''' delete element at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        p = self
        for i in range(0, loc):
            p = p.next
        # p is the element BEFORE loc
        p.next = p.next.next
        self.len -= 1

    ###### DETECTING CYCLES IN LISTS ###########

    def detect_cycle1(self):
        s = set()  # like dict, but only keys
        p = self
        while True:
            if p == None:
                return False
            if p in s:
                return True
            s.add(p)
            p = p.next

    def detect_cycle2(self):
        """The hare moves twice as quickly as the tortoise
        Eventually they will both be inside the cycle
        and the distance between them will decrease by 1 every
        time until they meet """

        slow = fast = self
        while True:
            if slow == None or fast == None:
                return False
            elif fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
            print("lst= ", id(self), "slow= ", id(slow), "fast= ", id(fast))
            if slow is fast:
                return True

    def create_cycle(self, start, end):
        p = q = self
        assert (start < len(self) and end < len(self))
        for i in range(0, start):
            p = p.next

        for i in range(0, end):
            q = q.next
        q.next = p

    ############################################


###### END OF CLASS LINKED_LIST ############
############################################


def test1():
    lst = Linked_list()
    lst.add_at_start(3)
    lst.add_at_start(5)
    lst.insert(1, 4)
    lst.insert(2, 7)
    print(lst)
    print("length of list=", len(lst))  # calls lst.__len__()
    print(lst.__getitem__(2))
    print(lst[2])  # calls lst.__getitem__(2)
    print(lst[0])
    lst.insert(0, 9)
    print(lst.find(4))
    print(lst.find(9))
    print(lst.find(8))
    lst.delete(3)
    print(lst)
    lst[1] = 999  # calls lst.__setitem__(1,999)
    print(lst)









