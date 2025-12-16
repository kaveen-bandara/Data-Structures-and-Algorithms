class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        return self
    
    def append(self, value):
        if not self.head:
            return self.prepend(value)        
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        return self
    
    def length(self):
        count, current_node = 0, self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def insert_at_position(self, position, value):
        if position < 1:
            raise Exception(f"Position:{position} invalid")
        if position == 1:
            return self.prepend(value)
        if position > self.length():
            return self.append(value)
        count, current_node = 1, self.head
        while current_node:
            count += 1
            if count == position:
                new_node = Node(value, current_node.next)
                current_node.next = new_node
                return self
            current_node = current_node.next

    def insert_multiple_values(self, values):
        for value in values:
            self.append(value)
        return self

    def deletion(self, position):
        length = self.length()
        if position < 1:
            raise Exception(f"Position:{position} invalid")
        if position > length:
            position = length
        if position == 1:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return self        
        count = 1
        current_node = self.head
        while current_node and current_node.next:
            count += 1
            if count == position:
                to_delete = current_node.next
                current_node.next = to_delete.next
                if to_delete == self.tail:
                    self.tail = current_node
                return self
            current_node = current_node.next
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

    def find_node(self, value):
        position = 1
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return position
            current_node = current_node.next
            position += 1
        return -1
        
    def update(self, old_value, new_value):
        current_node = self.head
        updated = False
        while current_node:
            if current_node.data == old_value:
                current_node.data = new_value
                updated = True
            current_node = current_node.next
        if not updated:
            raise ValueError(f"{old_value} not found in the list")
        return self
    
    def sort(self):
        if not self.head or not self.head.next:
            return self
        def merge(a, b):
            dummy = Node()
            tail = dummy
            while a and b:
                if a.data <= b.data:
                    tail.next, a = a, a.next
                else:
                    tail.next, b = b, b.next
                tail = tail.next
            tail.next = a or b
            return dummy.next
        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid
        def merge_sort(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            return merge(merge_sort(left), merge_sort(right))
        self.head = merge_sort(self.head)
        current = self.head
        while current and current.next:
            current = current.next
        self.tail = current
        return self

    def __repr__(self):
        if not self.head:
            return "Linked list is empty"
        values = []
        current_node = self.head
        while current_node:
            values.append(repr(current_node.data))
            current_node = current_node.next
        return " -> ".join(values) + " -> None"

ll = LinkedList()
ll.prepend(2)
ll.append(4)
ll.append(5)
ll.append(3)
ll.prepend(1)
# print(ll.head)
# print(ll.tail)
# print(ll.head.next)
# print(ll.tail.next)
# print(ll.length())
#ll.insert_at_position(2, 4)
ll.deletion(2)
print(ll.head)
print(ll.tail)
#ll.insert_multiple_values([10, 11, 12, 13])
#ll.update(13, 15)
ll.sort()
print(ll)
#ll.traverse()
#print(ll.find_node(8))    
        
#     def reverse(self):
#         if not self.head or not self.head.next:
#             return self
#         else:
#             new_head = self.reverse()
#             self.head.next.next = self.head
#             self.head.next = None
#             return new_head