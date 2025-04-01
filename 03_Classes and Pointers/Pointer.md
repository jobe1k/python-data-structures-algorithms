### Summary of Pointers in Python

- **Pointers as References**: In Python, variables store references to objects in memory, not the actual memory addresses. The Python interpreter manages memory automatically.

### Example with Immutable Objects
```python
a = 10
b = a  # b references the same object as a
b = 20  # A new object is created for b
print(a)  # Output: 10
```

- Immutable objects like integers create new objects when modified.

### Example with Mutable Objects
```python
list1 = [1, 2, 3]
list2 = list1  # list2 references the same object as list1
list2.append(4)
print(list1)  # Output: [1, 2, 3, 4]
```

- Mutable objects like lists share the same reference, so changes affect all variables pointing to the object.

### Reassigning References
```python
dict1 = {'key': 'value'}
dict2 = dict1  # dict2 references the same dictionary as dict1
dict2['key'] = 'new_value'
print(dict1['key'])  # Output: 'new_value'

dict3 = {'key': 'another_value'}
dict2 = dict3  # dict2 now references a new dictionary
print(dict1['key'])  # Output: 'new_value'
```

- Reassigning a variable to a new object changes its reference, leaving the original object unaffected.

### Garbage Collection
- When an object has no references, it becomes eligible for garbage collection, and Python's garbage collector reclaims its memory.

```python
dict1 = {'key': 'value'}
dict2 = dict1
dict2 = None  # dict2 no longer references the dictionary
# The dictionary is still accessible through dict1
dict1 = None  # Now the dictionary is eligible for garbage collection
```

- Understanding references and garbage collection helps avoid memory leaks and unintended side effects.