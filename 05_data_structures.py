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

# List Comprehensions
