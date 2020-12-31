
class GradeSystemFunctionStudent(object):#學生功能
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (1000, 800))
        self.createPage()  
    def createPage(self):#主頁面 
        self.SearchPage = SearchFrame(self.root)
        self.OutputPage = OutputFrame(self.root)
        self.ListCoursePage = ListCourseFrame(self.root)
        self.ListCourseStudentPage = ListCourseStudentFrame(self.root)
        self.SearchPage.pack() #出現"查詢成績"的介面
        self.menu = Menu(self.root)#創建菜單 
        self.menu.add_command(label='查詢成績',font=10, command = self.SearchData)
        self.menu.add_command(label='產生成績單',font=10, command = self.OutputData)
        self.menu.add_command(label='列出課程清單',font=10,command = self.ListCourse)
        self.menu.add_command(label='列出課程學生',font=10,command = self.ListCourseStudent)
        self.menu.add_command(label='切換使用者',font=10, command = self.ChangeUser)  
        self.root['menu'] = self.menu#菜單欄位       
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


class SearchFrame(Frame): #查詢頁面,繼承Frame
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10)
        self.E6 = Entry(self,font=10,show="*")
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self,  font=10,text = '課程代碼: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=E)
        Label(self,  font=10,text = '學號: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Label(self,  font=10,text = '使用者名稱: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)
        Label(self,  font=10,text = '密碼: ').grid(row=6, stick=W, pady=10)
        self.E6.grid(row=6, column=1, stick=E)
        Button(self, font=10, text='查詢',command=self.search).grid(row=7, column=1, stick=E, pady=10)
    def search(self):
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        identify = self.E4.get()
        username = self.E5.get()
        password = self.E6.get()
        if  self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(identify) or self.spacejudge(username) or self.spacejudge(password):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.searchInfo(year,semester,num,identify,username,password)
    def searchInfo(self,year,semester,num,identify,username,password):
        temp=0
        f = open('./課程資訊.csv','r',encoding='utf-8')#重要!要選格式為UTF-8的excel檔才可讀取
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<5:
                break
            if info[0]==year and info[1]==semester and info[2] ==num:
                temp=1
                classname=info[3]
                f.close()
        if temp==0:
            showinfo(title='錯誤',message ="沒有此課程!")
            f.close()
            return
        else:
            f.close()
        temp3=0
        f = open('./帳號密碼.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==username and info[1] ==password and info[2] =='1' and info[5]==identify:
                temp3=1
                f.close()
            if info[0] ==username and info[1] ==password and info[2]=='3':
                temp3=1
                f.close()
        if temp3==0:
            showinfo(title='錯誤', message ="身分與欲查詢學生不符")
            f.close
            return
        else:
            f.close
        f = open('./學生資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num and info[3] ==identify and info[6]=="1":
                showinfo(title='查詢結果',message ="姓名："+info[4] +"\n學號:"+info[3] +"\n課程:"+classname +"\n成績:"+info[5] )
                f.close()
                return
        showinfo(title='提示', message ="沒有此學生的成績")
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
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        self.tree=ttk.Treeview(self)#表格
        self.tree["columns"]=("代碼","名稱","學分","教授","類型")
        self.tree.column("代碼",width=100)   #表示列,不顯示
        self.tree.column("名稱",width=100)
        self.tree.column("學分",width=100)
        self.tree.column("教授",width=100)
        self.tree.column("類型",width=100)     
        self.tree.heading("代碼",text="代碼")  #顯示錶頭
        self.tree.heading("名稱",text="名稱")
        self.tree.heading("學分",text="學分")
        self.tree.heading("教授",text="教授")
        self.tree.heading("類型",text="類型")
        self.tree.grid(row=3, column=1, stick=W, pady=10)
        Button(self, font=10, text='查詢',command=self.search).grid(row=6, column=1, stick=E, pady=10)
    def search(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#刪除表格內元件
        year = self.E1.get()
        semester = self.E2.get()
        if self.spacejudge(year) or self.spacejudge(semester):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.searchInfo(year,semester)
    def searchInfo(self,year,semester):
        temp=0
        i=0
        f = open('./課程資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester:
                temp=1
                self.tree.insert("",i,text="課程" ,values=(info[2],info[3],info[4],info[5],info[6])) #插入資料
                i+=1
        if temp==0:
            showinfo(title='提示', message ="沒有此學期課程的訊息")
            f.close()
            return
        else:
            showinfo(title='提示', message ="已列出表格")
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