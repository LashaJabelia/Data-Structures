class ListNode:
    """Node for linked list which has reference to next node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        cur = self.head

        while cur.next:
            cur = cur.next

        if self.is_empty():
            self.head = ListNode(value)
        else:
            cur.next = ListNode(value)

    def prepend(self, value):
        cur = self.head

        if self.is_empty():
            self.head = ListNode(value)

        new = ListNode(value)
        new.next = cur
        self.head = new

    def insert(self, index, value):
        cur = self.head

        if self.size() < index:
            raise IndexError("Index is greater than size")

        for i in range(index - 1):
            cur = cur.next

        buffer = cur.next
        
        cur.next = ListNode(value)
        cur = cur.next
        cur.next = buffer

    def remove_at(self, index):
        cur = self.head
        
        if self.size() < index:
            raise IndexError("Index is greater than size")

        for i in range(index - 1):
            cur = cur.next

        cur.next = cur.next.next

    def find(self, value):
        cur = self.head
        counter = 0

        while cur.next:
            if cur.val == value:
                return counter
            counter += 1
            cur = cur.next
        
    def size(self):
        cur = self.head
        counter = 1

        if self.is_empty():
            return 0

        while cur.next:
            counter += 1
            cur = cur.next

        return counter
    
    def is_empty(self):
        if self.head == None:
            return True
        return False

    def __str__(self):
        cur = self.head

        res = []
        while True:
            if self.is_empty():
                return ""
            
            res.append(cur.val)
            if not cur.next:
                break
            cur = cur.next

        return str(res)