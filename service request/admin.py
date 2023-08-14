from tkinter import *
from tkinter import ttk
import pymysql
import os
from datetime import date


admin = Tk()
admin.geometry('1000x700+1+1')
admin.title('Admin Panel')
admin.configure(background="silver")
admin.resizable(True, True)
title = Label(admin,
                text='[Admin Panel]',
                bg='#FFFFFF',
                font=('Arial Rounded MT', 14),
                fg="black"
                )
title.pack(fill=X)


#menu = Menu(admin)
#admin.config(menu=menu)
#filemenu = Menu(menu)
#menu.add_cascade(label='File', menu=filemenu)
#filemenu.add_command(label='Client', )
#filemenu.add_separator()
#filemenu.add_command(label='Exit', command=admin.quit)
#helpmenu = Menu(menu)
#menu.add_cascade(label='Help', menu=helpmenu)
#helpmenu.add_command(label='About')


    # =========================== (details) عرض النتائج والبيانات ============================ #
details_Frame2 = Frame(admin, bg='#ADADAD')
details_Frame2.place(x=0, y=60, width=1000, height=700)
        # --- scroll --- #
scroll_x = Scrollbar(details_Frame2, orient=HORIZONTAL)
scroll_y = Scrollbar(details_Frame2, orient=VERTICAL)
        # --- treeview ---#
admintree1 = ttk.Treeview(details_Frame2,
                            columns=('8', '7', '6', '5', '4', '3', '2', '1'),
                            xscrollcommand=scroll_x.set,
                            yscrollcommand=scroll_y.set)
admintree1.place(x=17, y=0, width=985, height=700)
admintree1.column('1', anchor=CENTER, stretch=NO, width=125)
admintree1.column('2', anchor=CENTER, stretch=NO, width=125)
admintree1.column('3', anchor=CENTER, stretch=NO, width=125)
admintree1.column('4', anchor=CENTER, stretch=NO, width=125)
admintree1.column('5', anchor=CENTER, stretch=NO, width=125)
admintree1.column('6', anchor=CENTER, stretch=NO, width=125)
admintree1.column('7', anchor=CENTER, stretch=NO, width=125)
admintree1.column('8', anchor=CENTER, stretch=NO, width=125)


scroll_y.pack(side=LEFT, fill=Y)
scroll_x.config(command=admintree1.xview)
scroll_y.config(command=admintree1.yview)
admintree1['show'] = 'headings'
admintree1.heading('8', text='الاسم')
admintree1.heading('7', text='التاريخ')
admintree1.heading('6', text='الشركة')
admintree1.heading('5', text='نوع الطلب')
admintree1.heading('4', text='الوصف')
admintree1.heading('3', text='رقم المعاملة')
admintree1.heading('2', text='الحالة')
admintree1.heading('1', text='رقم التذكرة')


    # =================================== ( search and buttom ) البحث و الازرار ================================= #
sb_Frame1 = Frame(admin, bg='#876159')
sb_Frame1.place(x=0, y=28, width=1000, height=32)
        # --- Lable ---#
Label1 = Label(sb_Frame1, text=': البحث عن معاملة جديدة', bd='1', bg='#876159', font=('Arial Rounded MT', 12),
                       fg="black")
Label1.place(x=170, y=4)
        # --- Entry ---#
search_Entry1 = Entry(sb_Frame1, bd='2')
search_Entry1.place(x=40, y=4)
        # --- Buttom ---#
b2 = Button(sb_Frame1, text="بحث", bd='2', bg='#A4A2A2')
b2.place(x=0, y=3)

Label1 = Label(sb_Frame1, text=': تغيير حالة الطلب ', bd='1', bg='#876159', font=('Arial Rounded MT', 12),
                fg="black")
Label1.place(x=890, y=4)
b3 = Button(sb_Frame1, text="تحت الإجراء", bd='2', bg='#A4A2A2',width=10)
b3.place(x=800, y=3)
b4 = Button(sb_Frame1, text="تمت  المعالجة", bd='2', bg='#A4A2A2',width=10)
b4.place(x=700, y=3)


admintree1.focus_get()
con = pymysql.connect(host='192.168.1.84', user='nat', password='', database='ticketsys')
cur = con.cursor()
cur.execute("select * from ticket_info")
rows = cur.fetchall()

count = 0
for record in rows:
    admintree1.insert("", "end", text='', values=(record[0], record[1], record[2], record[3], record[4],record[5],record[6],record[7]))
count += 1
con.commit()
con.close()


admin.mainloop()