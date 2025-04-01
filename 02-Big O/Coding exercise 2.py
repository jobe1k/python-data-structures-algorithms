# def print_items(n):
#     for i in range(n):
#         print(i)
    
#     for j in range(n):
#         print(j)

# print_items(10)

# This function ran 2 times n+n which is 2n.
# The time complexity is O(n) because we ignore the constant factor (2 in this case).

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)

# print_items(10)

# This function has a time complexity of O(n^2) because it has two nested loops.
# The time it takes to run the function increases quadratically with the number of items.

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)
    
#     for k in range(n):
#         print(k)

# print_items(10)

# First for loop ran O(n^2) and the second for loop ran O(n).
# The overall time complexity is O(n^2 + n).
# When n is large, the n^2 term dominates, so we can simplify it to O(n^2).

# def add_items(n):
#     return n + n

# This function has a time complexity of O(1) because it performs a constant number of operations regardless of the size of n.
# The time it takes to run the function does not depend on the size of n.

# O(log n)