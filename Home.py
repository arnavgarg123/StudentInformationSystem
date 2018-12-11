from tkinter import *


class home:

    def func1(self, frame1):

        frame1.grid(row=0, column=1, sticky=N)

        wc = Label(frame1, text="WELCOME TO STUDENT INFORMATION MANAGEMENT SYSTEM",
                   relief="raised", height="5", width="100")
        wc.grid(row=0, column=1)
