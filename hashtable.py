# hashtable.py

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity

    def __len__(self):
        return self.capacity