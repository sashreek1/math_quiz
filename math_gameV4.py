from tkinter import *
from tkinter import messagebox

class questions() :
    def __init__(self,question,answer,options):
        self.question = question
        self.answer = answer
        self.options = options
class math_app():
    def __init__(self):
        self.numteams = 0
        self.teamlist = []
        self.pointslist = None
        self.sub_counter = 0
        self.quelst = []
        self.numcorrectans = 0
        self.prev_ques = 0
        self.donelst = []
        self.cur_team = None
        self.cur_ans = None

    def get_ques(self):
        que_file = open("math_app_ques_csv", 'r')
        text = que_file.read()
        text = text.split('\t\t,\t\t')
        for i in range(len(text)):
            if i % 6 == 0:
                question = text[i]
                oplist = []
                continue
            if i % 6 == 1 or i % 6 == 2 or i % 6 == 3 or i % 6 == 4:
                oplist.append(text[i])
                continue
            if i % 6 == 5:
                ans = int(text[i])
            instance = questions(question, ans, oplist)
            self.quelst.append(instance)


    def placeques(self, frame, text):
        q = Label(frame, text=text, anchor=CENTER)
        q.place(x=10,y=10)
        q.config(font=("Times",28,"bold"))

    def placeans(self, frame, text):
        for i in range(len(text)):
            q = Label(frame, text=text[i], anchor=CENTER)
            q.place(x=20, y=40*3*i)
            q.config(font=("Times",28,"bold"))

    def sub (self,text,root):
        self.numteams = int(text)
        root.destroy()
        for i in range(self.numteams):
            self.teamlist.append(chr(65+i))
        self.pointslist = [0] * len(self.teamlist)
        self.get_ques()
        self.gui()

    def no_teams(self):
        root = Tk()
        root.geometry("600x100+700+400")
        root.resizable(False,False)
        root.title("Number Of Teams")

        l = Label(root, text="Enter the number of teams that are playing ")
        l.place(x=20,y =20)
        l.config(font=26)

        t = Entry(width=10)
        t.place(x=450,y=20)

        b = Button (text="Submit",command= lambda : self.sub(t.get(),root))
        b.place(x=270,y=60)

        root.mainloop()
    def disp_win(self):
        window = Tk()
        window.geometry("500x400")
        window.title("Math Game")
        labelfont = ('Ubuntu', 20, 'bold')
        text = "The winner is/are : group "
        text1 = "The team/s at second place is/are "
        win_list = []
        sec_list = []
        ma = max(self.pointslist)
        for i in range(len(self.pointslist)):
            try:
                win_list.append(chr(self.pointslist.index(ma)+65))
                self.pointslist[self.pointslist.index(ma)] = -100
                print(win_list)
                continue
            except:
                break
        ma = max(self.pointslist)
        for i in range(len(self.pointslist)):
            try:
                sec_list.append(chr(self.pointslist.index(ma) + 65))
                self.pointslist[self.pointslist.index(ma)] = -100
                print(sec_list)
                continue
            except:
                break
        text+=' , '.join(win_list)
        text1+=' , '.join(sec_list)
        Label(window, text=text, font=labelfont).place(x=80,y=150)
        Label(window,text=text1, font =('Ubuntu', 14, 'bold')).place(x=80,y=190)



    def sub_func(self,ansvar,teamvar,f2,f3,root):
        ans = ansvar.get()
        team = teamvar.get()
        self.cur_team.set("Your group")
        self.cur_ans.set("Your option")
        ques_no = self.sub_counter//self.numteams
        if team in self.donelst:
            self.sub_counter -= 1
            messagebox.showerror("Error", "This team has already played")
        else:
            self.donelst.append(team)
            if self.sub_counter == (self.numteams*10)-1: # display the points table
                root.destroy()
                self.disp_win()
            if self.sub_counter % self.numteams == 0:
                self.numcorrectans = 0
            if self.numcorrectans == 0 and int(ans)==int(self.quelst[ques_no].answer):
                self.pointslist[int(ord(team)-65)] += 10
                self.numcorrectans+=1
            elif self.numcorrectans == 1 and int(ans)==int(self.quelst[ques_no].answer):
                self.pointslist[int(ord(team)-65)] += 5
                self.numcorrectans += 1
            elif self.numcorrectans == 2 and int(ans)==int(self.quelst[ques_no].answer):
                self.pointslist[int(ord(team)-65)] += 2
                self.numcorrectans += 1
        self.sub_counter+=1
        print(self.pointslist)
        ques_no = self.sub_counter // self.numteams
        if self.prev_ques!= ques_no:
            try:
                f2.destroy()
                f3.destroy()
                f2 = Frame(root, height=515, width=920, borderwidth=2)
                f2.place(x=7, y=10)
                f2.config(relief=RIDGE)
                f3 = Frame(root, height=515, width=920, borderwidth=2)
                f3.place(x=927, y=10)
                f3.config(relief=RIDGE)
                f2.pack_propagate(0)
                f3.pack_propagate(0)
                self.placeques(f2, self.quelst[ques_no].question)
                self.placeans(f3, self.quelst[ques_no].options)
                self.prev_ques = ques_no
                self.donelst = []
            except:
                pass

    def gui(self):
        root = Tk()
        root.geometry("1366x768")
        root.resizable(True,True)
        root.title("Math Game")
        labelfont = ('Ubuntu', 20, 'bold')

        f1 = Frame(root, height=460, width=1840, borderwidth=2)
        f1.place(x=7,y=540)
        f1.config(relief=SUNKEN)

        f2 = Frame(root, height=515, width=920, borderwidth=2)
        f2.place(x=7,y=10)
        f2.config(relief=RIDGE)
        f2.pack_propagate(0)

        f3 = Frame(root, height=515, width=920, borderwidth=2)
        f3.place(x=927, y=10)
        f3.config(relief=RIDGE)
        f3.pack_propagate(0)

        f4 = Frame(f1, height=445, width=650, borderwidth=2)
        f4.place(x=595, y=10)
        f4.config(relief=RIDGE)

        l1 = Label(f4, text="Pick your group : ")
        l1.place(x=80, y=40)
        l1.config(font=labelfont)
        l1.config(height=3, width=20)

        OPTIONS = self.teamlist
        self.cur_team = StringVar(root)
        self.cur_team.set("Your group")
        popupMenu = OptionMenu(f4, self.cur_team, *OPTIONS)
        popupMenu.place(x=357, y=72)
        popupMenu.config(font=labelfont)

        l1 = Label(f4, text="Pick your answer : ")
        l1.place(x=80, y=190)
        l1.config(font=labelfont)
        l1.config(height=3, width=20)

        OPTIONS = [1,2,3,4]
        self.cur_ans = StringVar(root)
        self.cur_ans.set("Your option")
        popupMenu = OptionMenu(f4, self.cur_ans, *OPTIONS)
        popupMenu.place(x=357, y=222)
        popupMenu.config(font=labelfont)

        self.placeques(f2, self.quelst[0].question)
        self.placeans(f3, self.quelst[0].options)

        b = Button(f4, text = "Submit", width=10, height=2, font = labelfont, command=lambda : self.sub_func(self.cur_ans,self.cur_team,f2,f3,root))
        b.place(x=220,y=350)


        root.mainloop()


instance = math_app()
instance.no_teams()
