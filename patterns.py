#!/usr/bin/env python
# coding: utf-8

# In[3]:


# print alphabet C using star patterns.
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or j==1:
            res+="*"+" "
    print(res)


# In[5]:


# print E using star pattern.
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or j==1 or i==(rows//2)+1:
            res+="*"+" "
    print(res)


# In[8]:


# print I using star pattern.
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or j==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# In[11]:


# print X  using star pattern.
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==j or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# In[12]:


# print H using star pattern.
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# In[13]:


# print T using star pattern.
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or j==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# In[14]:


# print N using star pattern.
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==j:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# In[15]:


# print Z using star pattern.
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# In[20]:


# print hallow square pattern.
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or j==1 or j==rows:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# In[1]:


#print square pattern.
rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        pattern+="*"+" "
    print(pattern)


# In[2]:


#print left triangle pattern.
rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,i+1):
        pattern+="*"+" "
    print(pattern)


# In[3]:


#print triangle pattern with numbers.
rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(j)+" "
    print(pattern)


# In[4]:


#print triangle pattern as same row number.
rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(i)+" "
    print(pattern)


# In[9]:


rows=4
num=1
for i in range(1,rows+1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(num)+" "
        num+=1
    print(pattern)


# In[10]:


rows=5
num=1
for i in range(1,rows+1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(num)+" "
        num+=1
    print(pattern)


# In[ ]:




