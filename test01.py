import tkinter

#To initialize tkinter, we have to create a Tk root widget, which is a
#window with a title bar and other decoration provided by the window manager.
#The root widget has to be created before any other widgets and there can only
#be one root widget. 
mainWindow = tkinter.Tk()

#get screen resolution, to create a propotional window
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
print("screen_width: %s screen_height: %s" % (screen_width, screen_height))

mainWindow.geometry('%dx%d' % (screen_width/2, screen_height/2))
mainWindow.title('Hello, Tkinter!')



label1 = tkinter.Label(mainWindow, text="hello")


mainWindow.mainloop()
