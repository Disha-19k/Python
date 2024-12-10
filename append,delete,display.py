#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class mylist():
    def __init__(self):
        self.list1=[]
    def append(self,element):
        self.list1.append(element)
    def remove(self,element):
        if element in self.list1:
            self.list1.remove(element)
        else:
            print("element not found")
    def display(self):
        if(len(self.list1)==0):
            print("list is empty")
        else:
            print("elements are",end=" ")
            for i in range(len(self.list1)):
                print(f"{self.list1[i]}",end=" ")
            print()
obj1=mylist()
print("1.append\n2.delete\n3.display\n4.exit")
while(1):
    choice=int(input("enter your choice"))
    if choice==1:
        element=int(input("enter element"))
        obj1.append(element)
    elif choice==2:
        element=int(input("enter element to delete"))
        obj1.remove(element)
    elif choice==3:
        obj1.display()
    elif choice==4:
        break
    else:
        print("invalid choice")


# In[ ]:




