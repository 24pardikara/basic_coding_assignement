for i in range(5):
    print(i)




for i in range(1,10,2):
    print(i)




for i in range(1,11):
    print(i*2)




for i in range(1,11):
    print(i*2, "  ", i*3,"  ",i*4)
print()
for i in range(1,11):
    print(i*11, "  ", i*12,"  ",i*13)





name = 'prashant'
data =['a','e','i','o','u']
vowel = 0
cons = 0
for i in name:
    if i in data:
        vowel +=1
    else:
        cons+=1
print("Vowels = ",vowel)
print("consonant = ", cons)







a=50
b=30
c=20
d=10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)






x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x!=z)







mylist = [2,5,8,4,1,9,8]
even = 0
odd = 0
total = 0
for i in mylist:
    total = total + i
    if i % 2:
        even += 1
    else:
        odd += 1
print("even = ",even)
print("odd = ",odd)
print("total sum = ",total)







val =[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(val.index(1))
print(val.index(2))
print(val.index(3))
print(val.index(4))
print(val.index(5))
print(val.index(6))







val =[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(val.count(1))
print(val.count(2))
print(val.count(3))
print(val.count(4))
print(val.count(5))
print(val.count(6))







rollno = [3,5,7,1,11,4,5,2]
for x in rollno:
    if x == 2 or x == 4 or x==6 or x==8 or x==10:
        print("even no is found ",x)
        break






name ="prashant"
i =0
for x in name :
    if x =='n' :
        print("the character present at index no ",i,"value=:",x)
        break
    i=i+1






for i in range (10):
    if i==5:
        continue
    print(i)






for i , j in zip(range(1,6), range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i," ",j)








#WAP to accept any character and check the entered character is upper case, lower case, digit and special symbol

ch = ord(input("enter any character= "))
if ch>=65 and ch<=91:
    print("you entered character is in upper case")
elif ch>=97 and ch<=122:
    print("you entered character is in lower case")
elif ch>=48 and ch<=57:
    print("you entered character is digit")
else:
    print("your entered character is in speacial symbols")








v = ['a','e','i','o','u']
w = input ("enter the word we will search the vowels: ")
found=[]
for i in w:
    if i in v:
        if i not in found:
            found.append(i)
print('found vowels= ',found)
print('Unique vowels',len(found),'from the given word=',w)