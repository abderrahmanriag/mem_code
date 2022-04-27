from tkinter import *
from tkinter import ttk
import re
import verify as vr
backround_color="grey70"
FONT=("Courier",15)
def ve():
                    x=sol_input.get()
                    x=re.findall(r'\b\d+\b', x)
                    for i in x:
                                        int(i)
                    valid, sol=vr.verify(x)
                    print(valid)
                    getVerify.insert(0, (valid, "#", sol[1]))
root=Tk()
root.configure(background=backround_color)
root.title('Verification')
root.geometry('840x150+300+180')

l=Label(root, text="Enter the solution", font=FONT, bg=backround_color)
l.place(x=10, y=10)


sol_input=Entry(root, width=90, font=30)
sol_input.place(x=10, y=50)


getVerify=Entry(root, width=20, font=40)
getVerify.place(x=150, y=100)

b=ttk.Button(root, text="Verify", command=ve)
b.place(x=10, y=100)

root.mainloop()