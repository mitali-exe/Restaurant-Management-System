from tkinter import *
import mysql.connector
import random
import sys
from datetime import datetime
from tkinter import messagebox

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()


class LoginPage:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")

        def on_resize(event):
            self.win.update_idletasks()


        self.win.state('zoomed')  
        self.win.bind("<Configure>", on_resize)  


        self.title_label = Label(self.win,text="Restaurant Management System",font=("Arial",35,'bold'),bg="Lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        self.main_frame = Frame(self.win,bg="Lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=450)

        self.login_lbl = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="Lightgrey",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg='Lightgrey',font=('sans-serif',18))
        self.entry_frame.pack(fill=BOTH,expand=True)

        #==============================Variables================================

        username = StringVar()
        password = StringVar()

        #========================================================================


        #=============================Username==================================
        self.entus_lbl = Label(self.entry_frame,text="Enter Username: ",bg="Lightgrey",font=('sans-serif',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.entus_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)
        
        #=================================Password===========================
        self.entpass_lbl = Label(self.entry_frame,text="Enter Password: ",bg="Lightgrey",font=('sans-serif',15))
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.entpass_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=password,show="*")
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)



        #==========================Functions========================================

        def check_login():
            try:
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="restaurant"
                )
                mycursor = mydb.cursor()
                mycursor.execute('''SELECT * FROM admin WHERE username = %s AND password = %s''', (username.get(), password.get()))
                user = mycursor.fetchone()
                if user:
                    self.billing_btn.config(state="normal")
                else:
                    messagebox.showerror(title="Login Failed!", message="Invalid username or password")
            except Exception as e:
                messagebox.showerror("Error!","Error connecting to database")


        def reset():
            username.set("")
            password.set("")

        def billing():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)

        #======================================================================================


        #================================Buttons===============================================

        self.button_frame = LabelFrame(self.entry_frame,text="Options",font=('Arial',15),bg="Lightgrey",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=150,width=730,height=100)

        self.login_btn = Button(self.button_frame,text="Login",font=('Arial',15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn = Button(self.button_frame,text="Billing",font=('Arial',15),bd=5,width=15,command=billing)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = Button(self.button_frame,text="Reset",font=('Arial',15),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)

        #====================================================================================


class Window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1300x750+0+0")
        self.win.title("Restaurant Management System")

        self.title_label = Label(self.win,text="Restaurant Management System",font=("Arial",35,'bold'),bg="Lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        def on_resize(event):
            self.win.update_idletasks()


        self.win.state('zoomed')  
        self.win.bind("<Configure>", on_resize)

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="restaurant"
            )
        mycursor = mydb.cursor()

        #==============================Variables================================

        bill_no = random.randint(100,999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        Calc_var = StringVar()

        cust_nm = StringVar()
        cust_co = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty = StringVar()
        cost = StringVar()

        date_pr.set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        total_list = []
        self.grd_total = 0

        #===========================================================================

        #==============================Functions================================

        def default_bill():
            self.bill_txt.insert(END,"\t\t\tSwad Restaurant")
            self.bill_txt.insert(END,"\n\t\t123, Modi Compound Railway Road,Bharuch")
            self.bill_txt.insert(END,"\n\t\t\tContact - +917896541230")
            self.bill_txt.insert(END,"\n=======================================================================")
            self.bill_txt.insert(END,f"\nBill Number: {bill_no_tk.get()}")
        

        def gen_bill():
            if cust_nm.get == "" or cust_co.get() == "" or len(cust_co.get()) != 10:
                messagebox.showerror("Error!","Please enter all details correctly",parent=self.win)
            else:
                self.bill_txt.insert(END,f"\nCustomer Name: {cust_nm.get()}")
                self.bill_txt.insert(END,f"\nCustomer Contact: {cust_co.get()}")
                self.bill_txt.insert(END,f"\nDate: {date_pr.get()}")
                self.bill_txt.insert(END,"\n=======================================================================")
                self.bill_txt.insert(END,"\nProduct Name\t\t      Quantity\t\t       Cost\t\t        Total")
                self.bill_txt.insert(END,"\n=======================================================================")
                
                self.add_btn.config(state=NORMAL)
                self.total_btn.config(state=NORMAL)
                self.gen_bill_btn.config(state=DISABLED)

        def add_pur():
            if item_pur.get() == "" or item_qty.get() == "" or item_qty.get().isdigit() == 0:
                messagebox.showerror("Error!","Please enter all details correctly",parent=self.win)
            else:
                qty = int(item_qty.get())
                cone = int(cost.get())
                total = qty * cone
                total_list.append(total)
                self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t      {item_qty.get()}\t\t       {cost.get()}\t\t        ₹{total}")

        def clear():
            cust_nm.set("")
            cust_co.set("")
            item_pur.set("")
            item_qty.set("")
            cost.set("")

        def reset():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state=DISABLED)
            self.total_btn.config(state=DISABLED)
            self.save_bill_btn.config(state=DISABLED)
            self.gen_bill_btn.config(state=NORMAL)
            self.bill_txt.delete("1.0",END)
            default_bill()

        def total():
            for item in total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END,"\n=======================================================================")
            self.bill_txt.insert(END,f"\t\t\t\t\t\t\tGrand Total : ₹{self.grd_total}")
            self.bill_txt.insert(END,"\n=======================================================================")
            self.save_bill_btn.config(state=NORMAL)

        def logout():
            self.win.destroy()

        def save():
            user_choice = messagebox.askyesno("Confirm?",f"Do you want to save the bill {bill_no_tk.get()}",parent=self.win)
            if user_choice > 0:
                self.bill_content = self.bill_txt.get("1.0",END)
                try:
                    con = open(f"{sys.path[0]}/bills/"+ str(bill_no_tk.get()) + ".txt","w",encoding="utf-8")
                except Exception as e:
                    messagebox.showerror("Error!",f"Error: {e}")
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success",f"Bill {bill_no_tk.get()} has been saved",parent=self.win)
            else:
                return
            
        def text_change(event):
            item = item_pur.get()
            mycursor.execute("SELECT cost FROM menu WHERE item_name = %s", (item,))
            cone = mycursor.fetchone()
            if cone:
                cost.set(cone[0])
            else:
                cost.set("")

        def menu():
            pass


        def insert():
            new_window = Toplevel(self.win)
            new_window.geometry("400x300") 
            new_window.title("Insert New Item")

            # Labels and Entry Fields
            self.item_id_label = Label(new_window, text="Item ID:", font=("Arial", 15), anchor="w")
            self.item_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            self.item_id_entry = Entry(new_window, font=('Arial', 15))
            self.item_id_entry.grid(row=0, column=1, padx=10, pady=5)

            self.item_name_label = Label(new_window, text="Item Name:", font=("Arial", 15), anchor="w")
            self.item_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

            self.item_name_entry = Entry(new_window, font=('Arial', 15))
            self.item_name_entry.grid(row=1, column=1, padx=10, pady=5)

            self.insert_cost_label = Label(new_window, text="Cost:", font=("Arial", 15), anchor="w")
            self.insert_cost_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

            self.cost_entry = Entry(new_window, font=('Arial', 15))
            self.cost_entry.grid(row=2, column=1, padx=10, pady=5)

            def insert_item():
                if self.item_id_entry.get() == "" or self.item_name_entry.get() == "" or self.cost_entry.get() == "":
                    messagebox.showerror("Error!","Enter all details",parent=new_window)
                else:
                    try:
                        mycursor.execute('''INSERT INTO menu VALUES (%s, %s, %s)''', (self.item_id_entry.get(), self.item_name_entry.get(), self.cost_entry.get()))
                        mydb.commit()
            
                        messagebox.showinfo("Success", "Item inserted successfully",parent=new_window)
                        new_window.destroy() 

                    except mysql.connector.IntegrityError:
                        messagebox.showerror("Error", "ID already exists! Try a different one.",parent=new_window)
                    except Exception as e:
                        messagebox.showerror("Error", str(e),parent=new_window)

            # Insert Button
            self.insert_button = Button(new_window, text="Insert in Menu",font=('Arial',15),bd=5,width=12,height=1,command=insert_item)
            self.insert_button.grid(row=3, columnspan=2, pady=8)

        #======================================================================


        #=============================Entry====================================

        self.entry_frame = LabelFrame(self.win,text="Enter Details",background="Lightgrey",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=600,height=650)

        #Bill number
        self.bill_no_lbl = Label(self.entry_frame,text="Bill Number: ",font=("Arial",15),bg="Lightgrey", anchor="w")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2, sticky="w")

        self.bill_no_ent = Entry(self.entry_frame,bd=5,textvariable=bill_no_tk,font=('Arial',15))
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state=DISABLED)

        #Customer Number
        self.cust_nm_lbl = Label(self.entry_frame,text="Customer Name: ",font=("Arial",15),bg="Lightgrey", anchor="w")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2, sticky="w")

        self.cust_nm_ent = Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('Arial',15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)

        #Customer Contact
        self.cust_no_lbl = Label(self.entry_frame,text="Customer Number: ",font=("Arial",15),bg="Lightgrey", anchor="w")
        self.cust_no_lbl.grid(row=2,column=0,padx=2,pady=2, sticky="w")

        self.cust_no_ent = Entry(self.entry_frame,bd=5,textvariable=cust_co,font=('Arial',15))
        self.cust_no_ent.grid(row=2,column=1,padx=2,pady=2)

        #Date
        self.date_lbl = Label(self.entry_frame,text="Date: ",font=("Arial",15),bg="Lightgrey", anchor="w")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2, sticky="w")

        self.date_ent = Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Arial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)
        self.date_ent.config(state=DISABLED)

        #Item Purchased
        self.item_pur_lbl = Label(self.entry_frame,text="Item Purchased: ",font=("Arial",15),bg="Lightgrey", anchor="w")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2, sticky="w")

        self.item_pur_ent = Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('Arial',15))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)
        self.item_pur_ent.bind("<KeyRelease>", text_change)

        #Quantity
        self.qty_lbl = Label(self.entry_frame,text="Quantity: ",font=("Arial",15),bg="Lightgrey", anchor="w")
        self.qty_lbl.grid(row=5,column=0,padx=2,pady=2, sticky="w")

        self.qty_ent = Entry(self.entry_frame,bd=5,textvariable=item_qty,font=('Arial',15))
        self.qty_ent.grid(row=5,column=1,padx=2,pady=2)


        #Cost
        self.cost_lbl = Label(self.entry_frame,text="Cost of One: ",font=("Arial",15),bg="Lightgrey", anchor="w")
        self.cost_lbl.grid(row=6,column=0,padx=2,pady=2, sticky="w")

        self.cost_ent = Entry(self.entry_frame,bd=5,textvariable=cost,font=('Arial',15))
        self.cost_ent.grid(row=6,column=1,padx=2,pady=2)
        self.cost_ent.config(state=DISABLED)


        #Menu
        self.menu_btn = Button(self.entry_frame,text="Menu",font=('Arial',15),bd=5,width=18,height=2,justify=CENTER,command=menu)
        self.menu_btn.place(x=25,y=300)

        self.insert_btn = Button(self.entry_frame,text="Insert new item",font=('Arial',15),bd=5,width=18,height=2,justify=CENTER,command=insert)
        self.insert_btn.place(x=238,y=300)

        #Buttons
        self.button_frame = LabelFrame(self.entry_frame,font=('Arial',15),bg="Lightgrey",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=375,width=435,height=230)

        self.add_btn = Button(self.button_frame,text="Add",font=('Arial',15),bd=5,width=11,height=2,command=add_pur)
        self.add_btn.grid(row=1,column=0,padx=2,pady=2)

        self.clear_btn = Button(self.button_frame,text="Clear",font=('Arial',15),bd=5,width=11,height=2,command=clear)
        self.clear_btn.grid(row=0,column=1,padx=2,pady=2)

        self.reset_btn = Button(self.button_frame,text="Reset",font=('Arial',15),bd=5,width=11,height=2,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=2,pady=2)

        self.gen_bill_btn = Button(self.button_frame,text="Generate Bill",font=('Arial',15),bd=5,width=11,height=2,command=gen_bill)
        self.gen_bill_btn.grid(row=0,column=0,padx=2,pady=2)

        self.total_btn = Button(self.button_frame,text="Total",font=('Arial',15),bd=5,width=11,height=2,command=total)
        self.total_btn.grid(row=1,column=1,padx=2,pady=2)

        self.save_bill_btn = Button(self.button_frame,text="Save Bill",font=('Arial',15),bd=5,width=11,height=2,command=save)
        self.save_bill_btn.grid(row=1,column=2,padx=2,pady=2)

        self.logout = Button(self.button_frame,text="Logout",font=('Arial',15),bd=5,width=37,height=2,justify=CENTER,command=logout)
        self.logout.grid(row=2,columnspan=3)


        self.add_btn.config(state=DISABLED)
        self.total_btn.config(state=DISABLED)
        self.save_bill_btn.config(state=DISABLED)

        #==============================Calculator================================================================
        
        self.calc_frame = Frame(self.win,bd=8,background="lightgrey",relief=GROOVE)
        self.calc_frame.place(x=750,y=110,width=605,height=295)

        self.num_ent = Entry(self.calc_frame,bd=15,background="lightgrey",textvariable=Calc_var,font=('Arial',15),width=50,justify="right")
        self.num_ent.grid(row=0,column=0,columnspan=11)

        def press_btn(event):
            text=event.widget.cget("text")
            if text == "=":
                if Calc_var.get().isdigit():
                    value = int(Calc_var.get())
                else:
                    value = eval(self.num_ent.get())
            
                Calc_var.set(value)
                self.num_ent.update()

            elif text == "C":
                Calc_var.set("")
                self.num_ent.update()
            else:
                Calc_var.set(Calc_var.get() + text)
                self.num_ent.update()


        self.btn7 = Button(self.calc_frame,bg="lightgrey",text="7",bd=6,width=11,height=1,font=('Arial',15))
        self.btn7.grid(row=1,column=0,padx=4,pady=2)
        self.btn7.bind("<Button-1>", press_btn)

        self.btn8 = Button(self.calc_frame,bg="lightgrey",text="8",bd=6,width=11,height=1,font=('Arial',15))
        self.btn8.grid(row=1,column=1,padx=2,pady=2)
        self.btn8.bind("<Button-1>", press_btn)

        self.btn9 = Button(self.calc_frame,bg="lightgrey",text="9",bd=6,width=11,height=1,font=('Arial',15))
        self.btn9.grid(row=1,column=2,padx=2,pady=2)
        self.btn9.bind("<Button-1>", press_btn)

        self.btnadd = Button(self.calc_frame,bg="lightgrey",text="+",bd=6,width=11,height=1,font=('Arial',15))
        self.btnadd.grid(row=1,column=3,padx=2,pady=2)
        self.btnadd.bind("<Button-1>", press_btn)

        self.btn4 = Button(self.calc_frame,bg="lightgrey",text="4",bd=6,width=11,height=1,font=('Arial',15))
        self.btn4.grid(row=2,column=0,padx=4,pady=2)
        self.btn4.bind("<Button-1>", press_btn)

        self.btn5 = Button(self.calc_frame,bg="lightgrey",text="5",bd=6,width=11,height=1,font=('Arial',15))
        self.btn5.grid(row=2,column=1,padx=2,pady=2)
        self.btn5.bind("<Button-1>", press_btn)

        self.btn6 = Button(self.calc_frame,bg="lightgrey",text="6",bd=6,width=11,height=1,font=('Arial',15))
        self.btn6.grid(row=2,column=2,padx=2,pady=2)
        self.btn6.bind("<Button-1>", press_btn)

        self.btnsub = Button(self.calc_frame,bg="lightgrey",text="-",bd=6,width=11,height=1,font=('Arial',15))
        self.btnsub.grid(row=2,column=3,padx=2,pady=2)
        self.btnsub.bind("<Button-1>", press_btn)

        self.btn1 = Button(self.calc_frame,bg="lightgrey",text="1",bd=6,width=11,height=1,font=('Arial',15))
        self.btn1.grid(row=3,column=0,padx=4,pady=2)
        self.btn1.bind("<Button-1>", press_btn)

        self.btn2 = Button(self.calc_frame,bg="lightgrey",text="2",bd=6,width=11,height=1,font=('Arial',15))
        self.btn2.grid(row=3,column=1,padx=2,pady=2)
        self.btn2.bind("<Button-1>", press_btn)

        self.btn3 = Button(self.calc_frame,bg="lightgrey",text="3",bd=6,width=11,height=1,font=('Arial',15))
        self.btn3.grid(row=3,column=2,padx=2,pady=2)
        self.btn3.bind("<Button-1>", press_btn)

        self.btnmul = Button(self.calc_frame,bg="lightgrey",text="*",bd=6,width=11,height=1,font=('Arial',15))
        self.btnmul.grid(row=3,column=3,padx=2,pady=2)
        self.btnmul.bind("<Button-1>", press_btn)

        self.btnC = Button(self.calc_frame,bg="lightgrey",text="C",bd=6,width=11,height=1,font=('Arial',15))
        self.btnC.grid(row=4,column=0,padx=4,pady=2)
        self.btnC.bind("<Button-1>", press_btn)

        self.btn0 = Button(self.calc_frame,bg="lightgrey",text="0",bd=6,width=11,height=1,font=('Arial',15))
        self.btn0.grid(row=4,column=1,padx=2,pady=2)
        self.btn0.bind("<Button-1>", press_btn)

        self.btneq = Button(self.calc_frame,bg="lightgrey",text="=",bd=6,width=11,height=1,font=('Arial',15))
        self.btneq.grid(row=4,column=2,padx=2,pady=2)
        self.btneq.bind("<Button-1>", press_btn)

        self.btndiv = Button(self.calc_frame,bg="lightgrey",text="/",bd=6,width=11,height=1,font=('Arial',15))
        self.btndiv.grid(row=4,column=3,padx=2,pady=2)
        self.btndiv.bind("<Button-1>", press_btn)

        #========================================================================================================

        #==============================================Bill Frame================================================

        self.bill_frame = LabelFrame(self.win,text="Bill Area",font=('Arial',18),bg="lightgrey",bd=8,relief=GROOVE)
        self.bill_frame.place(x=750,y=420,width=605,height=320)

        self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt = Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)

        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=True)

        default_bill()


        #==========================================================================================================


if __name__ == "__main__":
    main()