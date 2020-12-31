
class GradeSystemFunctionStudent(object):#�ǥͥ\��
    def __init__(self, master=None):
        self.root = master #�w�q�����ܼ�root
        self.root.geometry('%dx%d' % (1000, 800))
        self.createPage()  
    def createPage(self):#�D���� 
        self.SearchPage = SearchFrame(self.root)
        self.OutputPage = OutputFrame(self.root)
        self.ListCoursePage = ListCourseFrame(self.root)
        self.ListCourseStudentPage = ListCourseStudentFrame(self.root)
        self.SearchPage.pack() #�X�{"�d�ߦ��Z"������
        self.menu = Menu(self.root)#�Ыص�� 
        self.menu.add_command(label='�d�ߦ��Z',font=10, command = self.SearchData)
        self.menu.add_command(label='���ͦ��Z��',font=10, command = self.OutputData)
        self.menu.add_command(label='�C�X�ҵ{�M��',font=10,command = self.ListCourse)
        self.menu.add_command(label='�C�X�ҵ{�ǥ�',font=10,command = self.ListCourseStudent)
        self.menu.add_command(label='�����ϥΪ�',font=10, command = self.ChangeUser)  
        self.root['menu'] = self.menu#������       
    def SearchData(self):
        self.SearchPage.pack()
        self.OutputPage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
    def OutputData(self):
        self.SearchPage.pack_forget()
        self.OutputPage.pack()   
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
    def ListCourse(self): 
        self.SearchPage.pack_forget()
        self.OutputPage.pack_forget()
        self.ListCoursePage.pack()
        self.ListCourseStudentPage.pack_forget()
    def ListCourseStudent(self):
        self.SearchPage.pack_forget()
        self.OutputPage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack()
    def ChangeUser(self):
        self.menu.destroy()
        self.SearchPage.destroy()
        self.OutputPage.destroy()
        self.ListCoursePage.destroy()
        self.ListCourseStudentPage.destroy()
        GradeSystemLogin(self.root)


class SearchFrame(Frame): #�d�߭���,�~��Frame
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #�w�q�����ܼ�root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10)
        self.E6 = Entry(self,font=10,show="*")
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '�Ǧ~: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self,  font=10,text = '�Ǵ�: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self,  font=10,text = '�ҵ{�N�X: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=E)
        Label(self,  font=10,text = '�Ǹ�: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Label(self,  font=10,text = '�ϥΪ̦W��: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)
        Label(self,  font=10,text = '�K�X: ').grid(row=6, stick=W, pady=10)
        self.E6.grid(row=6, column=1, stick=E)
        Button(self, font=10, text='�d��',command=self.search).grid(row=7, column=1, stick=E, pady=10)
    def search(self):
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        identify = self.E4.get()
        username = self.E5.get()
        password = self.E6.get()
        if  self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(identify) or self.spacejudge(username) or self.spacejudge(password):
            showinfo(title='����', message ="���@��J���i����")
        else:
            self.searchInfo(year,semester,num,identify,username,password)
    def searchInfo(self,year,semester,num,identify,username,password):
        temp=0
        f = open('./�ҵ{��T.csv','r',encoding='utf-8')#���n!�n��榡��UTF-8��excel�ɤ~�iŪ��
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<5:
                break
            if info[0]==year and info[1]==semester and info[2] ==num:
                temp=1
                classname=info[3]
                f.close()
        if temp==0:
            showinfo(title='���~',message ="�S�����ҵ{!")
            f.close()
            return
        else:
            f.close()
        temp3=0
        f = open('./�b���K�X.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==username and info[1] ==password and info[2] =='1' and info[5]==identify:
                temp3=1
                f.close()
            if info[0] ==username and info[1] ==password and info[2]=='3':
                temp3=1
                f.close()
        if temp3==0:
            showinfo(title='���~', message ="�����P���d�߾ǥͤ���")
            f.close
            return
        else:
            f.close
        f = open('./�ǥ͸�T.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num and info[3] ==identify and info[6]=="1":
                showinfo(title='�d�ߵ��G',message ="�m�W�G"+info[4] +"\n�Ǹ�:"+info[3] +"\n�ҵ{:"+classname +"\n���Z:"+info[5] )
                f.close()
                return
        showinfo(title='����', message ="�S�����ǥͪ����Z")
        f.close()
        return
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1


class ListCourseFrame(Frame):
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #�w�q�����ܼ�root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '�Ǧ~: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '�Ǵ�: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        self.tree=ttk.Treeview(self)#���
        self.tree["columns"]=("�N�X","�W��","�Ǥ�","�б�","����")
        self.tree.column("�N�X",width=100)   #��ܦC,�����
        self.tree.column("�W��",width=100)
        self.tree.column("�Ǥ�",width=100)
        self.tree.column("�б�",width=100)
        self.tree.column("����",width=100)     
        self.tree.heading("�N�X",text="�N�X")  #��ܿ��Y
        self.tree.heading("�W��",text="�W��")
        self.tree.heading("�Ǥ�",text="�Ǥ�")
        self.tree.heading("�б�",text="�б�")
        self.tree.heading("����",text="����")
        self.tree.grid(row=3, column=1, stick=W, pady=10)
        Button(self, font=10, text='�d��',command=self.search).grid(row=6, column=1, stick=E, pady=10)
    def search(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#�R����椺����
        year = self.E1.get()
        semester = self.E2.get()
        if self.spacejudge(year) or self.spacejudge(semester):
            showinfo(title='����', message ="���@��J���i����")
        else:
            self.searchInfo(year,semester)
    def searchInfo(self,year,semester):
        temp=0
        i=0
        f = open('./�ҵ{��T.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester:
                temp=1
                self.tree.insert("",i,text="�ҵ{" ,values=(info[2],info[3],info[4],info[5],info[6])) #���J���
                i+=1
        if temp==0:
            showinfo(title='����', message ="�S�����Ǵ��ҵ{���T��")
            f.close()
            return
        else:
            showinfo(title='����', message ="�w�C�X���")
            f.close()
            return
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1