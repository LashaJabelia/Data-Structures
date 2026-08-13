class Stack:
    """Stack is data structure which works on principe LIFO (Last in First Out)"""
    
    def __init__(self, storage=None):
        if storage is not None and not isinstance(storage, list):
            raise TypeError("Storage must be a list or None")
        self.storage = [] if storage is None else storage

    def push(self, item):
        """Putting item on top of the stack"""
        self.storage.append(item)

    def pop(self):
        """Removing item from the top of the stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")

        poped_item = self.storage.pop()
        return poped_item
    
    def top(self):
        """Just looking what is top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.storage[-1]

    def is_empty(self):
        """Checking if stack is empty"""
        if len(self.storage) == 0:
            return True
        return False

    def size(self):
        """Returns stacks size"""
        return len(self.storage)

    def get_min(self):
        """Returns minimum value"""
        if self.is_empty():
            raise IndexError("Stack is empty")

        minimum = self.storage[0]

        for i in self.storage:
            if i < minimum:
                minimum = i

        return minimum

    def get_max(self):
        """Retruns maximum Value"""
        if self.is_empty():
            raise IndexError("Stack is empty")

        maximum = self.storage[0]

        for i in self.storage:
            if i > maximum:
                maximum = i

        return maximum

    def clear(self):
        """Clears stack"""
        self.storage.clear()

    def __str__(self):
        return str(self.storage)