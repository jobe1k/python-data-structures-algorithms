# Constructor for linked list
class Node:
    def __init__(self, value):
        # Store the value of the node
        self.value = value
        # Set the next pointer to None (no connection yet)
        self.next = None

# LinkedList class manages the entire linked list
class LinkedList:
    def __init__(self, value):
        # Create the first node of the linked list
        new_node = Node(value)
        # Set the head (start) of the list to this node
        self.head = new_node
        # Set the tail (end) of the list to this node
        self.tail = new_node
        # Keep track of how many nodes are in the list
        self.length = 1
    
    def print_list(self):
        # Start at the head of the list
        temp = self.head
        # Loop through all nodes until the end
        while temp is not None:
            # Print the value of the current node
            print(temp.value)
            # Move to the next node
            temp = temp.next

    def append(self, value):
        # Create a new node with the given value
        new_node = Node(value)
        # If the list is empty, set head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Connect the current tail to the new node
            self.tail.next = new_node
            # Update the tail to be the new node
            self.tail = new_node
        # Increase the count of nodes in the list
        self.length += 1

    def pop(self):
        # If the list is empty, there's nothing to remove
        if self.length == 0:
            return None
        # Start at the head of the list
        temp = self.head
        pre = self.head
        # Move through the list until the last node
        while temp.next is not None:
            pre = temp
            temp = temp.next
        # Set the second-to-last node as the new tail
        self.tail = pre
        # Disconnect the last node
        self.tail.next = None
        # Decrease the count of nodes in the list
        self.length -= 1
        # If the list is now empty, reset head and tail to None
        if self.length == 0:
            self.head = None
            self.tail = None
        # Return the value of the removed node
        return temp.value


my_linked_list = LinkedList(1)

my_linked_list.append(2)

print(my_linked_list.print_list())

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())