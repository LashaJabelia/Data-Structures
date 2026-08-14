class Queue:
    """Queue is data structure which works or principe FIFO (Firs in first out)"""

    def __init__(self, storage=None):
        if storage is not None and not isinstance(storage, list):
            raise TypeError("Storage must be a list or None")
        self.storage = [] if storage is None else storage

    def enqueue(self, item):
        """Adding item to the back"""
        self.storage.append(item)

    def dequeue(self):
        """Removing item from start"""
        if self.is_empty():
            raise IndexError("Queue is emtpy")
        
        res = self.storage.pop(0)
        return res

    def first(self):
        """Cheks what is first item"""
        if self.is_empty():
            raise IndexError("Queue is emtpy")
        
        return self.storage[0]

    def is_empty(self):
        """Checking if queue is empty"""
        if len(self.storage) == 0:
            return True
        return False

    def size(self):
        """Returns queue size"""
        return len(self.storage)

    def get_min(self):
        """Returns minimum value"""
        if self.is_empty():
            raise IndexError("Queue is empty")

        minimum = self.storage[0]

        for i in self.storage:
            if i < minimum:
                minimum = i

        return minimum
    
    def get_max(self):
        """Retruns maximum Value"""
        if self.is_empty():
            raise IndexError("Queue is empty")

        maximum = self.storage[0]

        for i in self.storage:
            if i > maximum:
                maximum = i

        return maximum

    def clear(self):
        """Clears queue"""
        self.storage.clear()

    def __str__(self):
        return str(self.storage)