# Python - Set Methods

Python has a set of built-in methods that you can use on sets.

# Set Methods

| Method                       | Description                                                |
| ---------------------------- | ---------------------------------------------------------- |
| `add()`                       | Adds an element to the set                                 |
| `clear()`                     | Removes all the elements from the set                      |
| `copy()`                      | Returns a copy of the set                                  |
| `difference()`                | Returns a set containing the difference between two or more sets  |
| `difference_update()`         | Removes the items in this set that are also included in another, specified set |
| `discard()`                   | Remove the specified item                                 |
| `intersection()`              | Returns a set that is the intersection of two other sets  |
| `intersection_update()`       | Removes the items in this set that are not present in other specified set(s) |
| `isdisjoint()`                | Returns whether two sets have an intersection or not    |
| `issubset()`                  | Returns whether another set contains this set or not     |
| `issuperset()`                | Returns whether this set contains another set or not    |
| `pop()`                       | Removes an element from the set                           |
| `remove()`                    | Removes the specified element                             |
| `symmetric_difference()`      | Returns a set with the symmetric differences of two sets |
| `symmetric_difference_update()` | Inserts the symmetric differences from this set and another |
| `union()`                     | Returns a set containing the union of sets               |
| `update()`                    | Update the set with the union of this set and others     |

## Time Complexity of sets

| Operation                      | Average Case              | Worst Case                | Notes                                        |
| ------------------------------ | ------------------------- | ------------------------- | -------------------------------------------- |
| `x in s`                       | O(1)                      | O(n)                      |                                              |
| `Union s|t`                    | O(len(s)+len(t))          |                           |                                              |
| `Intersection s&t`             | O(min(len(s), len(t))     | O(len(s) * len(t))        | Replace "min" with "max" if t is not a set |
| `Multiple Intersection s1&s2&..&sn` |                         | (n-1) * O(l) where l is max(len(s1),..,len(sn)) |                                    |
| `Difference s-t`               | O(len(s))                 |                           |                                              |

## Operators for Sets

Sets and frozen sets support the following operators:

# Set Operators and Their Descriptions

| Operators      | Notes                                         |
| -------------- | --------------------------------------------- |
| `key in s`     | Containment check                              |
| `key not in s` | Non-containment check                          |
| `s1 == s2`     | s1 is equivalent to s2                         |
| `s1 != s2`     | s1 is not equivalent to s2                     |
| `s1 <= s2`     | s1 is a subset of s2                          |
| `s1 < s2`      | s1 is a proper subset of s2                   |
| `s1 >= s2`     | s1 is a superset of s2                        |
| `s1 > s2`      | s1 is a proper superset of s2                 |
| `s1 \| s2`     | The union of s1 and s2                        |
| `s1 & s2`      | The intersection of s1 and s2                 |
| `s1 - s2`      | The set of elements in s1 but not in s2       |
| `s1 ^ s2`      | The set of elements in precisely one of s1 or s2 |

## Difference between Sets and Lists in Python

Sets and lists are both data structures in Python, but they have several key differences:

1. **Ordering:**
   - Lists: Lists are ordered collections, which means the elements in a list are stored in a specific order, and you can access them by their indices (position).
   - Sets: Sets are unordered collections. The elements in a set have no specific order, and you cannot access them by their indices.

2. **Duplicates:**
   - Lists: Lists can contain duplicate elements. You can have the same value appear multiple times in a list.
   - Sets: Sets do not allow duplicate elements. If you try to add a duplicate element to a set, it will not be included.

3. **Mutability:**
   - Lists: Lists are mutable, which means you can change their contents (add, remove, or modify elements) after they are created.
   - Sets: Sets are mutable as well. You can add or remove elements from a set, but you cannot modify individual elements because they are unordered.

4. **Membership Testing:**
   - Lists: To check if an element is in a list, you typically need to iterate through the list or use the `in` keyword for membership testing, which can be slower for large lists.
   - Sets: Sets are optimized for membership testing. Checking if an element is in a set is usually very fast because of the way sets are implemented (using hash tables).

5. **Use Cases:**
   - Lists: Lists are used when you need to store an ordered collection of items, and duplicates or order matter. Lists are a good choice for sequences of data where you care about the position of each element.
   - Sets: Sets are used when you want to store a collection of unique items and don't care about their order. Sets are useful for tasks like eliminating duplicates from a list, testing membership, and performing set operations like union, intersection, and difference.

Here's a simple example to illustrate the differences:

```python
# List with duplicates and ordering
my_list = [1, 2, 3, 2, 4, 1]
print(my_list)  # Output: [1, 2, 3, 2, 4, 1]

# Set without duplicates and no specific order
my_set = {1, 2, 3, 2, 4, 1}
print(my_set)  # Output: {1, 2, 3, 4}
```

In summary, use lists when you need ordered collections with potential duplicates, and use sets when you need an unordered collection of unique elements for fast membership testing and set operations.