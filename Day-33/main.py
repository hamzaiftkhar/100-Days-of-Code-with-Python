# Examples of set methods described in readme file

# Set methods
# add() - Adds an element to the set
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days.add("Holiday")
print(days)
#Output: {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Holiday'}


# clear() - Removes all the elements from the set
days.clear()
print(days)
#Output: set()


# copy() - Returns a copy of the set
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = days.copy()
print(days_copy)
#Output: {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}


# difference() - Returns a set containing the difference between two or more sets
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
print(days.difference(days_copy))
#Output: {'Saturday', 'Sunday'}


# difference_update() - Removes the items in this set that are also included in another, specified set
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
days.difference_update(days_copy)
print(days)
#Output: {'Saturday', 'Sunday'}


# discard() - Remove the specified item
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days.discard("Monday")
print(days)
#Output: {'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}


# intersection() - Returns a set, that is the intersection of two other sets
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
print(days.intersection(days_copy))
#Output: {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}

# intersection_update() - Removes the items in this set that are not present in other, specified set(s)
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
days.intersection_update(days_copy)
print(days)
#Output: {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}


# isdisjoint() - Returns whether two sets have a intersection or not
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
print(days.isdisjoint(days_copy))
#Output: False


# issubset() - Returns whether another set contains this set or not
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
print(days_copy.issubset(days))
#Output: True


# issuperset() - Returns whether this set contains another set or not
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
print(days.issuperset(days_copy))
#Output: True


# pop() - Removes an element from the set
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days.pop()
print(days)
#Output: {'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}


# remove() - Removes the specified element
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days.remove("Monday")
print(days)
#Output: {'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}


# symmetric_difference() - Returns a set with the symmetric differences of two sets
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
print(days.symmetric_difference(days_copy))
#Output: {'Saturday', 'Sunday'}


# symmetric_difference_update() - inserts the symmetric differences from this set and another
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
days.symmetric_difference_update(days_copy)
print(days)
#Output: {'Saturday', 'Sunday'}


# union() - Return a set containing the union of sets
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
print(days.union(days_copy))
#Output: {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}


# update() - Update the set with the union of this set and others
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
days_copy = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
days.update(days_copy)
print(days)
#Output: {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}


# len() - Returns the length of the set
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(len(days))
#Output: 7


# max() - Returns the largest item in the set
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(max(days))
#Output: Wednesday


# min() - Returns the smallest item in the set
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(min(days))
#Output: Friday


# sum() - Returns the sum of all elements in the set
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(sum(days))
#Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'


# sorted() - Returns a sorted list of the specified set
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(sorted(days))
#Output: ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']


# any() - Returns True if any element of an iterable is true. If not, any() returns False
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(any(days))
#Output: True


# all() - Returns True if all elements of an iterable are true. If not, all() returns False
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(all(days))
#Output: True


# enumerate() - Takes a collection (e.g. a tuple) and returns it as an enumerate object
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(enumerate(days))
#Output: <enumerate object at 0x000001F2F9F4F8C0>


# filter() - Use a filter function to exclude items in an iterable object
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(filter(days))
#Output: <filter object at 0x000001F2F9F4F8C0>


# iter() - Returns an iterator object
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(iter(days))
#Output: <set_iterator object at 0x000001F2F9F4F8C0>


# list() - Returns a list
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(list(days))
#Output: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# tuple() - Returns a tuple
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(tuple(days))
#Output: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')