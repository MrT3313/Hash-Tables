# Initial Commit

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        print(f'\n-INSERT-\n')

        # Make the hashed index
        index = self._hash_mod(key)
        print(f'-*- Created Hash Index {index}')

        # Find what is at that hashed index in the hash table's storage
        curr_linkedPair = self.storage[index]
        last_linkedPair = None
        print(f'-*- Current Linked Pair {curr_linkedPair}')
        print(f'-*- Last Linked Pair {last_linkedPair}')

        # Traverse the linked value 'tree' at the hashed index => this 
        # would be accounting for colisions in which a link list is implemented
        # as the hashed index
        ## --
        # We have a PAIR at the hash index in question 
        # the KEY of ^^ is NOT the key you are looking for
        while curr_linkedPair is not None and curr_linkedPair.key != key:     
            # Increment up the LAST linked pair to the CURRENT
            last_linkedPair = curr_linkedPair
            # Increment the CURRENT linked pair to the NEXT
            curr_linkedPair = last_linkedPair.next
            print(f'-*- MOVE')


        print(f'-*- UPDATED Current Linked Pair {curr_linkedPair}')
        print(f'-*- UPDATED Last Linked Pair {last_linkedPair}')

        # you have FOUND the key that matches your 
        if curr_linkedPair is not None:
            curr_linkedPair = value 
        else:
            # make new linked pair
            new_linkedPair = LinkedPair(key, value)
            # add the rest of the chain on
            new_linkedPair.next = self.storage[index]
            self.storage[index] = new_linkedPair

        print(f'Self.Storage {self.storage}')

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Make the hashed index
        index = self._hash_mod(key)
        print(f'Created Hash Index {index}')

        # Find what is at that hashed index in the hash table's storage
        curr_pair = self.storage[index]
        print(f'Current Pair {curr_pair}')

        # Loop
        while curr_pair is not None:
            # Did you find it?
            if(curr_pair.key == key):
                return curr_pair.value
            # Increment the current pair
            curr_pair = curr_pair.next 




    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass


# ht = HashTable()

# ht.insert('test_item', 'test_value')

print(f'--this is the end--')

# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
