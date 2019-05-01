import tkinter

dino = tkinter.Tk()

homePage = tkinter.Frame(dino, bg="blue", height=300, width=200)
homePage.grid_propagate(False)
homePage.grid(row=0, column=0, sticky="nsew")

pageOne = tkinter.Frame(dino, bg="blue")
pageOne.grid(row=0, column=0, sticky="nsew")

homePage.tkraise()

def showHome():
    homePage.tkraise()

def showPageOne():
    pageOne.tkraise()

goToOne = tkinter.Button(homePage, text="start", fg="black", command=showPageOne)
goToOne.grid(row=0, column=0, sticky="nsew")

dino.mainloop()
