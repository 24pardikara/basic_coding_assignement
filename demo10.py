username = ""
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