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
    def __init__(self, capacity=15):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size =  0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # V1
        return hash(key)
        # V2
        # hashsum=0
        # for i,char in enumerate(key):
        #     hashsum += (i+len(key))**ord(char)

        # return hashsum


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
        
        # Get Key
        index = self._hash_mod(key)
        # Get 'head' node on that key
        node = self.storage[index]
        
        if node is None:
            # Make head node w/ linked pair
            self.storage[index] = LinkedPair(key,value)
            self.size +=1
            return

        else: 
            if node.key == key:
                node.value = value
                print('value', value)
                return
            while node.next is not None:
                node = node.next
                if node.key == key: 
                    node.value = value
                    return
        node.next = LinkedPair(key, value)
        self.size += 1

        # # Get to the end of the linked chain on this hashed key value
        # while node is not None:
        #     # update prev node to this node
        #     prev=node
        #     # update the current node to the next node in the LinkedPair chain
        #     node = node.next
        # # You have found the last node
        # # go back to the prev node and set the next to a new linked pair
        # prev.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Get hashed key
        idx = self._hash_mod(key)
        # Get current node @ hashed index
        current = self.storage[idx]
        
        # key == empty
        if current is None:
            print('current', current)
            return current
        
        # Key matches
        if current.key == key:
            self.storage[idx] = current.next
            print('current.next', current.next)
            return
        # get next node
        new_node = current.next

        # check for key
        while new_node is not None:
            if new_node.key == key:
                current.next = new_node.next
                print('current.next', current.next)
                return
            current = new_node
            new_node = new_node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Find the hashed key you are looking for
        index = self._hash_mod(key)
        # Get the 'head' node on that LinkedPair chain
        node= self.storage[index]

        # Traverse the chain until you find the value yopu are looking for
        while node is not None and node.key != key:
            print(f'NodeValue: {node.value}')
            node=node.next

        if node is None:
            print(f'Node not found')
            return None
        else:
            print(f'WE FOUND IT!')
            print(f'Node.Value: {node.value}')
            return node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        for x in range(self.capacity):
            self.storage.append(None)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
