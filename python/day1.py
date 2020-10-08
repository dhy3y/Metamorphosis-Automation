#This is the comment
#This is the print function
print("This line will be printed")
#we uses the indention for setting the scope
x = 1
if x == 1:
    #indented to set the scope
    print("x is 1")
#everything in python is an object
#Number in python
myint = 7
print(myint)
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
#string are with single or double quotes
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
one = 1
two = 2
three = one + two
print(three)
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
#assignments on a single line
a,b = 3,4
print(a,b)
#List in python
#List are like arrays
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
#using loop to print
for x in mylist:
    print(x)
#print(mylist[3])
number = 1 + 2 * 3 / 4.0
print(number)
remainder = 11 % 3
print(remainder)
#7^2 = 49
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
#string concatination with +
helloworld = "hello" + " " + "world"
print(helloworld)
#forming repetaive sting sequence
lotsofhello = "hello" * 10
print(lotsofhello)
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
print([1,2,3] * 3)
