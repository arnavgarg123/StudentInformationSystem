from tkinter import *
import Home
import Admin
import Student


class fp(Home.home, Admin.admin, Student.student):

    def maingui(self):

        self.top = Tk()
        self.top.geometry("870x630")
        self.top.title("Student Information System")

        frame = Frame(self.top)
        frame.grid(row=0, sticky=W)

        self.frame1 = Frame(self.top)

        button1 = Button(frame, text="Home", height="13",
                         width="20", command=lambda: self.ho())
        button1.grid(row=0)

        button2 = Button(frame, text="Admin", height="13",
                         width="20", command=lambda: self.Ad())
        button2.grid(row=1)

        button3 = Button(frame, text="Student", height="13",
                         width="20", command=lambda: self.st())
        button3.grid(row=2)

        button4 = Button(frame, text="Exit", height="13",
                         width="20", fg="red", command="exit")
        button4.grid(row=3)

        super().func1(self.frame1)

        self.top.mainloop()

    def ho(self):
        self.frame1.destroy()
        self.frame1 = Frame(self.top)
        super().func1(self.frame1)

    def Ad(self):
        self.frame1.destroy()
        self.frame1 = Frame(self.top)
        super().func2(self.frame1)

    def st(self):
        self.frame1.destroy()
        self.frame1 = Frame(self.top)
        super().func3(self.frame1)


a = fp()
a.maingui()
