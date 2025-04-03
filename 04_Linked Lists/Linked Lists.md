### Linked lists
- Does not have indexes.
- While lists are in a contiguious location in memory, linked lists/nodes are spread across the memory.
- Linked list has a variable called "head" for the first item and "tail" for the last item.
- Each node points to the next node until the last node which points to None.

### Linked list and Big O
- Append a new node to the end: O(1)
- Remove an item from the end: O(n) because we had to iterate through the list
- Add item to the front: O(1)
- Removing first item: O(1)
- Adding an item to the middle: O(n) because we had to iterate through the list
- Remove and item from the middle: O(n) because we had to iterate through the list
- Look up value: O(n) because we had to iterate through the list
- Popping and item from a list and lookup by index operations are more efficient for regular lists
- Adding a value at the beginning or end of a linked list is more efficient than a regular list

### Under the hood
- "Node" is the value plus the pointer - essentially a dictionary where:
```python
head: {
    'value': x, 
    'next': 
    {'value': x, 
     'next': None}
                } : tail
```
### Additional Notes on Linked Lists
- Linked lists are dynamic in nature, meaning they can grow or shrink in size during runtime, making them suitable for scenarios where the size of the data is not known in advance.
- Types of linked lists:
    - Singly linked list: Each node points to the next node.
    - Doubly linked list: Each node points to both the next and previous nodes.
- Advantages:
    - Dynamic size: Memory is allocated as needed, avoiding the need for resizing.
    - Efficient insertions and deletions: Adding or removing elements at the beginning or middle of the list is O(1) if the node reference is known.
- Disadvantages:
    - Sequential access: Accessing an element by index requires traversing the list from the head, resulting in O(n) time complexity.
    - Overhead: Each node requires extra memory for the pointer(s).
- Use cases:
    - Frequently used in scenarios requiring frequent insertions and deletions, such as stacks, queues, or adjacency lists in graph representations.
    - Less efficient than arrays for random access due to the lack of direct indexing.
- Memory management:
    - In languages without automatic garbage collection, care must be taken to avoid memory leaks by properly deallocating nodes when they are removed.
- Big O Complexity:
    - Access by index: O(n) (sequential traversal is required).
    - Search for an element: O(n) (must traverse the list to find the element).
    - Insertion at the head: O(1) (constant time, as no traversal is needed).
    - Insertion at the tail: O(n) for singly linked lists (requires traversal), but O(1) for doubly linked lists if the tail pointer is maintained.
    - Deletion of a node: O(1) if the node reference is known, otherwise O(n) to find the node.
- Linked lists are less efficient than arrays for random access but excel in scenarios requiring dynamic resizing and frequent insertions or deletions.
