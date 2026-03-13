#Simple Interest Calculator
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = 10000
r = 10
t = 1
print(simple_interest(p, r, t))#Centigrade to Fahrenheit Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

c = 41
print(celsius_to_fahrenheit(c))#Swapping two numbers
a = 5
b = 10
print("Before swapping: a =", a, "b =", b)
# a, b = b, a
# print("After swapping: a =", a, "b =", b)
a= a+b
b= a-b
a= a-b
print("After swapping: a =", a, "b =", b)#Height of user in feet and convert into centimeters and inches
def convert_height(feet):
    centimeters = feet * 30.48
    inches = feet * 12
    return centimeters, inches


h = float(input("Enter your height in feet: ")) 
cm, inc = convert_height(h)
print("Height in centimeters:", cm)
print("Height in inches:", inc)#Reverse the number and string
num = 1234567
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed number:", rev)

# num = 123
# print(num)
# a = num % 10
# num = num // 10
# b = num % 10
# c = num // 10
# rev = a * 100 + b * 10 + c
# print("Reversed number:", rev)# Python Data Collection (List)
mylist = ["prashant", "sachin", "satyarth", "pratik", 77, 66.05, True, False]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[-1])
print(mylist[2:5])
print(mylist[2:])
print(mylist[:5])
print(mylist[:])
print(mylist[1:8:2])
print(mylist[::-1])
mylist.append("harsh")
mylist.append("satyarth")
mylist.insert(2, "pratik")
mylist.insert(1, "sanket")
print(mylist)
mylist.remove("pratik")
print(mylist)
newlist = mylist.copy()
print(newlist)
print(mylist)
print("Id of mylist:", id(mylist))
print("Id of newlist:", id(newlist))
mylist = [['prashant', 'sachin', 'satyarth', 'pratik'], [77, 66.05, True, False], ['python', 'java', 'c++']]
print("example of nested list:", mylist)
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[1][1])
print(mylist[2][0])
print(mylist[2][1])
print(mylist[2][2])
list1 = ["prashant", "sachin", "satyarth", "pratik"]
print(list1*2)
list2 = [5435, 6546, 6546, 6546, 6546]
print(list1 + list2)
del list1[2]
del list2
print(list1)
list2 = [5435, 6546, 6546, 6546, 6546]
list2.clear()
print(list2)
nyname = "prashant"
mylist = list(nyname)
print(mylist)
mylist = [875689, 783564, 982349, 23623, 87364587, 655446, 23]
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
math = 10
phy = 10
print(id(phy))
print(id(math))
mylist = [875689, 783564, 982349, 23623, 87364587, 655446, 23]
newlist = mylist
print("Id of mylist:", id(mylist))
print("Id of newlist:", id(newlist))# Python Basics: Input, Loops, and String Operations
name = input("Please enter your name: ")
print("Hello, " + name + "! Welcome to the programming world!")
print('Z' in name)
print('Z' not in name)

for i in range(2, 11, 2):
    print(i)  
print("Loop is finished.")

for i in range(1, 11):
    print(i*3)

for i in range(1, 21):
    print(f"Table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)

for i in range(1, 11):
    print(f"{i*2} | {i*3} | {i*4} | {i*5} | {i*6} | {i*7} | {i*8} | {i*9} | {i*10}")
# Python Conditional Statements (if-else)
no = int(input("Please enter a number: "))

if no > 0:
    print("The number is positive.")
    
elif no < 0:
    print("The number is negative.")
    
else:
    print("The number is zero.")

# accept day from user and check whether it's a working day or weekend using if-else statement
day = input("Please enter a day: ")
day = day.capitalize() 
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a working day.")
else:
    print("It's a weekend.")

# accept marks of three papers and calculate total and percentage and check whether the student is eligible for placement or not using if-else statement. (Eligibility criteria: percentage should be greater than 60%)
marks1 = float(input("Enter marks for paper 1: "))
marks2 = float(input("Enter marks for paper 2: "))
marks3 = float(input("Enter marks for paper 3: "))
total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100

if percentage > 60:
    print("The student is eligible for placement.")
else:
    print("The student is not eligible for placement.")# accept five different values in five different variables and print maximum value using simple if statements
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
d = int(input("Enter fourth value: "))
e = int(input("Enter fifth value: "))

if a > b and a > c and a > d and a > e:
    print("The maximum value is:", a)
elif b > c and b > d and b > e:
    print("The maximum value is:", b)
elif c > d and c > e:
    print("The maximum value is:", c)
elif d > e:
    print("The maximum value is:", d)
else:
    print("The maximum value is:", e)for i,j,z in zip(range(1,6), range(5,0,-1), range(10,15)):
    if i == 3 and j == 3 and z == 12:
        continue
    print(i,j,z)username = ""
password = ""
while username != 'admin' and password != "hello":
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == 'admin' and password == "hello":
        print("Approved!")
    else:
        print("Enter correct username and password")
        
# write a program that sum of first 10 numbers using while loop
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("The sum of the first 10 numbers is:", total)

# remove duplicate characters from a string using while loop
name = "prashant"
unique_chars = ""
i = 0
while i < len(name):
    if name[i] not in unique_chars:
        unique_chars += name[i]
    i += 1
print("Original string:", name)
print("String with duplicate characters removed:", unique_chars)

#remove duplicate characters from a string using for loop
name = "prashant"
unique_chars = ""
for char in name:
    if char not in unique_chars:
        unique_chars += char
print("Original string:", name)
print("String with duplicate characters removed:", unique_chars)

# reverse a string using while loop and for loop
# using while loop
name = "prashant"
reversed_name = ""
i = len(name) - 1
while i >= 0:     
    reversed_name += name[i]
    i -= 1
print("Original string:", name)
print("Reversed string:", reversed_name)

# using for loop
name = "prashant"
reversed_name = ""
for i in range(len(name) - 1, -1, -1):
    reversed_name += name[i]
print("Original string:", name)
print("Reversed string:", reversed_name)

mycart = [10,20,30,60,800,500,9]
for i in mycart:
    if i > 400:
        print("This items are purchased")
        continue
    print(i)

# user input to check palindrome or not
word = input("Enter a word: ")
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

# user input to check anagram or not
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if sorted(word1) == sorted(word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")

# add key value pair to a dictionary
my_dict = {"name": "Alice", "age": 30}
my_dict["city"] = "New York"
print(my_dict)

#remove key value pair from a dictionary using pop operator
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_dict.pop("age")
print(my_dict)

#check if a key exists in a dictionary using get() operator
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
key_to_check = "age"
if my_dict.get(key_to_check) is not None:
    print("Key Exists")
else:
    print("Key does not exist")

#iterate over key value pair in a dictionary using for loop
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Nested for loop to print a pattern
for i in range(1, 4):
    for j in range(1, 4):
        print(i, end="")
    print()

# nested for loop to user input to print ascii code
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(chr(64 + i), end=" ")
    print()

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print((n + 1 - i), end=" ")
    print()