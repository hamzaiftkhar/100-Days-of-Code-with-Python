# Examples of Lists methods in Python

#append() - Adds an element at the end of the list
# Adds List Element as value of List.
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)
#output: ['Mathematics', 'chemistry', 1997, 2000, 20544]

#copy() - Returns a copy of the list
List = ['Mathematics', 'chemistry', 1997, 2000]
List1 = List.copy()
print(List1)
#output: ['Mathematics', 'chemistry', 1997, 2000]

#count() - Returns the number of elements with the specified value
List = [1, 2, 3, 4, 5, 1, 1, 1]
print(List.count(1))    #count number of 1 in the list
#output: 4

#clear() - Removes all the elements from the list
List = [1, 2, 3, 4, 5, 1, 1, 1]
List.clear()
print(List)
#output: []

#extend() - Add the elements of a list (or any iterable), to the end of the current list
List = [1,2,3,4]
List1 = [5,6,7,8]
List.extend(List1)
print(List)
#output: [1, 2, 3, 4, 5, 6, 7, 8]

#index() - Returns the index of the first element with the specified value
List = [1,2,3,4,5,6,7,8,9,10]
print(List.index(5))
#output: 4

#insert() - Adds an element at the specified position
List = [1,2,3,4,5,6,7,8,9,10]
List.insert(5, 11)
print(List)
#output: [1, 2, 3, 4, 5, 11, 6, 7, 8, 9, 10]

#pop() - Removes the element at the specified position
List = [1,2,3,4,5,6,7,8,9,10]
List.pop(5)  #pop 6th element
print(List)
#output: [1, 2, 3, 4, 5, 7, 8, 9, 10]

#remove() - Removes the first item with the specified value
List = [1,2,3,4,5,6,7,8,9,10]
List.remove(5)
print(List) #remove 5 from the list
#output: [1, 2, 3, 4, 6, 7, 8, 9, 10]

#reverse() - Reverses the order of the list
List = [1,2,3,4,5,6,7,8,9,10]
List.reverse()
print(List)
#output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#sort() - Sorts the list
List = [5,2,8,4,1,6,7,10,9,3]
List.sort()
print(List)
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#min() - Returns the minimum value of the list
List = [5,2,8,4,1,6,7,10,9,3]
print(min(List))
#output: 1

#max() - Returns the maximum value of the list
List = [5,2,8,4,1,6,7,10,9,3]
print(max(List))
#output: 10