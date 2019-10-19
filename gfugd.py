from Tkinter import *

class Application(Frame):

     def _init_(self,master):
         Frame._init_(self,master)
         self.grid()
         self.create_widgets()

     def create_widges(self):
          self.instruction=Label(self,text="Enter ")
          self.instruction.grid(row=0,column=0,columnspan=2,sticky=W)

          self.password=Entry(self)
          self.password.grid(row=1,column=1,sticky=W )

          self.submit_button=Button(self,text="Check",command=self.reveal)
          self.submit_button.grid(row=2,column=0,sticky=W)

          self.text=Text(self,width=35,height=5,wrap=WORD)
          self.text.grid(row=3,coulmn=0,columnspan=2,sticky=W)

     def reveal(self):
            content=self.password.get()

            if content== "password" :
                message="yyyyyyyyyy"
            else :
                message="nnnnoooo"

            self.text.insert(0.0,message)

root=Tk()
root.title("Password")
root.geometry("250x150")
app=Application(root)
app.grid()
root.mainloop()
            
          
