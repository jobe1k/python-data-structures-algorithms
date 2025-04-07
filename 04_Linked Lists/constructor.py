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
    
    def prepend(self, value):
        # Create a new node with the given value
        new_node = Node(value)
        
        # If the list is empty, set head and tail to the new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        # Otherwise, set the new node's next value to the current head
        else:
            # Set the new node's next pointer to the current head
            new_node.next = self.head
            # Update the head to be the new node
            self.head = new_node

        # Increase the count of nodes in the list
        self.length += 1
        
        return True
    
    def pop_first(self):
        # If the list is empty, there's nothing to remove
        if self.length == 0:
            return None

        # Store the current head value
        temp = self.head
        # Update the head to the next node
        self.head = self.head.next
        # Disconnect the old head from the list
        temp.next = None
        # Decrease the count of nodes in the list
        self.length -= 1
        # If the list is now empty, reset tail to None
        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        # Check if the index is valid
        if index < 0 or index >= self.length:
            return None
        # Start at the head of the list
        temp = self.head
        # Loop through the list until reaching the desired index
        for _ in range(index):
            # Move to the next node
            temp = temp.next

        return temp
    
    def set_value(self, index ,value):
        # Check if the index is valid
        temp = self.get(index)
        # If the node exists, update its value
        if temp:
            # Update the value of the node at the specified index
            temp.value = value
            # Return True to indicate success
            return True
        # If the node doesn't exist, return False        
        return False
    
    def insert(self, index, value):
        # Check if the index is valid
        if index < 0 or index > self.length:
            return False
        # If the index is 0, prepend the value
        if index == 0:
            return self.prepend(value)
        # If the index is at the end, append the value
        if index == self.length:
            return self.append(value)
        # Create a new node with the given value
        new_node = Node(value)
        # Get the node at the specified index
        temp = self.get(index - 1)
        # Store the next node after the specified index
        new_node.next = temp.next
        # Link the previous node to the new node
        temp.next = new_node
        # Increase the count of nodes in the list
        self.length += 1

        return True
    
    def remove(self, index):
        # Check if the index is valid
        if index < 0 or index >= self.length:
            return None
        # If the index is 0, pop the first node
        if index == 0:
            self.pop_first()
        # If the index is the last node, pop the last node
        if index == self.length - 1:
            return self.pop()
        # Get the node before the specified index
        prev = self.get(index - 1)
        # Get the node at the specified index
        temp = prev.next
        # Link the previous node to the node after the specified index
        prev.next = temp.next
        # Disconnect the node at the specified index
        temp.next = None
        # Decrease the count of nodes in the list
        self.length -= 1

        return temp.value
    
    def reverse(self):
        # Start at the head of the list
        temp = self.head 
        # Update head to the current tail
        self.head = self.tail 
        # Update tail to the current head
        self.tail = temp 
        # Store the next node
        after = temp.next 
        # Initialize before as None
        before = None 
        # Loop through the list for the number of nodes
        for _ in range(self.length):
            # Store the next node
            after = temp.next
            # Reverse the link
            temp.next = before
            # Move before and temp one step forward
            before = temp
            # Move temp to the next node
            temp = after
         

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()

# print(my_linked_list.get(2)) # Returns 2 node 

# # (2) Item - Returns 2 node
# print(my_linked_list.pop_first())
# # (1) Items - Returns 1 node
# print(my_linked_list.pop_first())
# # (0) Items - Returns None
# print(my_linked_list.pop_first())

# print(my_linked_list.print_list())

# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())