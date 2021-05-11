from tkinter import *

top = Tk()
groceryList = []

def results():
    result = E1.get()
    print(result)
    print(type(result))

def addToList():
    newItem = E1.get()
    groceryList.append(newItem)
    E1.delete(0, END)

#this is a Label widget
L1 = Label(top, text = "Grocery List :)")
L1.grid(column = 0, row = 1)

#this is an Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#this is a Button widget
B1 = Button(text = "   Print Grocery List   ", bg = "#c6edee", command = results)
B1.grid(column = 0, row = 3)

B2 = Button(text = "  Add to Grocery List  ", bg = "#feebe5", command = addToList)
B2.grid(column = 1, row = 2)

top.mainloop()
