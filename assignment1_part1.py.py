#!/usr/bin/env python
# coding: utf-8

# In[12]:


if __name__ == "__main__":
#Create a function listDivide that takes in two parameters
    def listDivide(numbers, divide=2):
        count = 0
        for x in numbers:
            if x%divide==0:
                count += 1
        return count        


# In[14]:


#Custom exception class ‘ListDivideException’.
class ListDivideException(Exception):
    pass


# In[15]:


#Function called testListDivide that performs tests on listDivide
def testListDivide():
    if listDivide([1,2,3,4,5])==2:
        if listDivide([2,4,6,8,10])== 5:
            if listDivide([30, 54, 63,98, 100], divide=10 )== 2:
                if listDivide([]) == 0:
                    if listDivide([1,2,3,4,5], 1)== 5:
                        print(testListDivide)
    else:
        raise ListDivideException


# In[16]:


if __name__ == "__main__":
    testListDivide()


# In[ ]:




