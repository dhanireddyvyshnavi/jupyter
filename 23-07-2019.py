#!/usr/bin/env python
# coding: utf-8

# ### Day 7
# 
# ### Date:(23-07-2019)
# 
# ### Day Objectives:
# 
#     * Tuples
#     * Dictionaries
#     * Linear and Binary Search
#     * Date Arthmetic
#     * Iterators and Generators
#     * Functional Programming
# 
# 
# 

# ### Python Tuples

# In[2]:


t1 = (1001,'name',85,72,90)


# In[3]:


t1


# In[4]:


t1[0]


# In[5]:


t1[-1]


# In[6]:


t1[2:]


# In[13]:


t2=(321,654,789098) #Accessing all the 2nd digits of elements in a list
print(str(t2[0])[1], str(t2[1])[1], str(t2[2])[1])


# In[14]:


t2=(321,654,789098) #Accessing all the 2nd digits of elements in a list
print(str(t2[0])[1]+str(t2[1])[1]+str(t2[2])[1])


# In[16]:


#Function to calculate the Average of all elements in a tuple
def averageTuple(t):
    sum = 0
    for i in range(0,len(t)):
        sum += t[i]
    return sum/len(t) 

averageTuple(t2)


# In[21]:


def averageLinearDs(t):
    sum = 0
    #for i in range(0,len(t)):
      #  sum += t[i]
    for item in t:
        sum+= item
    return sum/len(t) 
li=[123,234,456,678,890]

averageLinearDs(li)
type(t1)
    


# In[18]:


#Function to search in a Linear Data Structure
def searchLinearDS(ds,key):
    for i in range(0,len(ds)):
        if ds[i] == key:
            return i
    return -1    
searchLinearDS(li,456)    


# ### Iterable Objects

# In[24]:


s='python'
for i in s:
    print(i)


# In[27]:


s='python'
for i in s:
    print(i,end='')


# In[28]:


# function to identify the maximum element in a Ds using iterable object
max([123,85,759684])


# In[36]:


# function to identify the maximum element in a Ds using iterable object
def maxElementDS(ds):
    m = ds[0]
    for i in ds:
        if i>m:
            m = i
    return m
maxElementDS(li)


# In[35]:


# function to identify the minimum element in a Ds using iterable object
def minElementDS(ds):
    m = ds[0]
    for i in ds:
        if i<m:
            m = i
    return m
minElementDS(li)


# ### Python Dictionaries

# In[41]:


d1 = {'name':7416251307,'name2':123456789}
d1['name']


# In[42]:


d1 = {'name':7416251307,'name2':123456789}
d1.keys()# all keys in a dict are unique


# In[43]:


d1 = {'name':7416251307,'name2':123456789}
d1.values()


# In[44]:


d1['name3']=987654321


# In[45]:


d1


# In[47]:


d1.pop('name2')#removes a key and value


# In[48]:


d1


# In[56]:


#Contacts application
#Display,Add,Modify and Delete Contacts
contacts = {}
def addContact(d,name,phone):
    contacts[name] = phone
    return

def displayContacts(contacts):
    for name,phone  in contacts.items():
        print(name, ":" ,phone)
    return    
        
    


# In[57]:


addContact(contacts, 'name1' ,7416251307)
addContact(contacts, 'name2' ,1307)


# In[58]:


displayContacts(contacts)


# In[60]:


contacts = {}
def addContact(d,name,phone):
    contacts[name] = phone
    return
addContact(contacts, 'name1' ,7416251307)
addContact(contacts, 'name2' ,1307)


def displayContacts(contacts):
    for name,phone  in contacts.items():
        print(name, ":" ,phone)
    return   
def modifyContacts(contacts,name,newphone):
    contacts[name] = newphone
    return


# In[61]:


addContact(contacts, 'name1' ,7407)
addContact(contacts, 'name2' ,130)


# In[62]:


displayContacts(contacts)


# In[69]:



contacts = {}
def addContact(d,name,phone):
    contacts[name] = phone
    return
addContact(contacts, 'name1' ,7416251307)
def displayContacts(contacts):
    for name,phone  in contacts.items():
        print(name, ":" ,phone)
    return   

def deleteContacts(contacts,name):
    contacts.pop(name)
    return    


# In[70]:



addContact(contacts, 'name1' ,7416251307)


# In[71]:


displayContacts(contacts)


# ### Looping Over Collections

# In[73]:


colors=['red','blue','white']
for i in range(len(colors)-1,-1,-1):
    print(colors[i])


# In[74]:


contacts.items()


# In[80]:


li2=[1,2,3,4,5]
li2=list(reversed(li2))
print(li2)


# In[82]:


li2=[1,2,3,4,5]
li2.reverse()
li2


# ### Regular Expression

# [0-9] RE for all digits
# [0,1,2....9]
# 
# [a-z] RE for all lower case alphabet
# [A-Z] RE for all upper case alphabet
# 
# [10]

# In[ ]:


# function to validate college student roll no
# function to validate indian phone number starting with 9,8,7,6 and have 10 digits
# function to validate email address

username@domain.extension
username=(string of length 9. can contain digits and alphabet)
domain=(string of 9.can)
extension=(length of 3. only alphabet)


# In[7]:


# ^[9876][0-9]{9}$ # logic for mobile number checking in RE


# In[8]:


# logic for email  checking in RE

#   ^[a].{5}[a]$   
#  '^[a-z][a-z0-9_.]{5,14}][@][a-z0-9]{3,12}[.][a-z]{2,3}$'


# In[10]:


import re
def phonenumberValidator(phone):
    phone = str(phone)
    pattern ='^[6-9][0-9]{9}$'
    if re.match(pattern,phone):
        return True
    return False

phonenumberValidator(7416251307)


# In[30]:


import re
def emailValidator(email):
    email = str(email)
    pattern ='^[a-z][a-z0-9_.]{5,14}][@][a-z0-9]{3,12}[.][2,3][.]?$'
    if re.match(pattern,email):
        return True
    return False

emailValidator('vyshoin@gmail.com')


# In[24]:


import re
s=input('mail:')
m=re.fullmatch("\w[a-zA-Z0-9-.]*@gmail[.]com",s)
if m!=None:
    print('valid')
    
else:
    print('invalid')


# ### python Date Time Arithmetic

# In[32]:


import datetime
datetime.datetime.now()


# In[35]:


import datetime
now = datetime.datetime.now()
now.day


# In[38]:


import datetime
now = datetime.datetime.now()
now.second


# In[39]:


import datetime
now = datetime.datetime.now()
print(now.hour,now.minute,now.second)
print(now)


# In[12]:


# function to find the d/f b/w two given dates

#yyyy:mm:dd is the date format as a string
#yyyymmdd

import datetime
def dateDifference(date1,date2):
    year1 = int(date1[:4])
    month1 = int(date1[5:7])
    day1 = int(date1[8:])
    year2 = int(date2[:4])
    month2 = int(date2[5:7])
    day2 = int(date2[8:])
    date1 = datetime.date(year1,month1,day1)
    date2 = datetime.date(year2,month2,day2)
    return date2-date1

    
print(dateDifference('2019:01:02','1994:01:02') )  


# In[ ]:




