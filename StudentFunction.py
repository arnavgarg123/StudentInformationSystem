from tkinter import *
import mysql.connector


class studfunc:
    def details(self, usr, frame3):

        lb = Listbox(frame3, height=20, width=50)
        lb.grid(row=0, column=0, sticky=W)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1, sticky="NS")

        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
        )
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
        )
        myc1 = mydb1.cursor()
        myc1.execute("DESC info")
        myc2 = mydb2.cursor()
        myc2.execute("SELECT * FROM info WHERE username='%s'" % (usr))
        j = myc2.fetchone()
        inc = 0
        for i in myc1:
            lb.insert(END, i[0] + " => " + str(j[inc]))
            inc = inc + 1

        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)

        def read():
            self.inpuu()
            self.execut(frame3, myc2, usr, self.en1, self.val1, mydb2)
        lab1 = Label(frame3, text="Entry field with wrong details")
        lab1.grid(row=4)
        self.en = Entry(frame3)
        self.en.grid(row=4, column=3)
        lab2 = Label(frame3, text="Enter the correct details")
        lab2.grid(row=5)
        self.val = Entry(frame3)
        self.val.grid(row=5, column=3)
        sample = Button(frame3, text="change", command=read, bg="green")
        sample.grid(row=6)

    def inpuu(self):
        self.en1 = self.en.get()
        self.val1 = str(self.val.get())

    def execut(self, frame3, myc2, usr, en1, val1, mydb2):
        if(self.en1 == "grade"):
            labe2 = Label(frame3, text="Can't change this field")
            labe2.grid(row=7)
        elif(self.en1 == "username"):
            labe2 = Label(frame3, text="Can't change this field")
            labe2.grid(row=7)
        else:
            myc2.execute("UPDATE info SET %s='%s' WHERE username='%s'" %
                         (en1, val1, usr))
            mydb2.commit()
            labe2 = Label(frame3, text="Press Details again to refresh")
            labe2.grid(row=7)

    def att(self, usr, frame3):
        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
        )
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
        )
        myc1 = mydb1.cursor()
        myc1.execute("DESC attendance")
        myc2 = mydb2.cursor()
        lb = Listbox(frame3, height=30, width=50)
        lb.grid(row=0, column=0, sticky=W)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1, sticky="NS")
        myc2.execute("SELECT * FROM attendance WHERE username='%s'" % (usr))
        j = myc2.fetchone()
        myc2.execute("SELECT * FROM attendance WHERE username='Total'")
        k = myc2.fetchone()
        inc = 1
        for i in myc1:
            if i[0] == "username":
                continue
            elif i[0] == "Total":
                continue
            lb.insert(END, i[0] + " => " +
                      str(int(j[inc]) / int(k[inc]) * 100))
            inc = inc + 1
        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)

    def aca(self, usr, frame3):

        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
        )

        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
        )
        myc1 = mydb1.cursor()
        myc1.execute("DESC academics")
        myc2 = mydb2.cursor()

        lb = Listbox(frame3, height=30, width=50)
        lb.grid(row=0, column=0, sticky=W)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1, sticky="NS")
        myc2.execute("SELECT * FROM academics WHERE username='%s'" % (usr))
        j = myc2.fetchone()
        inc = 1
        for i in myc1:
            if i[0] == "username":
                continue
            lb.insert(END, i[0] + " => " + str(j[inc]))
            inc = inc + 1
        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)

    def fee(self, usr, frame3):

        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
        )

        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
        )
        myc1 = mydb1.cursor()
        myc1.execute("DESC fee")
        myc2 = mydb2.cursor()

        lb = Listbox(frame3, height=10, width=50)
        lb.grid(row=0, column=0, sticky=W)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1, sticky="NS")
        myc2.execute("SELECT * FROM fee WHERE username='%s'" % (usr))
        j = myc2.fetchone()
        y = j[1]
        z = j[2]
        inc = 1
        for i in myc1:
            if i[0] == "username":
                continue
            elif i[0] == "Total":
                continue
            lb.insert(END, i[0] + " => " + str(j[inc]))
            inc = inc + 1
        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)
        lab2 = Label(frame3, text="Enter Ammount to pay")
        lab2.grid(row=1)
        self.ent = Entry(frame3)
        self.ent.grid(row=2, column=0)

        def read():
            self.input()
            self.execut12(frame3, myc2, usr, self.en2, mydb2, y, z)
        sample = Button(frame3, text="pay", fg="green", command=read)
        sample.grid(row=3)

    def input(self):
        self.en2 = self.ent.get()

    def execut12(self, frame3, myc2, usr, en2, mydb2, y, z):
        if int(y) < int(en2):
            labe2 = Label(frame3, text="  Value exceeded the ammount to pay  ")
            labe2.grid(row=4)
        else:
            myc2.execute("UPDATE fee SET Pending='%s' WHERE username='%s'" %
                         (str(int(y) - int(en2)), usr))
            myc2.execute("UPDATE fee SET Paid='%s' WHERE username='%s'" %
                         (str(int(z) + int(en2)), usr))
            mydb2.commit()

            labe2 = Label(frame3, text="Press 'Fee Details' again to refresh")
            labe2.grid(row=4)
