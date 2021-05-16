

def deleteNode(llist, position):
    # Write your code here
    if position ==0:
        return llist.next
    current_index = 1
    current_node = llist
    while True:
        last_node = current_node
        current_node = current_node.next
        if current_index == position:
            last_node.next = current_node.next
            return llist
        current_index += 1


