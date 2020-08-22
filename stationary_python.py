from tkinter import *
##class for heading
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Customer Bill")
        blue_colr="#595959"
        red_colr="#FF0000"
        title=Label(self.root,text="Customer Bill",bd=12,relief=RIDGE,
            bg=blue_colr,fg="white",font=("calibary",25,"bold")).pack(fill=X)


        #.....variable declaration........#
        # .............products var declration........#
        self.notebook=IntVar() # notebook is a variable name for integer input in box
        self.pen = IntVar()
        self.pencil = IntVar()
        self.dbook = IntVar()
        self.colors = IntVar()
        self.gum = IntVar()
        #............total...per...product....

        self.t1 = IntVar()
        self.t2 = IntVar()
        self.t3 = IntVar()
        self.t4 = IntVar()
        self.t5 = IntVar()
        self.t6 = IntVar()


        #.............customer data var........#        s
        self.cname = StringVar()
        self.cmob = StringVar()
        self.cmail = StringVar()

        #......gst and discount......#
        self.gst= StringVar()

        self.disc = StringVar()
        self.total = StringVar()

        self.grosstotal = StringVar()

        #........buttons...
        self.search = StringVar()
        self.generatebill = StringVar()

        #.......customer data..........#

        frame_1=LabelFrame(self.root,text="CUSTOMER DATA",relief=RIDGE,bd=10,font=("bookman",10,"bold"),fg="white",bg=blue_colr)
        frame_1.place(x=0,y=75,relwidth=1)

        #........cust name and entry of name....#

        cust_name=Label(frame_1,text="CUSTOMER NAME :",font=("bookman",15,"bold"),fg="white",bg=blue_colr).grid(row=0,column=1,padx=2, pady=5)
        cust_txt=Entry(frame_1,width=20,textvariable=self.cname,font="roboto 16").grid(row=0,column=2,pady=5)

        # ........cust mobile no and entry of number....#

        cust_mob = Label(frame_1, text="MOBILE NO :", font=("bookman", 15, "bold"), fg="white", bg=blue_colr).grid(row=0,column=3, padx=2, pady=5)
        cust_mob_no = Entry(frame_1, width=15,textvariable=self.cmob, font="roboto 16").grid(row=0, column=4,pady=5,padx=2)

        # ........cust email and entry of email....#

        cust_mail = Label(frame_1, text="EMAIL ID :", font=("bookman", 15, "bold"), fg="white", bg=blue_colr).grid(row=0, column=5, padx=2, pady=5)

        cust_mail_id = Entry(frame_1, width=25, textvariable=self.cmail,font="roboto 16").grid(row=0, column=6,pady=5)

        prpjectdevname=Label(frame_1,text="project by:Aniket Rajgure",width=18,bd=7,fg="white",bg=blue_colr,font="roboto 10 bold").grid(row=0,column=7,padx=5, pady=5)

         #............stationary type.............#

        frame_2 = LabelFrame(self.root, text="STATIONARY TYPE", relief=RIDGE, bd=10, font=("bookman", 15, "bold"), fg="white", bg=blue_colr)
        frame_2.place(x=9, y=170, width=500,height=380)

        #product names#
        ITEM1=Label(frame_2,text="PRODUCT NAME ",font=("bookman",15,"bold"),fg="white",width=25,bg=red_colr,relief=RIDGE, bd=6).grid(row=0,column=1,padx=5,pady=5)
        ITEM2=Label(frame_2,text="Notebook ",font=("bookman",15,"bold"),fg="BLACK",width=25,bg="YELLOW",relief=RIDGE, bd=6).grid(row=1,column=1, padx=5,pady=5)
        ITEM3=Label(frame_2,text="Pen ",font=("bookman",15,"bold"),fg="BLACK",width=25,bg="YELLOW",relief=RIDGE, bd=6).grid(row=2,column=1, padx=5,pady=5)
        ITEM4=Label(frame_2,text="Pencil ",font=("bookman",15,"bold"),fg="BLACK",width=25,bg="YELLOW",relief=RIDGE, bd=6).grid(row=3,column=1, padx=5,pady=5)
        ITEM5=Label(frame_2,text="Drawing book ",font=("bookman",15,"bold"),fg="BLACK",width=25,bg="YELLOW",relief=RIDGE, bd=6).grid(row=4,column=1, padx=5,pady=5)
        ITEM6=Label(frame_2,text="Colors ",font=("bookman",15,"bold"),fg="BLACK",width=25,bg="YELLOW",relief=RIDGE, bd=6).grid(row=5,column=1, padx=5,pady=5)
        ITEM7=Label(frame_2,text="Gum ",font=("bookman",15,"bold"),fg="BLACK",width=25,bg="YELLOW",relief=RIDGE, bd=6).grid(row=6,column=1, padx=5,pady=5)

        ITEM7=Label(frame_2,text="Quantity",font=("bookman",15,"bold"),fg="white",width=10,bg=red_colr,relief=RIDGE, bd=6).grid(row=0,column=2, padx=5,pady=5)

        #...............quantity....#
        qty1= Entry(frame_2,font=("bookman",15,"bold"),textvariable=self.notebook,fg="BLACK",width=10,bg="white",relief=RIDGE, bd=4).grid(row=1,column=2, padx=5,pady=5)
        qty2= Entry(frame_2,font=("bookman",15,"bold"),textvariable=self.pen,fg="BLACK",width=10,bg="white",relief=RIDGE, bd=4).grid(row=2,column=2, padx=5,pady=5)
        qty3= Entry(frame_2,font=("bookman",15,"bold"),textvariable=self.pencil,fg="BLACK",width=10,bg="white",relief=RIDGE, bd=4).grid(row=3,column=2, padx=5,pady=5)
        qty4= Entry(frame_2,font=("bookman",15,"bold"),textvariable=self.dbook,fg="BLACK",width=10,bg="white",relief=RIDGE, bd=4).grid(row=4,column=2, padx=5,pady=5)
        qty5= Entry(frame_2,font=("bookman",15,"bold"),textvariable=self.colors,fg="BLACK",width=10,bg="white",relief=RIDGE, bd=4).grid(row=5,column=2, padx=5,pady=5)
        qty6= Entry(frame_2,font=("bookman",15,"bold"),textvariable=self.gum,fg="BLACK",width=10,bg="white",relief=RIDGE, bd=4).grid(row=6,column=2, padx=5,pady=5)

        # ............stationary TOTAL.............#
        frame_3= LabelFrame(self.root, text="TOTAL", relief=RIDGE, bd=10, font=("bookman", 15, "bold"), fg="white", bg=blue_colr)
        frame_3.place(x=520, y=170, width=300, height=380)

        totc1=Label(frame_3,text="Total",font=("bookman",15,"bold"),fg="white",width=15,bg=red_colr,relief=RIDGE, bd=6).grid(row=0,column=0, padx=50,pady=5)
        totc2=Entry(frame_3,font=("bookman",15,"bold"),textvariable=self.t1,fg="BLACK",width=15,bg="white",relief=RIDGE, bd=6).grid(row=1,column=0, padx=50,pady=5)
        totc3=Entry(frame_3,font=("bookman",15,"bold"),textvariable=self.t2,fg="BLACK",width=15,bg="white",relief=RIDGE, bd=6).grid(row=2,column=0, padx=50,pady=5)
        totc4=Entry(frame_3,font=("bookman",15,"bold"),textvariable=self.t3,fg="BLACK",width=15,bg="white",relief=RIDGE, bd=6).grid(row=3,column=0, padx=50,pady=5)
        totc5=Entry(frame_3,font=("bookman",15,"bold"),textvariable=self.t4,fg="BLACK",width=15,bg="white",relief=RIDGE, bd=6).grid(row=4,column=0, padx=50,pady=5)
        totc6=Entry(frame_3,font=("bookman",15,"bold"),textvariable=self.t5,fg="BLACK",width=15,bg="white",relief=RIDGE, bd=6).grid(row=5,column=0, padx=50,pady=5)
        totc7=Entry(frame_3,font=("bookman",15,"bold"),textvariable=self.t6,fg="BLACK",width=15,bg="white",relief=RIDGE, bd=6).grid(row=6,column=0, padx=50,pady=5)



        # ............billing generation frame.............#



        frame_4= Frame(self.root, relief=RIDGE,bd=10, bg="white")
        frame_4.place(x=833, y=170, width=515, height=380)
        #shop_name=Label(frame_4,text="my stationary shop",font="arial,15,bold",bd=7,relief=RIDGE).pack(fill=X)
        scroll=Scrollbar(frame_4,orient=VERTICAL)
        self.txtarea=Text(frame_4,font="verdana 9  ",yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        self.bill_cdata()





        #..........gst...tax.........#

        frame_bottom = LabelFrame(self.root, text="Taxes", relief=RIDGE, bd=10, font=("bookman", 15, "bold"), fg="white", bg=blue_colr)
        frame_bottom.place(x=9, y=560, width=500, height=120)
        gst = Label(frame_bottom,text="GST :",font=("bookman", 15, "bold"), fg="white", width=5, bg=blue_colr,  bd=6).grid(row=0, column=0, padx=30, pady=0)
        gstshow = Entry(frame_bottom,font=("bookman", 12, "bold"), textvariable=self.gst,fg="black", width=20, bg="white", relief=RIDGE, bd=6).grid(row=0, column=1, padx=70, pady=2)
        discount=Label(frame_bottom,text="Discount",font=("bookman",15,"bold"),fg="white",width=10,bg=blue_colr,bd=6).grid(row=1, column=0, padx=30, pady=0)
        discounttshow = Entry(frame_bottom,font=("bookman", 12, "bold"),textvariable=self.disc, fg="black", width=20, bg="white", relief=RIDGE, bd=6).grid(row=1, column=1, padx=70, pady=2)

        #........total........#
        frame_tot = LabelFrame(self.root, text="TOTAL", relief=RIDGE, bd=10, font=("bookman", 15, "bold"), fg="white", bg=blue_colr)
        frame_tot.place(x=520, y=560, width=300, height=120)
        #total_lable.........#

        total = Label(frame_tot,text="Total (Rs.)",font=("bookman", 12, "bold"), fg="BLACK", width=10, bg="white", relief=RIDGE, bd=6).grid(row=0, column=0, padx=5, pady=5)
        totalwdisc = Label(frame_tot,text="Gross Total (Rs.)",font=("bookman", 9, "bold"), fg="BLACK", width=14, bg="white", relief=RIDGE, bd=6).grid(row=1, column=0, padx=5, pady=5)
         #.......output values....#

        totalop=Entry(frame_tot,font=("bookman",12,"bold"),textvariable=self.total,fg="BLACK",width=14,bg="white",relief=RIDGE, bd=6).grid(row=0,column=1, padx=8,pady=5)
        gross_totalop=Entry(frame_tot,font=("bookman",12,"bold"),textvariable=self.grosstotal,fg="BLACK",width=14,bg="white",relief=RIDGE, bd=6).grid(row=1,column=1, padx=8,pady=5)


        #........empty frame.......#
        eframe= LabelFrame(self.root, text="Total ", relief=RIDGE, bd=10, font=("bookman", 15, "bold"), fg="white", bg=blue_colr)
        eframe.place(x=833, y=560, width=515, height=120)
        # ......generatebutton.........
        totalbutton = Button(eframe,command=self.totalf,text="Total", width=12, bd=7, font="roboto 15 bold").grid(row=0, column=0, padx=10,pady=10)
        billgenbutton= Button(eframe,command=self.bill_section,text="GENERATE BILL", width=15, bd=7, font="roboto 15 bold").grid(row=0, column=1, padx=10,pady=10)

        #devdata = Label(eframe, text="Name:Aniet Rajgure Mail ID:aniketrajgure1998@gmail.com", fg="white", bg=blue_colr, font="roboto 7 bold").grid(row=0, column=1, padx=10,pady=10)
        #totalbill1 = Button(eframe,command=self.gstshow,text="Total", width=12, bd=7, font="roboto 15 bold").grid(row=0, column=0, padx=10,pady=10)


    def totalf(self):  #........functionn for addition
        self.tot_st_prc=float(
            (self.notebook.get()*50)+
            (self.pen.get() * 10) +
            (self.pencil.get() * 5) +
            (self.dbook.get() * 100) +
            (self.colors.get() * 200) +
            (self.gum.get() * 15) )

        self.total.set(float(self.tot_st_prc))

        # .........gst.....calculation
        self.gstcal=int(
                         (self.tot_st_prc)/100*18
                         )

        self.gst.set((self.gstcal))

        #.....total without....disc..#
        self.add=float(
                      (self.gstcal)+(self.tot_st_prc)
                      )
        self.grosstotal.set(float(self.add))

        #total price with discount..........
        self.discount=float(
                            (self.add)/100*4
                           )
        self.disc.set(float(self.discount))
        #..................final total
        self.totwithdisc=float(
                              (self.add)-(self.discount)
                              )
        self.grosstotal.set(float(self.totwithdisc))


        #......total..of..per..product.....
        self.to1 = float(
                        (self.notebook.get() * 50)
                        )
        self.t1.set(float(self.to1))

        self.to2= float( (self.pen.get() * 10)

        )
        self.t2.set(float(self.to2))

        self.to3 = float( (self.pencil.get() * 5)

                         )
        self.t3.set(float(self.to3))

        self.to4 = float( (self.dbook.get() * 100)

                         )
        self.t4.set(float(self.to4))

        self.to5 = float((self.colors.get() * 200)

                         )
        self.t5.set(float(self.to5))


        self.to6= float(   (self.gum.get() * 15)

                         )
        self.t6.set(float(self.to6))

    def bill_cdata(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t      Your total bill")
        self.txtarea.insert(END,f"\n  Name : {self.cname.get()} ")
        self.txtarea.insert(END, f"\n  Mobile no : {self.cmob.get()} ")
        self.txtarea.insert(END, f"\n  Email ID :   {self.cmail.get()} ")
        self.txtarea.insert(END,f"\n\n \tProduct\t     price\t     Quantity\t       total")




#...........................use product this identation from margin....#


    def bill_section(self):
        self.bill_cdata()
        if self.notebook.get()!=0:

            self.txtarea.insert(END, f"\n\n   \tnotebook\t      50  \t       {self.notebook.get()}\t          {self.to1}")

        if self.pen.get() != 0:

            self.txtarea.insert(END, f"\n\n   \tpen\t      10  \t       {self.pen.get()}\t           {self.to2}")
        if self.pencil.get() != 0:

            self.txtarea.insert(END,  f"\n\n   \tpencil\t      5 \t     {self.pencil.get()}\t        {self.to3}")
        if self.dbook.get() != 0:

            self.txtarea.insert(END, f"\n\n\tDrawing book\t   100  \t    {self.dbook.get()}\t          {self.to4}")
        if self.colors.get() != 0:

            self.txtarea.insert(END,f"\n\n  \tcolors\t     150  \t       {self.colors.get()}\t          {self.to5}")
        if self.gum.get() != 0:

            self.txtarea.insert(END, f"\n\n   \tgum\t      10  \t       {self.gum.get()}\t          {self.to6}")



        self.txtarea.insert(END,f"\n     .................................................................................................................")

        self.txtarea.insert(END, f"\n   \tGst(18%) : \t{self.gst.get()} rs/-\tDiscount\t    {self.disc.get()}  ")
        self.txtarea.insert(END,f"\n     .................................................................................................................")

        self.txtarea.insert(END,f"\n   \tTOTAL\t                       {self.grosstotal.get()} /-")
        self.txtarea.insert(END,f"\n     .................................................................................................................")


root =Tk()
obj =Bill_App(root)
root.mainloop()









