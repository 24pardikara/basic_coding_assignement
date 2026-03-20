def msg():
    print("Welcome to Python programming!")

def add():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print("Sum is: ", n1 + n2)
    
msg()
add()

def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    sum = n1 + n2
    # print("Sum is: ", sum)
    sub = n1 - n2
    # print("Difference is: ", sub)
    mul = n1 * n2
    # print("Product is: ", mul)
    div = n1 / n2
    # print("Quotient is: ", div)
    return sum, sub, mul, div

result = main()
print("Sum is: ", result[0])
print("Difference is: ", result[1])
print("Product is: ", result[2])
print("Quotient is: ", result[3])

def personalInfo(fname, lname):
    print("First name: ", fname)
    print("Last name: ", lname)

personalInfo("John", "Doe") 
personalInfo(fname="Jane", lname="Smith") 
personalInfo("Alice", lname="Johnson") 

def cityInfo(city = "Hyderabad"):
    print("City: ", city)
    
cityInfo("Nagpur")
cityInfo("Mumbai")
cityInfo("Pune")
cityInfo()

def studentNames(*name):
    print(name)

studentNames("Prashant", "Rahul", "Mandip", "Ashish")

mylist = [1, 2, 3, 4, 5]
def searchElement(target):
    for i in range(len(mylist)):
        if mylist[i] == target:
            print("Element found at index: ", i)
            return i
    return -1

result = searchElement(3)
if result != -1:
    print("Element found at index: ", result)
else:    
    print("Element not found in the list.")

def timeConversion(s):
    hour = int(s[0:2])
    minute = s[3:5]
    second = s[6:8]
    period = s[8:]
    if period == "AM":
        if hour == 12:
            hour = 0  
    else: 
        if hour != 12:
            hour += 12  
    hour_str = f"{hour:02d}"
    return f"{hour_str}:{minute}:{second}"