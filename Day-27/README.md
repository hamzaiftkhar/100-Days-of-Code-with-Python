# Operation on Tuples in Python Programming Language

As in our pervious exercise we have seen what are tuples and how to create a tuple in python programming language. Now we will see how to perform some operation on tuple.

## Manupulating Tuples

Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

### 1. Adding Items in a Tuple

You cannot add or remove items directly in the tuple, so first we convert it into a list, change the list, and convert the list back into a tuple.

```python
x = ("apple", "banana", "cherry")
y = list(x)
y.append("kiwi")
x = tuple(y)

print(x)
```

Output:

```python
('apple', 'banana', 'cherry', 'kiwi')
```

So in this way we can add items in a tuple.

### 2. Changing Items in a Tuple

Once a tuple is created, you cannot change its items, but there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```

Output:

```python
('apple', 'kiwi', 'cherry')
```

So in this way we can change items in a tuple.

### 3. Removing Items in a Tuple

**Note:** You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

```python
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
y.pop(1)
x = tuple(y)

print(x)
```

Output:

```python
('cherry',)
```

So in this way we can remove items in a tuple and pop them as well.

Or you can delete the tuple completely:

```python
x = ("apple", "banana", "cherry")
del x

print(x) #this will raise an error because the tuple no longer exists
```

### 4. Joining Two Tuples

To join two or more tuples you can use the + operator:

```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

Output:

```python
('a', 'b', 'c', 1, 2, 3)
```

### 5. Multiply Tuples

If you want to multiply the content of a tuple a given number of times, you can use the * operator:

```python
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
```

Output:

```python
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

## Loop Through a Tuple

You can loop through the tuple items by using a for loop and while loop.

```python
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```

Output:

```python
apple
banana
cherry
```

Now looping in tuple using while loop.

```python
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
```

Output:

```python
apple
banana
cherry
```

## Tuples methods

Python has two built-in methods that you can use on tuples.

### 1. count()

The count() method returns the number of times a specified value appears in the tuple.

```python
thistuple = (1, 4, 6, 8, 4, 9, 4)
x = thistuple.count(4)
print(x)
```

Output:

```python
3
```

### 2. index()

The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

```python
thistuple = (1, 4, 6, 8, 4, 9, 4)
x = thistuple.index(4)
print(x)
```

Output:

```python
1
```

Additional methods we can use on tuples are:

- len()
- max()
- min()
- sum()