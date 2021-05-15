def insertNodeAtHead(llist, data):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    new_node.next = llist
    return new_node