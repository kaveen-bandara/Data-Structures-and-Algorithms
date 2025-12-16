class Array:
    
    # Initializes items if they exist, else create empty list
    def __init__(self, items=None):
        self.items = items if items is not None else []

    # Travese and print each item in list
    def traverse(self):
        for item in self.items:
            print(item)

    # Access an item in a specific index if index is within range
    def access_item(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        raise IndexError(f"Index:{index} out of range")
    
    # Insert item to a specific index if index is within range
    def insertion(self, index, item):
        if index < 0 or index > len(self.items):
            raise IndexError(f"Index:{index} out of range")
        self.items.append(None)
        for i in range(len(self.items) - 1, index, -1):
            self.items[i] = self.items[i - 1]
        self.items[index] = item
        return self.items
    
    # Delete item in a specific index if index is within range
    def deletion(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError(f"Index:{index} out of range")
        for i in range(index, len(self.items) - 1):
            self.items[i] = self.items[i + 1]
        self.items.pop()
        return self.items
    
    # Sort values in ascending order using bubble sort
    def bubble_sort(self):
        for n in range(len(self.items) - 1, 0, -1):
            swapped = False
            for i in range(n):
                if self.items[i] > self.items[i + 1]:
                    self.items[i], self.items[i + 1] = self.items[i + 1], self.items[i]
                    swapped = True
            if not swapped:
                break
        return self.items
    
    # Search for a specific item in the list using linear search and return its index
    def linear_search(self, item):
        for index, value in enumerate(self.items):
            if value == item:
                return index
        return -1

    # Search for a specific item in the list using binary search and return its index
    def binary_search(self, item):
        arr = sorted(self.items)
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == item:
                return mid
            elif arr[mid] < item:
                left = mid + 1
            else:
                right = mid -1
        return -1
    
    # Update index with a new item if index is within range
    def update(self, index, item):
        if 0 <= index < len(self.items):
            self.items[index] = item
            return self.items
        raise IndexError(f"Index:{index} out of range")
    
    # Return an iterable of the items
    def __iter__(self):
        return iter(self.items)

lst = Array([2, 11, [4, 8]])
lst.insertion(0, [1, 2, 3])
lst.deletion(2)
lst.update(2, [3, 5])
print(lst.access_item(1))
lst.traverse()
print(list(lst))

l = Array([1, 7, 2, 6, 4, 3, 9, 5, 8])
print(l.linear_search(11))
print(l.bubble_sort())
print(l.binary_search(7))