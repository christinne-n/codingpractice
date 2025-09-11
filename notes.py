""" 
.replace == replaces all occurrences of a substring with another substring
.upper == converts all characters in a string to uppercase
.lower == converts all characters in a string to lowercase
.title == converts the first character of each word to uppercase
.len == returns the length of a string (number of characters)
slices == use [start:end] to extract a substring from a string (start index is inclusive, end index is exclusive)
.find == returns the index of the first occurrence of a substring (or -1 if not found)

arithmetic operators:
+ == addition or string concatenation
- == subtraction
* == multiplication or string repetition
/ == division, returns float
// == floor division, returns integer
% == modulus, returns remainder
** == exponentiation, ex: x**y = x^y

loops:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#will loop through each item in the list

for i in range(1,5):
    print(i)
#will print numbers 1-4 (5 is excluded)

range(start[included], stop[excluding], step[optional])
for i in range(0, 10, 2):
    print(i)
#will print 0, 2, 4, 6, 8

i = 10
while i > 0:
    print(i)
    i -= 1
#will print 10 to 1
#while loops must have initialization, condition, and increment/decrement

arrays/lists:
.append() == adds an item to the end of the list
.remove() == removes the first occurrence of an item from the list
.insert(index, item) == inserts an item at a specified index
.sort() == sorts the list in ascending order
.reverse() == reverses the order of the list
.copy() == creates a copy of the list
.clear() == removes all items from the list
.pop() == removes and returns the last item from the list
.index(item) == returns the index of the first occurrence of an item (or raises an error if not found)
"""