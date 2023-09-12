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