#########################################
### HASH FUNCTIONS EXAMPLES           ###
#########################################

def hash4int(n):
    m = 1000
    c = (5 ** 0.5 - 1) / 2  # some irrational, 0<c<1
    return int(m * ((n * c) % 1))


def hash4strings(st):
    p = 2 ** 120 + 451  # some arbitrary prime number
    s = 0
    for c in st:
        s = (128 * s + ord(c)) % p
    return s


#########################################
### CLASS HASH TABLE                  ###
#########################################

class Hashtable:

    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries, uses hash_func """

        # self.table = [[]*m]            ##bogus initialization
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda key: hash_func(key) % m

    def __repr__(self):
        return "".join([str(i) + " " + str(self.table[i]) + "\n" \
                        for i in range(len(self.table))])

    def find(self, item):
        """ returns True if item in hashtable, False otherwise  """
        i = self.hash_mod(item)
        chain = self.table[i]
        return item in chain  # a hidden loop
        ##or the long way:
        # if item in chain:
        #    return True
        # else:
        #    return False

    def insert(self, item):
        """ insert an item into table, if not there """
        i = self.hash_mod(item)
        chain = self.table[i]
        if item not in self.table[i]:  # a hidden loop
            self.table[i].append(item)

####################
#### some tests ####
####################

##tribes = ['Reuben', 'Simeon', 'Levi', 'Judah', 'Dan',
##          'Naphtali', 'Gad', 'Asher', 'Issachar', 'Zebulun',
##          'Benjamin', 'Joseph', 'Ephraim', 'Manasse']
##
##ht = Hashtable(7)
##
##for name in tribes:
##    ht.insert(name)
##
##print(ht) #calls __repr__
##
##
##ht = Hashtable(21)
##
##for name in tribes:
##    ht.insert(name)
##
##print(ht) #calls __repr__


###################################
#### hashing class Student     ####
###################################

##from student import * # Student class from an earlier lecture
# it must implement __hash__ and __eq__

##st1 = Student("Grace", "Hopper", 123456789)
##st2 = Student("Grace", "Hopper", 123456789)
##ht = Hashtable(7)
##ht.insert(st1)
##print(ht.find(st2)) #without __eq_ this will output False
