from tkinter import *
import mysql.connector


class adminfunc:
    def details(self, frame3):
        lb = Listbox(frame3, height=20, width=50)
        lb.grid(row=0, column=0, sticky=W,rowspan=3)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1,rowspan=3 ,sticky="NS")
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
        myc2.execute("SELECT * FROM info")
        inc=0
        inc1=1
        for j in myc2:
            inc=0
            lb.insert(END,"Student number : "+str(inc1))
            inc1=inc1+1
            lb.insert(END," ")
            for i in myc1:
                
                lb.insert(END, i[0] + " => " + str(j[inc]))
                inc = inc + 1
            lb.insert(END," ")
            myc1.execute("DESC info")

        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)
        def read1():
            self.inpu1()
            mydb3 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
            )
            myc3 = mydb3.cursor()
            myc3.execute("SELECT * FROM info")
            flag=0
            
            for i in myc3:
                if i[0]==self.en1:
                    lab1=Label(frame3, text="                      ")
                    lab1.grid(row=2,column=2,sticky=N)
                    flag=0
                    self.execut1(frame3,  self.en1,lb,scrollbar)
                    break
                else:
                    flag=1
            if flag==1:
                lab1 = Label(frame3, text="No such student exists")
                lab1.grid(row=2,column=2,sticky=N)
        lab1 = Label(frame3, text="Enter student name to view details")
        lab1.grid(row=0,column=2,sticky=S)
        self.en = Entry(frame3,width=30)
        self.en.grid(row=1, column=2,sticky=N)
        sample = Button(frame3, text="Select",command=read1, bg="green")
        sample.grid(row=1,column=3,sticky=N)

        def read():
            self.inpu()
            self.execut(frame3, myc2, self.val2, self.en1, self.val1, mydb2)

        lab1 = Label(frame3, text="Entry field with wrong details")
        lab1.grid(row=4)
        self.ent = Entry(frame3)
        self.ent.grid(row=4, column=1,columnspan=2,sticky=W)
        lab2 = Label(frame3, text="Enter the correct details")
        lab2.grid(row=5)
        self.val = Entry(frame3)
        self.val.grid(row=5, column=1,columnspan=2,sticky=W)
        lab3 = Label(frame3, text="Enter the name")
        lab3.grid(row=6)
        self.valu = Entry(frame3)
        self.valu.grid(row=6, column=1,columnspan=2,sticky=W)
        sample = Button(frame3, text="change", command=read, bg="green")
        sample.grid(row=7)

    def inpu(self):
        self.en1 = self.ent.get()
        self.val1 = str(self.val.get())
        self.val2 = str(self.valu.get())

    def execut(self, frame3, myc2, usr, en1, val1, mydb2):
        if(self.en1 == "grade"):
            labe2 = Label(frame3, text="Can't change this field")
            labe2.grid(row=7)
        elif(self.en1 == "username"):
            labe2 = Label(frame3, text="Can't change this field")
            labe2.grid(row=7)
        else:
            myc2.execute("UPDATE info SET %s='%s' WHERE name='%s'" %
                         (en1, val1, usr))
            mydb2.commit()
            labe2 = Label(frame3, text="Press Details again to refresh")
            labe2.grid(row=8)


    def inpu1(self):
        self.en1 = self.en.get()
        
    def execut1(self, frame3, en1,lb,scrollbar):
        lb.destroy()
        scrollbar.destroy()
        lb = Listbox(frame3, height=20, width=50)
        lb.grid(row=0, column=0, sticky=W,rowspan=3)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1,rowspan=3 ,sticky="NS")
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
        myc2.execute("SELECT * FROM info WHERE username='%s'" % (en1))
        j = myc2.fetchone()
        inc = 0
        for i in myc1:
            lb.insert(END, i[0] + " => " + str(j[inc]))
            inc = inc + 1

        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)

    def att(self, frame3):
        scrollY = Scrollbar(frame3)
        canvas=Canvas(frame3,width="5i",height="5i",yscrollcommand = scrollY.set)
        scrollY.config(command=canvas.yview)
        draw=Frame(canvas)
        draw.grid()

        canvas.create_window(0,0,window=draw,anchor='nw')

        
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
        myc2.execute("SELECT * FROM attendance")

        def read():
            mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
            )
            myc1 = mydb1.cursor()
            myc1.execute("DESC attendance")
            self.input1()
            flag=1
            if self.en1=="":
                lab3 = Label(canvas, text="Enter the correct class",relief=GROOVE)
                lab3.place(x=10,y=0)
            elif self.en1=="username":
                lab3 = Label(canvas, text="Enter the correct class",relief=GROOVE)
                lab3.place(x=10,y=0)
            else:
                for i in myc1:   
                    if self.en1==i[0]:
                        flag=0
                        break
                
                if flag==0:
                    self.execute1(canvas, myc2, self.en1, mydb2,frame3)
                else:
                    lab3 = Label(canvas, text="Enter the correct class",relief=GROOVE)
                    lab3.place(x=10,y=0)

        lab3 = Label(canvas, text="Enter the name of class",relief=GROOVE)
        lab3.place(x=10,y=0)
        self.valu = Entry(canvas)
        self.valu.place(x=180, y=0)
        sample = Button(canvas, text="Select", command=read, bg="green")
        sample.place(x=330,y=0)
        scrollY.grid(row=0,column=2,sticky=NS)
        canvas.grid(row=0,column=1)
        frame3.update()
        canvas.config(scrollregion=canvas.bbox("all"))

        
        

    def input1(self):
        self.en1 = self.valu.get()
    def execute1(self,canvas, myc2, en1, mydb2,frame3):
        inc=25
        def press(a):
            self.attupd(a,self.en1,canvas,frame3)
        k=myc2.fetchall()
        v=[]
        vi=[0,0]
        for i in range(len(k)):
            v=v+vi
        myc2.execute("SELECT * FROM attendance")
        for i in myc2:
            if i[0]=='Total':
                continue
            lb=Label(canvas,text=i[0])
            lb.place(x=10,y=inc)

            v[int(inc/25)-1]=Button(canvas, text="Present",command=lambda inc=inc:press(int(inc/25)-1), bg="green")
            v[int(inc/25)-1].place(x=70,y=inc)
            inc=inc+25
        

        blast=Button(canvas, text="Submit",command=lambda inc=inc:press(10))
        blast.place(x=10,y=inc+25)
        frame3.update()
        canvas.config(scrollregion=canvas.bbox("all"))

    def attupd(self,a,clas,canvas,frame3):
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
        myc2 = mydb2.cursor()
        myc2.execute("SELECT * FROM attendance")
        j=myc2.fetchall()
        myc1 = mydb1.cursor()
        myc1.execute("SELECT %s FROM attendance WHERE username='%s'" %(str(clas),str(j[a][0])))
        k=myc1.fetchone()
        myc1.execute("UPDATE  attendance SET %s='%s' WHERE username='%s'" %(str(clas),str(int(k[0])+1),str(j[a][0])))
        mydb1.commit()
        if a==10:
            lab3 = Label(canvas, text="Submited Successfully",relief=GROOVE)
            lab3.place(x=22,y=1)
        frame3.update()
        canvas.config(scrollregion=canvas.bbox("all"))










    def aca(self, frame3):
        lb = Listbox(frame3, height=20, width=50)
        lb.grid(row=0, column=0, sticky=W,rowspan=3)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1,rowspan=3 ,sticky="NS")
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
        myc2.execute("SELECT * FROM academics")
        inc=0
        inc1=1
        for j in myc2:
            inc=0
            lb.insert(END,"Student number : "+str(inc1))
            inc1=inc1+1
            lb.insert(END," ")
            for i in myc1:
                
                lb.insert(END, i[0] + " => " + str(j[inc]))
                inc = inc + 1
            lb.insert(END," ")
            myc1.execute("DESC academics")

        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)
        def read1():
            self.iinpu11()
            mydb3 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
            )
            myc3 = mydb3.cursor()
            myc3.execute("SELECT * FROM academics")
            flag=0
            
            for i in myc3:
                if i[0]==self.en1:
                    lab1=Label(frame3, text="                      ")
                    lab1.grid(row=2,column=2,sticky=N)
                    flag=0
                    self.eexecut11(frame3,  self.en1,lb,scrollbar)
                    break
                else:
                    flag=1
            if flag==1:
                lab1 = Label(frame3, text="No such student exists")
                lab1.grid(row=2,column=2,sticky=N)
        lab1 = Label(frame3, text="Enter student username to view details")
        lab1.grid(row=0,column=2,sticky=S)
        self.en = Entry(frame3,width=30)
        self.en.grid(row=1, column=2,sticky=N)
        sample = Button(frame3, text="Select",command=read1, bg="green")
        sample.grid(row=1,column=3,sticky=N)

        def read():
            self.iinpuu()
            self.eexecutt(frame3, myc2, self.val2, self.en1, self.val1, mydb2)

        lab1 = Label(frame3, text="Entry field with wrong details")
        lab1.grid(row=4)
        self.ent = Entry(frame3)
        self.ent.grid(row=4, column=1,columnspan=2,sticky=W)
        lab2 = Label(frame3, text="Enter the correct details")
        lab2.grid(row=5)
        self.val = Entry(frame3)
        self.val.grid(row=5, column=1,columnspan=2,sticky=W)
        lab3 = Label(frame3, text="Enter the username")
        lab3.grid(row=6)
        self.valu = Entry(frame3)
        self.valu.grid(row=6, column=1,columnspan=2,sticky=W)
        sample = Button(frame3, text="change", command=read, bg="green")
        sample.grid(row=7)

    def iinpuu(self):
        self.en1 = self.ent.get()
        self.val1 = str(self.val.get())
        self.val2 = str(self.valu.get())

    def eexecutt(self, frame3, myc2, usr, en1, val1, mydb2):
        if(self.en1 == "grade"):
            labe2 = Label(frame3, text="Can't change this field")
            labe2.grid(row=7)
        elif(self.en1 == "username"):
            labe2 = Label(frame3, text="Can't change this field")
            labe2.grid(row=7)
        else:
            myc2.execute("UPDATE academics SET %s='%s' WHERE username='%s'" %
                         (en1, val1, usr))
            mydb2.commit()
            labe2 = Label(frame3, text="Press academics again to refresh")
            labe2.grid(row=8)


    def iinpu11(self):
        self.en1 = self.en.get()
        
    def eexecut11(self, frame3, en1,lb,scrollbar):
        lb.destroy()
        scrollbar.destroy()
        lb = Listbox(frame3, height=20, width=50)
        lb.grid(row=0, column=0, sticky=W,rowspan=3)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1,rowspan=3 ,sticky="NS")
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
        myc2.execute("SELECT * FROM academics WHERE username='%s'" % (en1))
        j = myc2.fetchone()
        inc = 0
        for i in myc1:
            lb.insert(END, i[0] + " => " + str(j[inc]))
            inc = inc + 1

        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)


    def fee(self, frame3):
        lb = Listbox(frame3, height=20, width=50)
        lb.grid(row=0, column=0, sticky=W,rowspan=3)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1,rowspan=3 ,sticky="NS")
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
        myc2.execute("SELECT * FROM fee")
        inc=0
        inc1=1
        for j in myc2:
            inc=0
            lb.insert(END,"Student number : "+str(inc1))
            inc1=inc1+1
            lb.insert(END," ")
            for i in myc1:
                
                lb.insert(END, i[0] + " => " + str(j[inc]))
                inc = inc + 1
            lb.insert(END," ")
            myc1.execute("DESC fee")

        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)
        def read1():
            self.iinpu1()
            mydb3 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
            )
            myc3 = mydb3.cursor()
            myc3.execute("SELECT * FROM fee")
            flag=0
            
            for i in myc3:
                if i[0]==self.en1:
                    lab1=Label(frame3, text="                      ")
                    lab1.grid(row=2,column=2,sticky=N)
                    flag=0
                    self.eexecut1(frame3,  self.en1,lb,scrollbar)
                    break
                else:
                    flag=1
            if flag==1:
                lab1 = Label(frame3, text="No such student exists")
                lab1.grid(row=2,column=2,sticky=N)
        lab1 = Label(frame3, text="Enter student username to view details")
        lab1.grid(row=0,column=2,sticky=S)
        self.en = Entry(frame3,width=30)
        self.en.grid(row=1, column=2,sticky=N)
        sample = Button(frame3, text="Select",command=read1, bg="green")
        sample.grid(row=1,column=3,sticky=N)

        def read():
            self.iinpu()
            self.eexecut(frame3, myc2, self.val2, self.en1, self.val1, mydb2)

        lab1 = Label(frame3, text="Entry field with wrong details")
        lab1.grid(row=4)
        self.ent = Entry(frame3)
        self.ent.grid(row=4, column=1,columnspan=2,sticky=W)
        lab2 = Label(frame3, text="Enter the correct details")
        lab2.grid(row=5)
        self.val = Entry(frame3)
        self.val.grid(row=5, column=1,columnspan=2,sticky=W)
        lab3 = Label(frame3, text="Enter the username")
        lab3.grid(row=6)
        self.valu = Entry(frame3)
        self.valu.grid(row=6, column=1,columnspan=2,sticky=W)
        sample = Button(frame3, text="change", command=read, bg="green")
        sample.grid(row=7)

    def iinpu(self):
        self.en1 = self.ent.get()
        self.val1 = str(self.val.get())
        self.val2 = str(self.valu.get())

    def eexecut(self, frame3, myc2, usr, en1, val1, mydb2):
        if(self.en1 == "grade"):
            labe2 = Label(frame3, text="Can't change this field")
            labe2.grid(row=7)
        elif(self.en1 == "username"):
            labe2 = Label(frame3, text="Can't change this field")
            labe2.grid(row=7)
        else:
            myc2.execute("UPDATE fee SET %s='%s' WHERE username='%s'" %
                         (en1, val1, usr))
            mydb2.commit()
            labe2 = Label(frame3, text="Press fee again to refresh")
            labe2.grid(row=8)


    def iinpu1(self):
        self.en1 = self.en.get()
        
    def eexecut1(self, frame3, en1,lb,scrollbar):
        lb.destroy()
        scrollbar.destroy()
        lb = Listbox(frame3, height=20, width=50)
        lb.grid(row=0, column=0, sticky=W,rowspan=3)
        scrollbar = Scrollbar(frame3)
        scrollbar.grid(row=0, column=1,rowspan=3 ,sticky="NS")
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
        myc2.execute("SELECT * FROM fee WHERE username='%s'" % (en1))
        j = myc2.fetchone()
        inc = 0
        for i in myc1:
            lb.insert(END, i[0] + " => " + str(j[inc]))
            inc = inc + 1

        lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)

    def newst(self,frame3):
        def inpread():
            self.takeinp()
            self.makeexe()
        
        lb2=Label(frame3,text="New Student Password : ")
        lb2.grid(row=2,column=0,sticky=W)
        self.en2=Entry(frame3)
        self.en2.grid(row=1,column=1)
        lb3=Label(frame3,text="New Student Name : ")
        lb3.grid(row=1,column=0,sticky=W)
        self.en3=Entry(frame3)
        self.en3.grid(row=2,column=1)
        lb4=Label(frame3,text="New Student Fathersname : ")
        lb4.grid(row=3,column=0,sticky=W)
        self.en4=Entry(frame3)
        self.en4.grid(row=3,column=1)
        lb5=Label(frame3,text="New Student Mothersname : ")
        lb5.grid(row=4,column=0,sticky=W)
        self.en5=Entry(frame3)
        self.en5.grid(row=4,column=1)
        lb6=Label(frame3,text="New Student Age : ")
        lb6.grid(row=5,column=0,sticky=W)
        self.en6=Entry(frame3)
        self.en6.grid(row=5,column=1)
        lb7=Label(frame3,text="New Student Gender : ")
        lb7.grid(row=6,column=0,sticky=W)
        self.en7=Entry(frame3)
        self.en7.grid(row=6,column=1)
        lb8=Label(frame3,text="New Student Regno : ")
        lb8.grid(row=7,column=0,sticky=W)
        self.en8=Entry(frame3)
        self.en8.grid(row=7,column=1)
        lb9=Label(frame3,text="New Student Course : ")
        lb9.grid(row=8,column=0,sticky=W)
        self.en9=Entry(frame3)
        self.en9.grid(row=8,column=1)
        lb10=Label(frame3,text="New Student Branch : ")
        lb10.grid(row=9,column=0,sticky=W)
        self.en10=Entry(frame3)
        self.en10.grid(row=9,column=1)
        lb11=Label(frame3,text="New Student Year : ")
        lb11.grid(row=10,column=0,sticky=W)
        self.en11=Entry(frame3)
        self.en11.grid(row=10,column=1)
        lb12=Label(frame3,text="New Student Grade : ")
        lb12.grid(row=11,column=0,sticky=W)
        self.en12=Entry(frame3)
        self.en12.grid(row=11,column=1)
        button=Button(frame3,text="submit",command=inpread)
        button.grid(row=12,column=0,columnspan=2)
        
    def makeexe(self):
        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentlogin"
        )
        myc1 = mydb1.cursor()
        myc1.execute("INSERT INTO login values('%s','%s')" %(self.en03,self.en02))
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="arnav",
            database="studentinfo"
        )
        myc2 = mydb2.cursor()
        myc2.execute("INSERT INTO info values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(self.en03,self.en03,self.en04,self.en05,self.en06,self.en07,self.en08,self.en09,self.en010,self.en011,self.en012))
        myc2.execute("INSERT INTO academics values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(self.en03,'','','','','','','','',''))
        myc2.execute("INSERT INTO attendance values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(self.en03,'0','0','0','0','0','0','0','0','0'))
        myc2.execute("INSERT INTO fee values('%s','%s','%s')" %(self.en03,'0','0'))
        mydb1.commit()
        mydb2.commit()

    def takeinp(self):
        self.en02 = self.en2.get()
        self.en03 = self.en3.get()
        self.en04 = self.en4.get()
        self.en05 = self.en5.get()
        self.en06 = self.en6.get()
        self.en07 = self.en7.get()
        self.en08 = self.en8.get()
        self.en09 = self.en9.get()
        self.en010 = self.en10.get()
        self.en011 = self.en11.get()
        self.en012 = self.en12.get()