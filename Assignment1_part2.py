#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Book:
    def __init__(self, title="", author="" ):
        self.author=author
        self.title=title
    def display(self):
        print(self.title + ", written by " +  self.author)
b1 = Book("Of Mice and Men", "John Steinbeck" )
b1.display()
b2 = Book("To Kill a Mockingbird", "Harper Lee")
b2.display()


# In[ ]:





# In[ ]:




