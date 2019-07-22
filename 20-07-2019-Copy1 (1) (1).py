#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=1
b=9
c=a+b
print(c)


# # Document Title
# 
# ### Date:20-07-2019
# 
# ### Session Objectives
# 
# * To intraduce jupyter notebook
# * To teach ***markdown*** jupyter
# * To intraduce **python** basics
#   * Basic Syntax(Variables,Assignment,Data Types)
#   * Control Structures
#     1. Conditional
#     2. Repetitive
#     
#  <img src='python.png'/> 
# 
# [Link to main website](https://sites.google.com/s/1KvWn3SIsB-AphSUHtTm3wSMRn9xp281A/p/1yBBw62xji1tIj1dHl1fTjmVm2RLBtAv5/edit)

# In[ ]:





# ### Python Basics

# In[5]:


print('Hello vyshnavi')#Single Parameter
print('vyshu'+'dvd' , end=' ')# concatination using +
print('dvd','vyshu')# multiple Parameters


# In[6]:


#print('hello')


# In[7]:


n = input('Enter a value')#capture the i/p and store it in it


# In[8]:


print(n)


# In[9]:


n=int(n)#type conversion to integer and reassign
n*n/1231 -1233645 #Expression evaluation using


# In[10]:


a=b=c=d=10#Assigning a single value to multiple variables
print(a,b,c,'\t',d)
a
b


# In[11]:


type(a)
a=str(a)
type(a)


# In[12]:


type(n)


# In[13]:


a,b,c,d=1,2,3,4#Assigning multiple values to multiple variables
print(a,type(a),b,c,id(d))


# In[14]:


b=float(b)
print(type(b))


# ### String Slicing

# In[15]:


s ='python programing'
s[0]


# In[72]:


s[::]


# In[75]:


s[:]


# In[16]:


s[-1]


# In[17]:


s[0:6]
s[:6]


# In[65]:


s[len(s)-1]


# In[74]:


s[len(s)-2]


# In[18]:


s[-1::-1]#reverse the string
s[::-1]


# In[19]:


s[7:]
s[7:len(s)]


# In[20]:


s[::-2]


# In[21]:


s[-1:6:-1]#reverse of substring


# In[22]:


s[5::-1]#reverse of substring


# In[23]:


s2='123456'
s2[-1:2:-1]#reverse of the last len(s2)-3


# In[24]:


s3='123456789'#reverse  of characters from index 5 to 3
s3[5:2:-1]


# In[25]:


s3[::2]#Accesing alternate character


# In[26]:


s3[1::2]


# In[27]:


s3[::-2]


# ### Functions in Python

# In[28]:


def reverseString(s):#reverse the string
    return s[::-1]
print(reverseString(s))
reverseString(s3)


# In[29]:


def reverseSubstring(s,i,j):#reverse the substring
    return s[j:i-1:-1]

reverseSubstring('abcde',1,3)


# In[30]:


def reverseSubstring(s,i,j):#reverse the substring
    sub=s[i:j+1]
    return sub[::-1]

reverseSubstring('abcde',0,2)


# ### Conditional Control Structures

# In[31]:


def divisibilityTest(n):# function to text divisibility  by 9,10 and 11
    if (n%9 == 0 and n%11 ==0 and n%10 ==0):
        return True
    else:
        return False
divisibilityTest(990)    
        


# In[32]:


def divisibilityTest(n):
    if n%9 == 0 and n%11 ==0 and n%10 ==0:
        return True
    else:
        return False
divisibilityTest(990)    
        


# In[33]:


#Recurssive Function for a power n
def powerN(a,n):
    if n ==0:
        return 1
    return a * powerN(a,n-1)
powerN(2,6)


# In[87]:


#function to check if a given string is a palindrome 
def ispalindrome(s):#starting and ending letter is same or not
    if(s == s[::-1]):
        return True
    else:
        return False
    
ispalindrome('dvd')        


# ### Iteration in Python

# In[35]:


for i in range (123,126):
    print(i)


# In[36]:


#function to determine all numbers divisible by
#7 in a given range[lb,ub]
def divisible7(lb,ub):
    for i in range(lb,ub+1):
        if i%7 ==0:
            print(i)
    return   
divisible7 (1,70)       
    


# In[37]:


#function to generate N prime numbers 
from math import sqrt,floor

def isFactor(dividend,divisor):
    if dividend % divisor ==0:
        return True
    return False
    
def isPrime(n):
    for i in range(2,floor(sqrt(n))+1):
        if isFactor(n,i):
            return False
    return True

def genPrimes(k):
    primeCounter =0
    seqCounter =2 
    while primeCounter < k:
        if isPrime(seqCounter):
            print(seqCounter,end=' ')
            primeCounter+=1
        seqCounter+=1
    

        
genPrimes(100)


# ### Higher Order Computation

# In[38]:


num = 987 ** 987
print(type(num))
len(str(num))


# ### Python Lists

# In[39]:


li=[1,2,3,4,5,6,'python',5.6]
li


# In[40]:


li[-1]


# In[41]:


li[-2:]


# In[42]:


li[6][0]


# In[43]:


li.append([321,543,765])
li


# In[44]:


li.remove(5.6)
li


# In[48]:


li[7].remove(543)
li


# In[55]:


li.pop(3)
li


# In[50]:


li.insert(1,546)
li


# In[77]:


lst=[9,2,8,4,7]
lst.sort()
lst


# In[78]:


lst.pop(2)
lst


# In[102]:


n=int(input('enter value:'))
if n>1:
    for i in range(2,n):
        if (n%i) == 0:
            print(n,'is not a prime ')
            break
        else:
            print(n,'is  a prime ')
            break
            


# In[ ]:





# In[ ]:




