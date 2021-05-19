

def insertNodeAtTail(head, data):
    '''new_node = SinglyLinkedListNode(data)
    current_node = head
    while current_node.next != None:
        current_node = current_node.next
    current_node.next = new_node
    return head'''
    if head is None:
        return SinglyLinkedListNode(data)
    current_node = head
    while current_node.next:
        current_node = current_node.next
    current_node.next = SinglyLinkedListNode(data)
    return head


