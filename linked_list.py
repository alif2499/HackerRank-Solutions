# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        
    def length(self):
        current_node = self.head
        size = 0
        while current_node.next != None:
            size += 1
            current_node = current_node.next
        return size
        
    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
    
    def get(self, index):
        if index >= self.length():
            print("ERROR--Index out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def delete(self, index):
        if index >= self.length():
            print("ERROR--Index out of range")
            return
        current_index= 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

my_list = linked_list()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()
print(my_list.get(3))
my_list.delete(3)
my_list.display()





