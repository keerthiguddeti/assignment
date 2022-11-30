#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.write a program to accept two numbers from the user and calculate multiplication,division 


# In[2]:


num1=int(input("Enter your number"))
num2=int(input("Enter your number"))
print(num1*num2)
print(num1%num2)


# In[3]:


# 2.write a program to print the characters from a string that are present at an even index


# In[4]:


name="keerthi"
new=''
for a in range(len(name)):
    if a%2==0:
        new=new+name[a]
print(new)


# In[5]:


# 3.write a program to print the characters from a string that are present at an odd index


# In[6]:


name="keerthi"
new=''
for b in range(len(name)):
    if b%2!=0:
        new=new+name[b]
print(new)


#  4.write a phython program which will print the sumof the two numbers if the two numbers are even or it will print the
#   difference of two numbers

# In[7]:


num1=int(input("number 1:- "))
num2=int(input("number 2:- "))
if num1 and num2%2==0:
    print("sum of {} and {} is {}".format(num1,num2,num1+num2))
else:
    print("difference of {} and {} is {}".format(num1,num2,num1-num2))


# 5.write a python programto to convert all even indexed alphabets to upper and odd indexed char to lower?

# In[8]:


name=input("type here :")
new=""
for i in range(0,len(name)):
    if i%2==0:
        new+=name[i].upper()
    else:
        new+=name[i].lower()
print(new)


# 6.write a python program to which willmprint true if the input number is divisible by 5 or else false

# In[11]:


num=int(input("Enter your number : "))
if num%5==0:
    print(True)
else:
    print(False)


# 7.Given two integer numbers return their product only if the product is greater than 1000,else return their sum

# In[15]:


num1=int(input("number 1:- "))
num2=int(input("number 2:- "))
def pro(num1,num2):
    if num1*num2 >1000:
        return "the productof {} and {} is {}".format(num1,num2,num1*num2)
    else:
        return "The sum of {} and {} is {}".format(num1,num2,num1+num2)

pro(num1,num2)


# 8.Given two strings x,y write a program to return a new string made of xand y's first middle and last character
#  - example:input X="python"y="java"Output"pjtvos"
# 

# In[16]:


x=input()
y=input()
def slicing(x,y):
    ma=int(len(x)/2)
    mb=int(len(y)/2)
    print("\n")
    print(x[0]+y[0]+x[ma]+y[mb]+x[-1]+y[-1])
slicing(x,y)


# 9.Write a python program to take three names as input from a  user in the single input from a user in the single input()function call

# In[2]:


name=input("Please enter your names here : ")
div=name.split()
for names in div:
    print(" {}".format(names))


# 10.write a python program to get a string from a given string where all ocurrence of its first char have been changed to '@',except the first char itself

# In[2]:


name=input("enter your name here")
a=name[0]
b=name[1:]
c=b.replace(a,"@")
print(a+c)


# 11.write a python program to add 'ing' at the end of given string (string length should be equal to or more than 3).if the given string alraedy ends with 'ing'then add 'ly'insted.if the string length of the given string is less than 3,leave it

# In[6]:


name=input("please enter the string here:")
           
if len(name)<3:
    print(name)
else:
    if name[-3:]=="ing":
        print(name.replace("ing","ly"))
    else:
        print(name+"ing")
    


# 12.write a python program that accepts two inputs num1 and num2 print true if one of them is 10 or if their sum is 10 otherwise print false

# In[7]:


num1=int(input("num1 : "))
num2=int(input("num2 : "))
if num1==10 or num2==10 or num1+num2==10:
    print(True)
else:
    print(False)


# 13..write a python program that accepts three inputs x,yand z print true if x*y>z other wise false 

# In[8]:


x=int(input())
y=int(input())
z=int(input())
if x*y>z:
    print(True)
else:
    print(False)


# 14.write a python program to print that accepts two strings inputs return true depending on whether the total number of charaters in the first string is equal to the total number of characters in the second string

# In[9]:


name1=input()
name2=input()
if len(name1)==len(name2):
    print(True)
else:
    print(False)


# 15.write a python program that takes a string input,well say that the front is the first  three characters of the string.if the string length is less than three characters the front is whatever is there,return a new string which is three copies of the front

# In[10]:


name=input()
if len(name)<3:
    print(name)
else:
    var=name[0:3]
print(var,var,var)


# 16.write a python program that takes in a words determines whether or not it is plural a plural word is one that ends in "s"

# In[12]:


word=input()
if word[-1]=="s" or word[-1]=="s":
    print("the given word {} is plural ".format(word))
else:
    print("the given word {} is not a plural ".format(word))


# 17.A bartender is writing a simiple program to determine whether he should serve drinks to someone. He only serves drinks to peole 18 and older and when he's not on break (true means break and false means nota break time). Given the persons age and whether break times is in session create a python program which prints whether he should serve drink or not. 

# In[15]:


name=input("Enter your")
age=int(input("please provide your age: "))
print("provide bar tender is in break or not?")
b=input("type y or n")
if b=="n" or b=="n":
    print("Bartender is not taking break!")
    if age >=18:
        print(" the bartender serves drink to {}".format(name))
    else:
        print("the bartender serves drink to {}".format(name))
if b=="y" or b=="y":
    print("the bartender serves drink to {}".format(name))
    


# 18.manoj kumar has family  and frieds.help him remind them who is who given a string with a name, return the relation of that person to manoj kumar.

# In[4]:


person=input("Please enter your name : ")
data={"shiva":"Father","letha":"Mother","vasavi":"Sister","tarun":"Brother"}
if person in data:
   print("{} is {} to Manoj Kumar.".format(person,data[person]))
else:
   relation=input("Please provide your relation with Manoj Kumar : ")
   if relation!="friend" or relation!="Friend":
       data.update({person:relation})
       print("{} is {} to Manoj Kumar.".format(person,data[person]))
   else:
       print("{} is friend to Manoj Kumar.".format(person))


# 19. Write a python program that takes a string, breaks it up and returns it with vowels
# first, consonants second. For any character that's not a vowel (like special characters
# or spaces), treat them like consonants

# In[6]:


string=input()
v=""
c=""
for letters in string:
    if letters in ["a","e","i","o","u","A","E","I","O","U"]:
        v+=letters
    else:
        c+=letters
print(v+c)


# In[ ]:




