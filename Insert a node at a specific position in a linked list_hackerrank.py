
class Node(object):
 
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def insertNodeAtPosition(head, data, position):
    if position==0:
        head = Node(data,head)
        return head
    else:
        temp_head = head
        current_index = 1
        while True:
            if current_index == position:
                temp_head.next = Node(data,temp_head.next)
                return head
            temp_head = temp_head.next
            current_index += 1

