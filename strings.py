#!/usr/bin/env python
# coding: utf-8

# In[5]:


# To find vowels using strings.
vowels="aeiou"
name="Monika"
vowel_count=0
for i in range(len(name)):
    c=name[i]
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
        vowel_count=vowel_count+1
print(vowel_count)


# In[6]:


# To find consonants using strings.
name="Saipraveen"
consonant_count=0
for i in range(len(name)):
    c=name[i]
    if c!="a" and c!="e" and c!="i" and c!="o" and c!="u":
        consonant_count=consonant_count+1
print(consonant_count)


# In[7]:


# To find char index using strings.
name="Karthikeya"
for i in range(len(name)):
    print(name[i],"is in",i,"index")


# In[8]:


# To find only vowels in a name using strings.
name="Padmasri"
for i in range(len(name)):
    c=name[i]
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
        print(name[i],"is in",i,"index")


# In[10]:


# To find only consonants in a name using strings.
name="Geethika"
for i in range(len(name)):
    c=name[i]
    if c!="a" and c!="e" and c!="i" and c!="o" and c!="u":
        print(name[i],"is in",i,"index")


# In[11]:


# To find length of the string.
word="Tiara"
for i in range(len(word)):
    print(word[i])


# In[1]:


# To find index numbers of a string.
word="Kanna"
for i in range(len(word)):
    print(i)


# In[2]:


# To find how many characters of the string.
word="advait"
char_count=0
for i in range(len(word)):
    if word[i]!="":
        char_count+=1
print(char_count)


# In[3]:


# Length of the string.
name="honey"
print(len(name))


# In[9]:


# To find length and particular character in string using index number.
name="bunny"
print(len(name))
print(name[2])
print(name[4])


# In[10]:


# To find last index of a string.
name="arjun"
last_index=len(name)-1
print(name[last_index])


# In[11]:


# To change the first letter of a string as capital letter without using uppercase method.
name="krishna"#declaration + assign
name="Krishna"#reassign
print(name)


# In[12]:


# To reverse a string without using reverse method.
word="nandan"
last=len(word)-1
for i in range(last,-1,-1):
    print(word[i])


# In[13]:


# Comparision of two strings.
print("AI"=="Ai")#because python is case sensitive.


# In[1]:


# print even positions of the vowel.
sentance="i am learning python"
for index in range(len(sentance)):
    c=sentance[index]
    if(c=="a" or c=="e" or c=="i" or c=="o" or c=="u") and (index%2==0):
        print(c,index)


# In[4]:


# print characters that are multiple of a number.
sentance="i am learning python"
for index in range(len(sentance)):
    c=sentance[index]
    if(index%4==0)and c!=" ":
        print(c,index)


# In[5]:


# counting number of words and removing the spaces using strip.
sentance="     we are going to play cricket on this sunday they after for lunch    "
spaces=sentance.strip().count(" ")
print("there are",spaces+1,"words") 


# In[6]:


# counting no of words using functions.
def count(sentance="    we are going to play cricket on this sunday they after for lunch    "):
    spaces=sentance.strip().count(" ")
    print("there are",spaces+1,"words")
count()   


# In[8]:


# Uppercase method in strings.
name="Hai"
a=name.upper()
print(a)


# In[9]:


# lowercase method in strings.
name="HellO"
a=name.lower()
print(a)


# In[10]:


# Capitalize method in strings.
name="sai"
a=name.capitalize()# to print first letter should be capital
print(a)


# In[11]:


# Title method in strings.
sentance="royal challengers bengaluru"
a=sentance.title()# to captitalize of the every word starting letter in the sentance.
print(a)


# In[12]:


# Strip method in strings.
name="  hanuman  "
a=name.strip()#to remove starting and ending space in a string
print(a)


# In[13]:


# leading method in strings.
name="  hanuman  "
a=name.lstrip()#to remove starting space in a string
print(a)


# In[14]:


# Trailing method in strings.
name="  hanuman  "
a=name.rstrip()#to remove ending space in a string
print(a)


# In[15]:


# Replace method in strings.
word="hello people,people are good"
word=word.replace("people","all")
print(word)


# In[16]:


#find method in strings.
word="string is a collection of characters"# it will print the index number of a character.
print(word.find("c"))# it will return if multiple time the character is there it only takes the first occurance.


# In[19]:


# Count method in strings to find how many times the character will appears.
name="we are going to play cricket on sunday "
a=name.count("e")#to remove starting and ending space in a string
print(a)


# In[21]:


# Count the spaces in a sentance.
name="we are going to play cricket on sunday"
a=name.count(" ")
print(a)


# In[22]:


# To check the char is upper or lowercase without using methods.
char="M"
if char==char.upper():
    print("char is in uppercase")
else:
    print("char is in lowercase")


# In[23]:


# To count how many uppercases in a sentance.
sentance="i like KOREAN DRAMAS"
upper_count=0
for i in range(len(sentance)):
    if sentance[i]==sentance[i].upper() and sentance[i]!=" ":
        upper_count+=1
print(upper_count)


# In[1]:


# Create a string with your name and print it.
name="Monika"
print(name)


# In[3]:


# Get the first character from the string.
name="paddu"
print(name[0])


# In[4]:


# Concatenate two strings.
str1="Sai"
str2="monika"
print(str1+str2)


# In[6]:


# Repeat of two strings.
word="Radhe"
print(word*3,)


# In[20]:


# Slice the first 5 character.
str="Tarakram"
print(str[:5])


# In[21]:


# Reverse a string.
name="Krishna"
print(name[::-1])


# In[24]:


# Check if a substring exists in a string.
a="radhakrishna"
b="krishna"
if b in a:
    print("Exist")
else:
    print("Not exist")


# In[37]:


# To print how many times the char is present, with index num.
sen="hello world"
a="l"
for i in range(len(sen)):
    if a==sen[i]:
        print(a,"is present in",i)


# In[39]:


# To print unique characters.
word="karthikeya"
for i in range(len(word)):
    if word.count(word[i])==1:
        print(word[i])


# In[40]:


# To print duplicate characters.
word="karthikeya"
for i in range(len(word)):
    if word.count(word[i])!=1:
        print(word[i])


# In[41]:


# Starts with particuar character.
word="karthi"
print(word.startswith("ka"))


# In[42]:


# Ends with particuar character.
word="arthi"
print(word.endswith("i"))


# In[43]:


# isalpha method in strings.
word="rocky"
print(word.isalpha())


# In[44]:


# isdigit method in strings.
num="1234567"
print(num.isdigit())


# In[45]:


# isalnum method in strings.
user_id="rocky22"
print(user_id.isalnum())


# In[46]:


# Swapcase method in strings.
word="pYTHOn"
print(word.swapcase())# change uppercase to lowercase,vise-verse


# In[47]:


# without using swapcase.
word="hAI"
for i in range(len(word)):
    if word[i]==word[i].upper():
        print(word[i].lower())
    else:
        print(word[i].upper())


# In[48]:


# zfill method in strings.
word="geethi"
print(word.zfill(9))


# In[52]:


# without using zfill.
word="radha"
l=7
req=l-len(word)
new_str=" "
for i in range(req):
    new_str+="0"
print(new_str+word)


# In[54]:


# split method in strings.
sen="good morning, everyone"
print(sen.split(" "))


# In[55]:


# join method in strings.
num_list=["hi","how","r","u"]
print(" ".join(num_list))


# In[59]:


# palindrome of a string.
word="amma"
rev=""
for k in range(len(word)-1,-1,-1):
    rev+=word[k]
if rev==word:
    print("palindrome")
else:
    print("not palindrome")


# In[7]:


# check whether the char is lower,upper,number using function.
def asc_char(char):
    asc=ord(char)
    if asc>=65 and asc<=90:
        print("uppercase")
    elif asc>=97 and asc<=122:
        print("lowercase")
    elif asc>=48 and asc<=57:
        print("number")
    else:
        print("special character")
asc_char("-")


# In[11]:


# write function to convert vowel char into new char.
def de_code(name):
    result=""
    for i in range(len(name)):
        char=ord(name[i])
        if name[i]=="a" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u":
            result+=chr(char+1)
        else:
            result+=name[i]
    print(result)
de_code("chinnu")    


# In[8]:


# encryption of a string.
name="chitti"   ## dijuuj
secret=""
for i in range(len(name)):
    code=ord(name[i])
    new_char=chr(code+1)
    secret+=new_char
print(secret)


# In[13]:


# Find ASCII value of char.
print(ord("S"))
print(ord("M"))


# In[15]:


# Find ASCII value of number.
print(ord("7"))


# In[20]:


# To print char by using ASCII value.
code=45
print(chr(code))
print(chr(22))


# In[10]:


# To count how many number of palindromes in a sentance.
def palindrome_count(sen):
    words=sen.split()
    count=0
    for i in range(len(words)):
        if words[i]==words[i][::-1]:
            count+=1
            print("palindrome is:",words[i])
    print("Total no of palindromes are:",count)
palindrome_count("my family consists of amma nanna akka anna")    


# In[ ]:




