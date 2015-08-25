# Chapter 5 Data Structures
print()

# An example that uses most of the list methods:

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.pop()
print(a)
print()

# Using lists as stacks (LIFO):

stack = [3,4,5]
print(stack)
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)
print()

# Using lists as queues (FIFO):
# It is possible to use a list as a queue, but lists are not efficient for this purpose.
# To implement a queue, use collections.deque, which was designed to have quick appends and pops from both ends.

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")     # Terry arrives
queue.append("Graham")    # Graham arrives
print(queue)              # The whole gang
queue.popleft()           # The first to arrive now leaves (Eric)
print(queue)
queue.popleft()           # The second to arrive now leaves (John)
print(queue)              # The remaining queue in order of arrival
print()


# 5.1.3 List Comprehensions
# For example, assume we want to create a list of squares, like:
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
# Note that this creates (or overwrites) a variable named x that still exists after the loop completes.
print(x)
print()
squares = []
x = "No longer exists"
#We can calculate the list of squares without any side effects using:
squares = list(map(lambda x: x**2, range(10)))
print(squares)
print(x)
print()
squares = []
# Here is something that is equivalent, but more concise and readable:
squares = [x**2 for x in range(10)]
print(squares)
print(x)
print()
"""
    A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
"""
# For example, this listcomp combines the elements of two lists if they are not equal:
my_listcomp = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(my_listcomp)
# It's equivalent to:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)
print()
# Note how the order of the for and if statements is the same in both of the above code snippets.
# If the expression is a tuple (e.g. the (x,y) in the previous example), it must be parenthesized:
vec = [-4, -2, 0, 2, 4]
print(vec)
double = [x*2 for x in vec]  # create a new list with the values doubled
print(double)
no_negative = [x for x in vec if x >= 0]  # filter the list to exclude negative numbers
print(no_negative)
my_func = [abs(x) for x in vec]  # apply a function to all of the elements
print(my_func)
# Call a method on each element:
freshfruit = ['  banana', '  loganberry', 'passion fruit']
print(freshfruit)
print([weapon.strip() for weapon in freshfruit])
# Create a list of 2-tuples like (number, square)
two_tup = [(x, x**2) for x in range(6)]
print(two_tup)
# [x, x**2 for x in range(6)] will throw a SyntaxError
# Flatten a list using a listcomp with two 'for' clauses:
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
print()

# List comprehensions can contain complex expressions and nested functions:
from math import pi
my_exp = [str(round(pi, i)) for i in range(1, 6)]
print(my_exp)
print()


# 5.1.4 Nested List Comprehensions

# The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.
# Consider the following example of a 3x4 matrix implemented as a list of three lists of length 4:
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print(matrix)
# The following list comprehension will transpose rows and columns:
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)
# As we saw in the previous section, the nested listcomp is evaluated in the context of the for that follows it,
# so the example above is equivalent to:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
# The above example is, in turn, the same as:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
# In the real world, you should prefer built-in functions to complex flow statements.
# The zip() function would do a grat job for this use case:
transposed = list(zip(*matrix))  # call with arguments unpacked from a list
print(transposed)
# What's with asterisk before matrix? See Unpacking Argument Lists.
print()


# 5.2. The del statement

# Use the del statement to remove an item from a list given its index instead of its value.
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
# del can also be used to delete entire variables:
del a
# print(a)  # NameError: name 'a' is not defined
print()


# 5.3. Tuples and Sequences

# Tuples, like lists and strings, are another example of standard sequence data types.
# A tuple consists of a number of values separated by commas, for instance:
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# Tuples are immutable:
# t[0] = 88888  # TypeError: 'tuple' object does not support item assignment
# but they can comtain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
print()
# On output, tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly.

# A special problem is the construction of tuples containing 0 or 1 items.
# Empty tuples are constructed by an empty pair of parentheses.
# A tuple with one item is constructed by following a value with a comma (instead of enclosing a single value in parentheses).
empty = ()
singleton = 'hello',  # <-- note the trailing comma
print(len(empty))
print(len(singleton))
print(singleton)
print()

# The statement  t = 12345, 54321, 'hello!'  is an example of tuple packing.
# The values 12345, 54321, and 'hello!' are packed together in a tuple.
# The reverse operation is also possible:
x, y, z = t
print(x)
print(y)
print(z)
# This is called sequence unpacking and works for any sequence on the right-hand side.
# Sequence unpacking requires that there are as many variables on the left side as there are elements in the sequence.
# x, y = t  # ValueError: too many values to unpack (expected 2)
# Multiple assignment is really just a combination of tuple packing and sequence unpacking.


# 5.4. Sets
