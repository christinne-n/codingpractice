#.replace == replaces all occurrences of a substring with another substring
#.upper == converts all characters in a string to uppercase
#.lower == converts all characters in a string to lowercase
#.len == returns the length of a string (number of characters)
#multiline strings == use triple quotes (''' or """) to create strings that span multiple lines
#slices == use [start:end] to extract a substring from a string (start index is inclusive, end index is exclusive)

full_name = "John Doe"
print(full_name.replace("John", "Jane"))  # Output: Jane Doe
print("What is your name?")
my_name=input()
print("Hello " + my_name)
print(my_name[4])
print(my_name[0:3])