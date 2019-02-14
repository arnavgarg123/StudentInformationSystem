from tkinter import *
import StudentFunction
import mysql.connector


class student(StudentFunction.studfunc):

    def check1(self, new, frame1):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentlogin"
        )
        myc = mydb.cursor()
        myc.execute("SELECT * FROM login")
        for i in myc:
            if self.usr == i[0] and self.pas == i[1]:
                flag = 0
                for i in frame1.winfo_children():
                    i.destroy()

                self.frame2 = Frame(frame1)
                self.frame2.grid(row=0, column=1, sticky=W)
                self.frame3 = Frame(self.frame2)
                wc = Label(self.frame2, text="Your Personal Information",
                           relief="raised", height="5", width="100")
                wc.grid(row=0, column=0, columnspan=4, sticky=N)

                button1 = Button(self.frame2, text="Details", height="10",
                                 width="21", bg="white", command=lambda: detail())
                button1.grid(row=1, column=0)

                button2 = Button(self.frame2, text="Attendance", height="10",
                                 width="21", bg="white", command=lambda: atten())
                button2.grid(row=1, column=1)

                button3 = Button(self.frame2, text="Academic report",
                                 height="10", width="21", bg="white", command=lambda: acad())
                button3.grid(row=1, column=2)
                button4 = Button(
                    self.frame2, text="Fee Details", height="10", width="21", bg="white", command=lambda: fees())
                button4.grid(row=1, column=3)

                def fees():
                    self.feee()

                def acad():
                    self.acaa()

                def atten():
                    self.atte()

                def detail():
                    self.det()

                break
            else:
                flag = 1
        if flag == 1:
            new.config(text="Invalid Username OR Password")
            new.grid(row=4, column=1)

    def feee(self):
        self.frame3.destroy()
        self.frame3 = Frame(self.frame2)
        self.frame3.grid(row=2, column=0, columnspan=4, sticky=W)
        super().fee(self.usr, self.frame3)

    def acaa(self):
        self.frame3.destroy()
        self.frame3 = Frame(self.frame2)
        self.frame3.grid(row=2, column=0, columnspan=4, sticky=W)
        super().aca(self.usr, self.frame3)

    def atte(self):
        self.frame3.destroy()
        self.frame3 = Frame(self.frame2)
        self.frame3.grid(row=2, column=0, columnspan=4, sticky=W)
        super().att(self.usr, self.frame3)

    def det(self):
        self.frame3.destroy()
        self.frame3 = Frame(self.frame2)
        self.frame3.grid(row=2, column=0, columnspan=4, sticky=W)
        super().details(self.usr, self.frame3)

    def error1(self, frame1, new):
        if self.usr == '':
            new.config(text='Enter the Username')
            new.grid(row=4, column=1)
        elif self.pas == '':
            new.config(text='Enter the Password')
            new.grid(row=4, column=1)
        else:
            self.check1(new, frame1)

    def inp(self):
        self.pas = self.pa.get()
        self.usr = self.un.get()

    def func3(self, frame1):

        self.new = Label(frame1)

        def log1():
            self.inp()
            self.error1(frame1, self.new)

        frame1.grid(row=0, column=1, sticky=N)

        wc = Label(frame1, text="LOGIN FOR STUDENT",
                   relief="raised", height="5", width="100")
        wc.grid(row=0, column=1)

        uname = Label(frame1, text="Enter Your Username : ", width=50)
        uname.grid(row=1, column=1, sticky=W)

        passw = Label(frame1, text="Enter Your Password : ", width=50)
        passw.grid(row=2, column=1, sticky=W)

        self.un = Entry(frame1)
        self.un.grid(row=1, column=1)

        self.pa = Entry(frame1)
        self.pa.grid(row=2, column=1)

        sample = Button(frame1, text="login", command=log1)
        sample.grid(row=3, column=1)
