from tkinter import *
#This function takes in inputs from the two entry and puts them through
# the AND OR and XOR functions
def initiate():
    A=EntryA.get()
    ArrayA=[x.strip() for x in A.split(',')]
    B=EntryB.get()
    ArrayB=[x.strip() for x in B.split(',')]
    EntryA.delete(0,END)
    EntryB.delete(0,END)
    AND(ArrayA,ArrayB)
    OR(ArrayA,ArrayB)
    XOR(ArrayA,ArrayB)
#finds the AND of the two sets
def AND(A,B):
    result=[]
    for i in A:
        if i in B and i not in result:
            result.append(i)
    result.sort()
    LabelAND.configure(text=("A AND B: "+", ".join(result)))
#finds the OR of the two sets
def OR(A,B):
    result=[]
    for i in A:
        if i not in result:
            result.append(i)
    for i in B:
        if i not in result:
            result.append(i)
    result.sort()
    LabelOR.configure(text=("A OR B: "+", ".join(result)))
#Finds the XOR of the two sets
def XOR(A,B):
    result=[]
    for i in A:
        if i not in B and i not in result:
            result.append(i)
    for i in B:
        if i not in A and i not in result:
            result.append(i)
    result.sort()
    LabelXOR.configure(text=("A XOR B: "+", ".join(result)))
#This chunk of code sets up the GUI
window=Tk()
window.title("Subsets")
window.geometry("800x450")
window.configure(bg="#bea4e9")
EntryA=Entry(window,width=50,borderwidth=10)
EntryA.place(x=450,y=200)
EntryB=Entry(window,width=50,borderwidth=10)
EntryB.place(x=450,y=250)
InfoLabel=Label(text="please enter both sets in a comma format without parenthesis,\n an example would be... \nA: 1,A,3  B: 4,5,Z",font=("fixedsys",10),wraplength=300,bg="#bea4e9")
InfoLabel.place(x=475,y=350)
LabelA=Label(text="A:",font=("fixedsys",20),bg="#bea4e9")
LabelA.place(x=400,y=200)
LabelB=Label(text="B:",font=("fixedsys",20),bg="#bea4e9")
LabelB.place(x=400,y=250)
LabelOR=Label(text="A OR B: ",font=("fixedsys",20),wraplength=400, anchor="w",bg="#bea4e9")
LabelOR.place(x=0,y=0)
LabelAND=Label(text="A AND B: ",font=("fixedsys",20),wraplength=400, anchor="w",bg="#bea4e9")
LabelAND.place(x=0,y=150)
LabelXOR=Label(text="A XOR B: ",font=("fixedsys",20),wraplength=400, anchor="w",bg="#bea4e9")
LabelXOR.place(x=0,y=300)
The_Button=Button(window,text="Enter",padx=136,bg="#CDFFFF",font=("fixedsys",3),command=initiate,)
The_Button.place(x=450,y=300)
window.mainloop()
