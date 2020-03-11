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
        index = self._hash_mod(key)

        #If key exists overwrite

        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key,value)          

        else:
            item = self.storage[index]
            while item:
                if item.key == key:
                    item.value = value
                    break
                elif item.next:
                    item = item.next
                else:
                    item.next = LinkedPair(key, value)
                    item = False
                
            

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            hasNext = True
            current_item = self.storage[index]

            while hasNext:
                if current_item.key == key:
                    self.storage[index] = None
                    hasNext = False
                elif current_item.next is not None:
                    current_item = current_item.next
                else:
                    hasNext = False
        else:
            print("Key not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        if self.storage[index] is None:
            return None

        bucket_item = self.storage[index]

        while bucket_item.key:
            if bucket_item.key == key:
                return bucket_item.value
            elif bucket_item.next is not None:
                bucket_item = bucket_item.next
            else:
                return None
            
    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage.copy()
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        
        for item in old_storage:
            if item is not None:
                hasNext =  True
                current_item = item
                while hasNext:
                    self.insert(current_item.key, current_item.value)

                    if current_item.next is not None:
                        current_item = current_item.next
                    else:
                        hasNext = False




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
