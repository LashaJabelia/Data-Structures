class HashTable:
    """Hash table is data structure where data is stored in key-value pairs"""

    def __init__(self, size):
        self.size = size
        self.storage = [[] for i in range(size)]

    def add(self, key, value):
        self.storage[hash(key) % self.size].append([key, value])

    def get(self, key):
        index = hash(key) % self.size
        bucket = self.storage[index]
        for i in bucket:
            if i[0] == key:
                return i[1]

        raise KeyError("Key not found")

    def remove(self, key):
        index = hash(key) % self.size
        bucket = self.storage[index]

        for i in bucket:
            if i[0] == key:
                bucket.remove(i)
                return "Key deleted"

        raise KeyError("Key not found")

    def contains(self, key):
        index = hash(key) % self.size
        bucket = self.storage[index]

        for i in bucket:
            if i[0] == key:
                return True

        return False

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.storage)