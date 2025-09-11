"""full_name = "John Doe"
print(full_name.replace("John", "Jane"))  # Output: Jane Doe
print("What is your name?")
my_name = input()
print("Hello " + my_name)
print(my_name[4])
print(my_name[0:3])
birth_year = int(input("Enter your birth year: ")) #takes input and converts to integer
print("your birth year is " + str(birth_year)) #converts integer to string for concatenation


is_hot = False
is_cold = True

if is_hot:
 print("hot day")
elif is_cold:
 print("cold day")
else:
 print("beautiful day") 
 

i = 1
while i < 5:
    print(i)
    i += 1
    
for i in range(1, 10, 2):
    print(i)
    
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[-1])
numbers.append(6)
numbers.insert(0, 0)
print(numbers)

customer = { #must use :
    "name" : "John Smith", #key:value
    "age" : 30,
    "verified" : True
}
print(customer["name"])
print(customer["age"])
customer["name"] = "Jane Smith" #updates value 
print(customer["name"])

def greet_user(first_name, last_name): #parameters
    print("Hi " + first_name + " " + last_name)
greet_user("John", "Smith") #arguments

def add_numbers(a, b):
    return a + b  # send result back

result = add_numbers(5, 3)
print(result) #8"""

try:
 age = int(input('Age: '))
 income = 20000
 risk = income / age
 print(age)
 print(risk)
except ValueError:
 print('Not a valid number')
except ZeroDivisionError:
 print('Age cannot be 0')