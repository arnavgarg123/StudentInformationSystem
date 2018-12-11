from tkinter import *
import AdminFunction
import mysql.connector 


class admin(AdminFunction.adminfunc):

    def check(self, new, frame1):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="adminlogin"
        )

        myc = mydb.cursor()
        myc.execute("SELECT * FROM login")
        
        for i in myc:
            if self.usr == i[0] and self.pas == i[1]:
                flag = 0
                for i in frame1.winfo_children():
                    i.destroy()

                self.frame2 = Frame(frame1)
                self.frame2.grid()
                self.frame3 = Frame(self.frame2)
                wc = Label(self.frame2, text="Student's Personal Information",
                           relief="raised", height="5", width="100")
                wc.grid(row=0, column=0, columnspan=5, sticky=N)

                button1 = Button(self.frame2, text="Details", height="10",width="16", bg="white", command=lambda: detail())
                button1.grid(row=1, column=0)

                button2 = Button(
                    self.frame2, text="Attendance", height="10", width="16", bg="white", command=lambda: atten())
                button2.grid(row=1, column=1)

                button3 = Button(
                    self.frame2, text="Academic report", height="10", width="16", bg="white", command=lambda: acad())
                button3.grid(row=1, column=2)
                button4 = Button(
                    self.frame2, text="Fee Details", height="10", width="16", bg="white", command=lambda: fees())
                button4.grid(row=1, column=3)
                button5 = Button(
                    self.frame2, text="New Student", height="10", width="16", bg="white", command=lambda: newstu())
                button5.grid(row=1, column=4)

                def newstu():
                    self.newstud()

                def fees():
                    self.fee1()

                def acad():
                    self.aca1()

                def atten():
                    self.atte1()

                def detail():
                    self.det1()

                break

                
            else:
                flag = 1
            if flag == 1:
                new.config(text="Invalid Username OR Password")
                new.grid(row=4, column=1)

    def newstud(self):
        self.frame3.destroy()
        self.frame3 = Frame(self.frame2)
        self.frame3.grid(row=2, column=0, columnspan=5, sticky=W)
        super().newst(self.frame3) 

    def fee1(self):
        self.frame3.destroy()
        self.frame3 = Frame(self.frame2)
        self.frame3.grid(row=2, column=0, columnspan=5, sticky=W)
        super().fee(self.frame3)  

    def aca1(self):
        self.frame3.destroy()
        self.frame3 = Frame(self.frame2)
        self.frame3.grid(row=2, column=0, columnspan=5, sticky=W)
        super().aca(self.frame3)

    def atte1(self):
        self.frame3.destroy()
        self.frame3 = Frame(self.frame2)
        self.frame3.grid(row=2, column=0, columnspan=40, sticky=W)
        super().att(self.frame3)

    def det1(self):
        self.frame3.destroy()
        self.frame3 = Frame(self.frame2)
        self.frame3.grid(row=2, column=0, columnspan=5, sticky=W)
        super().details(self.frame3)

    def error(self, frame1, new):
        if self.usr == '':
            new.config(text='Enter the Username')
            new.grid(row=4, column=1)
        elif self.pas == '':
            new.config(text='Enter the Password')
            new.grid(row=4, column=1)
        else:
            self.check(new, frame1)

    def inp(self):
        self.pas = self.pa.get()
        self.usr = self.un.get()

    def func2(self, frame1):

        self.new = Label(frame1)

        def log():
            self.inp()
            self.error(frame1, self.new)

        frame1.grid(row=0, column=1, sticky=N)

        wc = Label(frame1, text="LOGIN FOR ADMIN",
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

        sample = Button(frame1, text="login", command=log)
        sample.grid(row=3, column=1)
