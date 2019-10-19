from Tkinter import *
root=Tk()
root.title("Labeler")
root.geometry("200x100")
app=Frame(root)
app.grid()
button1=Button(app,text="This is a button")
button1.grid()
button2=Button(app)
button2.grid()
button2.configure(text="this will show text")
button3=Button(app)
button3.grid()
button3["text"]="this will show up as well."
 

root.mainloop()
