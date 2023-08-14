from tkinter import *
from tkinter import ttk
import pymysql
import os
from datetime import date


class service_request1:

    # ===================== ( interface ) واجهة البرنامج ===================== #

    def __init__(self, root):
        self.admintree2 = None
        self.root = root
        self.root.geometry('450x530')
        self.root.title('Service Request')
        self.root.configure(background="silver")
        title = Label(self.root,
                      text='[ مرسل التذكرة ]: ' + os.getenv("USERNAME"),
                      bg='#876159',
                      font=('Arial Rounded MT', 14),
                      fg="black"
                      )
        title.pack(fill=X)
    
        # ======================== (Variables) المتغيرات ======================== #
        self.CompanyName = StringVar()
        self.ServiceType = StringVar()
        self.DetailedServiceType = StringVar()
        self.ReferenceNumber = StringVar()
        self.DescriptionInfo = StringVar()
        self.Status = StringVar()

        # def clear(self):
        # self.combo_var.set('')
        # self.Text_var.set('')
        # self.Text2_var.set('')

        # =============================== ( Frame ) لوحة اختيار الطلب ================================ #
        Manage_Frame = Frame(self.root, bg='#FFFFFF')
        Manage_Frame.place(x=0, y=29, width=450, height=500)
        CompName = Label(Manage_Frame, text='اختر اسم الشركة', bg='white')
        CompName.pack(padx=10, pady=10)
        CompanyList = [
            "وادي جدة",
            "شركة تطمين السعودية للاستثمارات والمشاريع",
            "شركة المنطلقات الحديثة للاتصالات وتقنية المعلومات",
            "شركة التصوير الجزيئي الطبية",
            "المنظومة السعودية لتطوير التعليم والتدريب - صافية",
            "مدرسة جدة المتطورة لتعليم القيادة",

        ]
        ServiceList = [
            "مشكلة",
            "طلب"
        ]
        ProbList = [
            "الربط المحاسبي للتصنيف",
            "فشل في سير عمل معاملة",
            "اخرى"
        ]
        ReqList = [
            "انشاء حساب",
            "اضافة صلاحيات",
            "اضافة تصنيف",
            "اضافة مجموعة عناصر",
            "اضافة مجموعة اصول",
            "اخرى"
        ]
        CompList = ttk.Combobox(Manage_Frame, values=CompanyList, textvariable=self.CompanyName,width=200,justify=RIGHT)
        CompList.pack(padx=10, pady=10)
        SrvcType = Label(Manage_Frame, text='حدد نوع الخدمة', bg='white')
        SrvcType.pack(padx=5, pady=5)
        SrvcList = ttk.Combobox(Manage_Frame, values=ServiceList, textvariable=self.ServiceType)
        SrvcList.pack(padx=5, pady=5)

        def choosing(e):
            Service = SrvcList.get()
            if Service == "مشكلة":
                combo.config(values=ProbList)
                Detailed.config(text=" حدد نوع المشكلة")

            else:
                combo.config(values=ReqList)
                Detailed.config(text=" حدد نوع الطلب")

        Detailed = Label(Manage_Frame, bg='white')
        Detailed.pack(padx=5, pady=5)
        combo = ttk.Combobox(Manage_Frame, values=[" "], textvariable=self.DetailedServiceType, )

        SrvcList.bind("<<ComboboxSelected>>", choosing)
        # choosing(self.ServiceType)
        combo.pack(padx=5, pady=5)

        RefNoLbl = Label(Manage_Frame, text='ادخل رقم المعاملة ان وجد'
                                            ' \n:مثال '
                                            '\nqut-000135'
                                            '\nPO-000135', bg='white')
        RefNoLbl.pack(padx=5, pady=5)
        RefNo = Entry(Manage_Frame, textvariable=self.ReferenceNumber, bd='2', justify='center')
        RefNo.pack(padx=5, pady=5)
        DescriptionLbl = Label(Manage_Frame, text='ادخل وصف المشكلة', bg='white')
        DescriptionLbl.pack(padx=5, pady=5)
        Description = Entry(Manage_Frame, textvariable=self.DescriptionInfo, bd='2', width=60, justify=RIGHT)
        Description.place(height=90, y=350, x=40)
        # Description.pack(padx=10, pady=10)
        # Description.place(x=49, y=200)
        # =================================== ( buttons ) الازرار ================================= #
        b1 = Button(Manage_Frame, text="ارفع التذكرة", bd='3', command=self.add_request)
        b1.place(x=5, y=465)
        DateLbl = Label(Manage_Frame, text=str(date.today()) + " : التاريخ", bg='white')
        # "مرسل التذكرة:  \t"+ os.getenv("USERNAME")+"\n"+"التاريخ:  \t"+ str(date.today())
        DateLbl.place(x=145, y=470)

    # ======================== (conneted to server data base) اتصال مع سيرفر قاعدة البيانات ======================== #

    def add_request(self):
        con = pymysql.connect(host='192.168.1.84', user='nat', password='', database='ticketsys')
        cur = con.cursor()
        cur.execute("insert into ticket_info values(%s,%s,%s,%s,%s,%s,Default,null)", (
            os.getenv("USERNAME"),
            date.today(),
            self.CompanyName.get(),
            self.ServiceType.get(),
            self.DescriptionInfo.get(),
            self.ReferenceNumber.get(),
        ))
        con.commit()
        con.close()

    # ======================== (conneted to server data base) اخذ البيانات من قاعدة البيانات ======================== #


root = Tk()
ob = service_request1(root)
root.mainloop()
