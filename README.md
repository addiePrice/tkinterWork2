from tkinter import *

top = Tk()
groceryList = []

def results():
    print(groceryList)
      
def exportList():
    with open('test.txt', 'w') as f:
        for item in groceryList:
            f.write("%s\n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs", bg = "#FFC300")
    LMain.grid(column = 2, row = 1)
    
    B1Main = Button(text = "Week 1", bg = "#FF5733", command = week1)
    B1Main.grid(column = 2, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "#C70039", command = week2)
    B2Main.grid(column = 2, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "#900C3F")
    B3Main.grid(column = 2, row = 4)

def week1():
    
    def addToList():
        newItem = E1.get()
        groceryList.append(newItem)
        E1.delete(0, END)

    clearWindow()
    
    #this is a Label widget
    L1 = Label(top, text = "Type stuff :)")
    L1.grid(column = 0, row = 1)

    #this is an Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #this is a Button widget
    B1 = Button(text = "   Print Stuff   ", bg = "#FFC300", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = "  +  ", bg = "#DAF7A6", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "  Export Stuff  ", bg = "#FF5733", command = exportList)
    B3.grid(column = 0, row = 4)
    
    Bclear = Button(text = "Main Menu", bg = "white", command = mainMenu)
    Bclear.grid(column = 3, row = 1)

def week2():
    clearWindow()
    L1W2 = Label(top, text="Dice Roller Program", bg = "white")
    L1W2.grid(column = 0, row = 1)

    L2W2 = Label(top, text = "How many sides?", bg = "white")
    L2W2.grid(column = 0, row = 2)
    
    L3W2 = Label(top, text = "How many rolls?", bg = "white")
    L2W2.grid(column = 2, row = 2)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)
    
    B1W2 = Button(text = "Roll!", bg= "white")
    B1W2.grid(column = 2, row = 4)

if __name__ == "__main__":
    mainMenu()
    top.mainloop()

