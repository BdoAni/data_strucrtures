# len(): Returns the length of an object
def python_methods():
    my_list=[1,2,3,4,5,6,7,8]
    print(len(my_list))

# append(): Adds an element to the end of a list
my_list=[1,2,3,4,5,6,7,8]
my_list.append(9)
print(my_list)

# insert(): list.insert(i, x) Inserts an element at a specified position in a list
my_list=[1,2,3,4,5,6,7,8]
my_list.insert(3,18)
print(my_list) 
# [1,2,3,18, 4,5,6,7,8]

# list.remove(x) Removes and returns the element at a specified index in a list.
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

my_list = [1, 2, 3, 4]
popped_element = my_list.pop(2)
print(popped_element)  # Output: 3
print(my_list)  # Output: [1, 2, 4]

# //
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

# list.clear()
# Remove all items from the list. Equivalent to del a[:].

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  

# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

# list.count(x)
# count(): Returns the number of occurrences of a specified element in a list.
# Return the number of times x appears in the list.
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2


# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

# list.reverse()
# reverse(): Reverses the order of elements in a list.
# Reverse the elements of the list in place.
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].


# join(): Joins the elements of a list into a string, using a specified delimiter.
my_list = ['Hello', 'World']
joined_string = ' '.join(my_list)
print(joined_string)  # Output: 'Hello World'

my_list = [1, 2, 3, 4, 5]
joined_string = ','.join(str(element) for element in my_list)
print(joined_string) 
# //#
# https://docs.python.org/3/tutorial/datastructures.html