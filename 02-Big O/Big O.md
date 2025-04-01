## Big O
- Big O is a way to measure how fast or how much memory an algorithm uses as the input grows. It helps compare which algorithm is better for large tasks.
- Time complexity: not measured by set time, measured in number of operations it takes to complete something 
- Space complexity: how much resource it uses to complete a task

## In Big O notation, three Greek letters are used to describe how algorithms perform:
- Ω (Omega): The best-case scenario—how fast it could be at least.
- Θ (Theta): The average-case when the best and worst are the same.
- O (Omicron): The worst-case scenario—how long it could take at most.

# Simplification techniques
## O(n) - O of n
- This function has a time complexity of O(n) because it iterates through n items.
- The time it takes to run the function increases linearly with the number of items.

```python
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)
```

## Drop constants
- This function ran 2 times n+n which is 2n.
- The time complexity is O(n) because we ignore the constant factor (2 in this case).

```python
def print_items(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print_items(10)
```

## O(n)^2
- This function has a time complexity of O(n^2) because it has two nested loops.
- The time it takes to run the function increases quadratically with the number of items.

```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)
```

## Drop non-dominants
- First for loop ran O(n^2) and the second for loop ran O(n).
- The overall time complexity is O(n^2 + n).
- When n is large, the n^2 term dominates, so we can simplify it to O(n^2).

```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for k in range(n):
        print(k)

print_items(10)
```

## O(1)
- This function has a time complexity of O(1) because it performs a constant number of operations regardless of the size of n.
- The time it takes to run the function does not depend on the size of n.
- As n increases, number of operations on n stays constant.
- Most efficient Big O.

```python
def add_items(n):
    return n + n
```

## O(log n)
- O(log n) means the time it takes to complete a task grows slowly as the input size increases. It happens when the input is repeatedly divided, like in binary search.

## Different terms for inputs
```python
def print_items(a, b):
    for i in range(a): # O(a)
        print(i)

    for j in range(b): # O(b)
        print(j)
```
- When you add O(a) + O(b) = O(a + b)

```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```
- When you multiply O(a) x O(b) = O(a x b)

## Big O of lists
```python
my_list = [11, 3, 23, 7]

my_list.append(17) # This is O(1)
my_list.pop() # This is O(1)

my_list.pop(0) # Item is removed and now the list needs to be reindex. This is O(n) - n=number of items on the list
my_list.insert(0, 11) # Item is added and now the list needs to be reindex. This is O(n) - n=number of items on the list

my_list.insert(1, 'Hi')
```
- Adding or removing from the end of a list is O(1).
- Adding or removing from the beginning of a list O(n) because reindexing needs to happen.
- Adding or removing from the middle of a list is O(n) because reindexing needs to happen.
- Looking for a value from a list is O(n).
- Looking for a value by index in a list is O(1).

## Big O when n = 100
- O(n^2) = 10_000: Loop within a loop
- O(n) = 100: Proportional
- O(log n) ~ 7: Divide and conquer
- O(1) = 1: Constant
- Spread become larger for O(n^2) as n increases: very inefficient

----------------------------------------------------------------------------------------------------------
## Key points about Big O:

### What is Big O?
- Big O measures how fast or how much memory an algorithm uses as the input size grows.
- It helps compare algorithms to determine which is better for large tasks.

## Time Complexity:
- Measured by the number of operations, not actual time.
- Describes how the runtime of an algorithm grows with input size.

## Space Complexity:
- Measures how much memory an algorithm uses to complete a task.

## Greek Letters in Big O:
- O (Omicron): Worst-case scenario (maximum time or space).
- Ω (Omega): Best-case scenario (minimum time or space).
- Θ (Theta): Average-case scenario (tight bound).

## Common Big O Notations:
- O(1): Constant time, regardless of input size (most efficient).
- O(log n): Grows slowly as input size increases (e.g., binary search).
- O(n): Linear growth, proportional to input size.
- O(n²): Quadratic growth, common with nested loops (inefficient for large inputs).

## Simplification Techniques:
- Drop Constants: Ignore constant factors (e.g., O(2n) simplifies to O(n)).
- Drop Non-Dominants: Focus on the term with the largest growth rate (e.g., O(n² + n) simplifies to O(n²)).

## Big O of Lists:
- Adding/removing at the end: O(1) (no reindexing needed).
- Adding/removing at the beginning or middle: O(n) (requires reindexing).
- Accessing by index: O(1).
- Searching for a value: O(n).

## Big O Examples:
- O(n): Iterating through a list.
- O(n²): Nested loops.
- O(log n): Divide-and-conquer algorithms like binary search. Halving input size each step.

## Big O for Input Combinations:
- Adding complexities: O(a) + O(b) = O(a + b).
- Multiplying complexities: O(a) × O(b) = O(a × b).

## Big O for n = 100:
- O(n²): 10,000 operations (inefficient for large inputs).
- O(n): 100 operations (proportional).
- O(log n): ~7 operations (efficient for large inputs).
- O(1): 1 operation (most efficient).

