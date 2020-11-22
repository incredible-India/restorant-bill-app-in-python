
"""Welcome to the restaurant offer...."""
"""This is created by Himanshu sharma"""
#make it cool
# start from here
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox as mes
from pygame import mixer
import random
from PIL import ImageTk,Image


import time

extra=[] #for food store

col=["#808000"
,"#00ffff"
,"#008040"
,"#400040"
,"#8000ff"
,"#006a9d"
,"#ff8000"]
col1=["#00ff80",
"#004080",
"#000055",
"#1f3f3f",
"#2f1717",
"#ca4200",
"#ff972f"]
chos=random.choice(col)
chos1=random.choice(col)
chos2=random.choice(col)
chos3=random.choice(col)
chos4=random.choice(col)

chos6=random.choice(col)



"""clases starts from here"""
def foodwork():
    vegi=["Paneer Butter Mashala  145\\plate","Sahi Paneer  145\\plate","Kaju Paneer  130\\plate","panner Tikka 120\\plate"
          ,"MIX VEG  90\\plate","Aallo Ghobhi  90\\Plate","Mashroom Kury  100\\plate","Parval With Saag  100\\plate","Rice and Beans  120\\plate",
          "Chana Mashala  80\\plate","Special Sahi thali  120\\plate","Simple Thali  80\\plate"]
    non_vegi=["Egg curry  80\\plate","Amritsari Chicken Mashala  100\\plate","Teekha Murg  100\\plate","Kerala Chiken Roast  100\\plate",
              "Chicken Chettinad  120\\plate","Chicken lollypop   100\\plate","Mutton Butter Mashala  200\\plate"
        ,"Special Sahi thali  220\\plate","Simple Thali  180\\plate"]
    mix=["Egg curry  80\\plate","Amritsari Chicken Mashala  100\\plate","Teekha Murg  100\\plate","Kerala Chiken Roast  100\\plate",
              "Chicken Chettinad  120\\plate","Chicken lollypop   100\\plate","Mutton Butter Mashala  200\\plate"
        ,"Special Sahi thali  220\\plate","Simple Thali  180\\plate","Paneer Butter Mashala  145\\plate","Sahi Paneer  145\\plate","Kaju Paneer  130\\plate","panner Tikka 120\\plate"
          ,"MIX VEG  90\\plate","Aallo Ghobhi  90\\Plate","Mashroom Kury  100\\plate","Parval With Saag  100\\plate","Rice and Beans  120\\plate",
          "Chana Mashala  80\\plate","Special Sahi thali  120\\plate","Simple Thali  80\\plate"]
    bread=["non roti  6\\piece","paratha  4\\piece","roti  3\\piece","Aaloo Pharatha  10\\piece ","Butter non-roti  8\\piece","butter roti 5\\piece",
            "Khowa pharatha  15\\piece"]
    rice=["Steam Rice  15\\plate","Poolaw 20\\plate","fried rice  25\\plate","Ghee Rice  20\\plate","Butter Rice "]

    desert_snakes=["Chips  10\\packet","Rasgulla  8\\peice","kala jamoon  10\\piece","Kurkure  5\\packet","kaju katli  12\\piece",
                   "chhena  18\\piece"]


    class options:
        global extra
        def __init__(self,value):
            self.value=value
        def combo(self):
            """make an special frame for here"""

            print(self.value)
            cpylist=[]
            if self.value==1:
                cpylist=vegi

            elif self.value==2:
                cpylist=non_vegi
            else:
                cpylist=mix

            food1=StringVar()

            food3=StringVar()
            food4=StringVar()
            food5=StringVar()
            food1.set("Select the Meals")

            food3.set("Select the Breads")
            food4.set("Select the Rice")
            food5.set("Select the Desert")

            f80 = Frame(root, width=200, bg="#ffff87", bd="3", relief=SUNKEN)
            f80.pack(fill=X, side=LEFT, anchor=NW)
            opt1=OptionMenu(f80,food1,*cpylist,command=self.getfood)
            opt1.pack(side=LEFT)


            opti2=OptionMenu(f80,food3,*bread,command=self.getfood)
            opti2.pack(side=LEFT)

            opti3=OptionMenu(f80, food4, *rice,command=self.getfood)
            opti3.pack(side=LEFT)

            opti4=OptionMenu(f80, food5, *desert_snakes,command=self.getfood)
            opti4.pack(side=LEFT)




        def getfood(self,*args):
            l.insert(END,*args)

            extra.insert(1,*args)
    """frme for food option pass in class as frame"""




    if(food.get()==1):




        l.delete(0,END)
        l.insert(END,"Order Review")
        extra.insert(0,"VEG")

        vag=options(1)
        vag.combo()
    elif food.get()==2:


        l.delete(0, END)
        l.insert(END, "Order Review")
        extra.insert(0, "NON-VEG")
        non=options(2)
        non.combo()
    else:

        l.delete(0, END)
        l.insert(END, "Order Review")
        extra.insert(0, "BOTH")
        dono=options(3)
        dono.combo()

    l.insert(END,extra[0])

"""get the value of food here  form option menu"""



"""order function with file handling """




def take_order():
    global extra
    o=Tk()
    o.geometry("600x550")
    o.iconbitmap("io.ico")
    o.config(bg="teal")

    def orderd():
        o.destroy()
    def orderdi():
        with open("order.txt", "a") as D:
            D.write(f"----------------------------------------------------")
            D.write(f"\nOn {time.asctime(time.localtime(time.time()))}\n the order has been given\n ")
            for i in extra:
                D.write(f"\n{i}\n")
            D.write(f"-----------------------------------------------------")
        mes.showinfo(title="Order Summery",message="Your order has been accepted ,Hope you  enjoy")

        o.destroy()

    def htado():
        extra.remove(li.get(ACTIVE))
        li.delete(ANCHOR)



    Label(o,text="YOUR ORDER REVIEW",font="Jokerman 15 bold",fg="blue",padx=4).pack(pady=6)
    fram=Frame(o)
    fram.pack(side=BOTTOM)


    lib = Button(fram, text="Confirm", bg="green",fg="white", font="latin 15 bold",command=orderdi)
    lib.pack(side=LEFT,padx=2,anchor=NW)
    lib = Button(fram, text="Cancel", bg="red", font="latin 15 bold",command=orderd)
    lib.pack(side=LEFT,padx=2,anchor=NW)
    lib = Button(fram, text="Remove", bg="yellow",fg="red", font="latin 15 bold",command=htado)
    lib.pack(side=LEFT,padx=2,anchor=NW)
    li=Listbox(fram,width=80,height=75,font="times 15 bold",bg="pink")
    li.pack(pady=10)
    lfar = Label(fram, text="Capsicum Meals", font="chiller  20 bold", fg="red")
    lfar.pack(side=LEFT)
    for i in extra:
        li.insert(END,f"{i}")

    o.mainloop()













"""calculator function starts from here"""
def click(event):
    global entry

    text=event.widget.cget('text')
    if text=="=":
        if E2.get().isdigit():
            E2.update()
            val=E2.get()
            E2.update()
            entry.set(val)
        else:
            try:
                E2.update()
                val=eval(E2.get())
                E2.update()
                entry.set(val)
            except Exception as error:
                print(error)
                entry.set("Invalid data \U0001F923")


    elif text=="C":
        entry.set("")
        E2.update()
    else:
        entry.set(E2.get()+text)






def bhula():
    mixer.init()
    mixer.music.load("bhu (1).ogg")
    mixer.music.play()
def pirat():
    mixer.init()
    mixer.music.load("bhu (4).ogg")
    mixer.music.play()

def bulliya():
    mixer.init()
    mixer.music.load("bhu (3).ogg")
    mixer.music.play()

def other():
    mixer.init()
    mixer.music.load("bhu (2).ogg")
    mixer.music.play()

def stop():
    mixer.init()
    mixer.music.stop()

"""color change function"""
def colorchange():
    k=colorchooser.askcolor(title="Select the color for background")
    root.config(bg=k[1])
    l1.config(bg=k[1])
    f4.config(bg=k[1])


def change_color2():
    k=colorchooser.askcolor(title="Select the color for backgropund..")
    f1.config(bg=k[1])

def color_change3():
    k=colorchooser.askcolor(title="Color For buttons")
    b2.config(bg=k[1])
    b3.config(bg=k[1])
    b4.config(bg=k[1])
    b5.config(bg=k[1])
    b6.config(bg=k[1])
    b7.config(bg=k[1])
    b8.config(bg=k[1])
    b9.config(bg=k[1])
    b10.config(bg=k[1])
    b11.config(bg=k[1])
def color_change4():
    k=colorchooser.askcolor(title="Color For buttons")
    b2.config(fg=k[1])
    b3.config(fg=k[1])
    b4.config(fg=k[1])
    b5.config(fg=k[1])
    b6.config(fg=k[1])
    b7.config(fg=k[1])
    b8.config(fg=k[1])
    b9.config(fg=k[1])
    b10.config(fg=k[1])
    b11.config(fg=k[1])
def color_change5():
    k=colorchooser.askcolor(title="pick the color")
    f2.config(bg=k[1])
    f3.config(bg=k[1])
    f4.config(bg=k[1])
    f5.config(bg=k[1])
def colorchange10():
    k=colorchooser.askcolor(title="select the color for order review")
    can.config(bg=k[1])

"""feedback work done here """

def feedback():
    def lelo():


        with open("feedback.dat","a") as f:
            f.write(f"\n on {time.asctime(time.localtime(time.time()))} \n the ratting is \n"
                    f"{st.get()} Star \n and they write {t1.get(1.0,END)}")
        lab=Label(can,text="Thanx for giving Feedback",fg="green",font="times 15 italic")
        lab.pack(side=LEFT,padx=5)
        feed.destroy()


    feed=Tk()
    feed.geometry("400x400")
    feed.config(bg="cyan")

    feed.resizable(False,False)
    feddbk=IntVar()
    st=Scale(feed,from_=1,to=5,orient="horizontal",label="Give us star to slide"
             ,font="chiller 15 bold",activebackground="red",variable=feddbk,fg="red")
    st.pack(side=LEFT,pady=20,anchor=NW)
    Label(feed,text=" Want to Write Something",font="Latin 15 bold",fg="green"
          ,bd=3,relief=SUNKEN,bg="red").pack(pady=5)

    bb=Button(feed,bd=2,relief=SOLID,text="Done",bg="brown",font="latin 15",command=lelo)
    bb.pack(side=BOTTOM,anchor=NW,fill=X)

    sc = Scrollbar(feed)
    sc.pack(side=RIGHT, fill=Y)
    t1 = Text(feed, yscrollcommand=sc.set, wrap=WORD, selectbackground="red", font="latin 15 bold")
    t1.pack(fill=X)
    t1.insert(END,"Write Some thing here,,")
    sc.configure(command=t1.yview)




    feed.mainloop()
    """end of feedback work"""


"""cancel food here and reset the setting"""

def cancel_food():
    l.delete(0,END)
    l.insert(END,"Order Review")

    extra.clear()

    """payment work starts from here"""

def payment():
    k=mes.showerror("Unable to take E-money ","Sorry for Some Technical "
                                             "Issue we are not accepting online payment please got the counter and pay there..")

"""root wale listbox ka hatyega"""
def htade():
    extra.remove(l.get(ACTIVE))
    l.delete(ACTIVE)

def tearm():
    tr=Tk()
    tr.resizable(False,False)
    op=open("terms.txt")
    t=op.readlines()
    Label(tr,text=t,bg="green",fg="white").pack()
    op.close()


    tr.mainloop()
"""order history"""
def history():
    tri=Tk()
    # tri.resizable(False,False)
    op=open("order.txt")
    t=op.readlines()
    Label(tri,text="Order History",font="times 15 bold").pack(side=TOP)

    scbar=Scrollbar(tri)
    scbar.pack(side=RIGHT,fill=Y)
    tt=Text(tri,yscrollcommand=scbar.set,)
    tt.pack(expand=True,fill=BOTH)
    tt.insert(END,list(t))
    scbar.config(command=tt.yview)
    op.close()


    tri.mainloop()













if __name__ == '__main__':

    root=Tk()
    root.iconbitmap("D:\\icons\\Iconleak-Cerulean-Compass.ico")

    root.title("Himanshu Restaurants..")
    root.config(bg=chos)
    root.geometry("1500x700")


    """menu work from starts from here"""

    mainmenu=Menu(root)
    m1=Menu(mainmenu,tearoff=0)

    m5=Menu(m1,tearoff=0)
    m5.add_command(label="Background color", command=change_color2)
    m5.add_command(label="Buttons Colors", command=color_change3)
    m5.add_command(label="Buttons Text Colors", command=color_change4)
    m5.add_command(label="Buttons Background Color", command=color_change5)
    m5.add_separator()
    m5.add_command(label="Exit", activebackground="black", command=exit)

    m1.add_command(label="Background color" ,command=colorchange)
    m1.add_command(label="Order Review color" ,command=colorchange10)
    m1.add_cascade(label="Calculator Color", menu=m5)
    m1.add_separator()
    m1.add_command(label="Order History",command=history)
    m1.add_command(label="Terms and Conditions",command=tearm)
    m1.add_separator()

    m1.add_command(label="Exit", activebackground="black", command=exit)


    m2=Menu(mainmenu,tearoff=0)
    m3=Menu(mainmenu,tearoff=0)
    m3.add_command(label="Pirates of Caribbean",activebackground="green",command=pirat)
    m3.add_command(label="Bhula dunga(Dharshan raval)",activebackground="green",command=bhula)
    m3.add_command(label="Bullya",activebackground="green",command=bulliya)
    m3.add_command(label="others",activebackground="green",command=other)
    m5=Menu(m1,tearoff=0)





    m2.add_cascade(label="Play songs",menu=m3)



    mainmenu.add_cascade(label="File", menu=m1)
    mainmenu.add_cascade(label="Entertainment",menu=m2)
    mainmenu.add_cascade(label="Exit",command=quit)
    mainmenu.add_cascade(label="Stop Song",command=stop)
    """End the menu works"""
    # menu works ends here

    root.config(menu=mainmenu)

    """label bro"""
    l1=Label(text="Welcome To The Capsicum Meals\n MEALS ON WHEELS",font="chiller 29 bold",bg=chos,fg="red"
             ,pady=10)
    l1.pack(pady=10,anchor=CENTER)
    """side frame for calculator"""
    f1=Frame(root,width=200,bg=chos1,bd="3",relief=SUNKEN)
    f1.pack(fill=Y,side=LEFT,anchor=NW)

    """menu works starts in frame for calculator"""

    """task bar"""
    task = Frame(root, height=25 , bg="red", bd="1", relief=SOLID)
    task.pack(fill=X, side=BOTTOM, anchor=S)
    """task bar ends here"""

    l2=Label(task,text=f"Date : {time.asctime(time.localtime(time.time()))}",fg="black",bg="red")
    l2.pack(side=LEFT)
    l16=Label(task,text=f"    \t\t Order id :{random.randint(100,10000)}",fg="black",bg="red")
    l16.pack(side=LEFT)
    l17 = Label(task, text=f"Himanshu sharma..", fg="black", bg="red")
    l17.pack(side=RIGHT)

    """calculator works start from here.."""
    l5=Label(f1,text="Calculator",bg="#ffff80",font="chiller 15 bold ",)
    l5.pack(anchor=CENTER,pady=3)
    """Entry widget starts form here"""
    entry=StringVar()
    E2=Entry(f1,font="Times 20",bd=5,relief=GROOVE,textvariable=entry,)
    E2.pack(side=TOP,padx=10,pady=10)
    """button works starts from here"""
    f2=Frame(f1,bg="#ffff80")
    f2.pack()
    f3 = Frame(f1,bg="#ffff80")
    f3.pack()
    f4 = Frame(f1,bg="#ffff80")
    f4.pack()
    f5= Frame(f1,bg="#ffff80")
    f5.pack()
    for i in range(9,0,-1):
        if i>=7:
            b2=Button(f2,text=str(i),bd=6,relief=GROOVE,font="latin 16 ",padx=5,)
            b2.pack(side=LEFT,padx=8,pady=8)
            b2.bind("<Button-1>",click)
        elif i>=4:
            b3=Button(f3,text=str(i),bd=6,relief=GROOVE,font="latin 16 ",padx=5)
            b3.pack(side=LEFT,padx=8,pady=8)
            b3.bind("<Button-1>", click)
        else :
            b4=Button(f4,text=str(i),bd=6,relief=GROOVE,font="latin 16 ",padx=5)
            b4.pack(side=LEFT,padx=8,pady=8)
            b4.bind("<Button-1>", click)
    b5=Button(f2,text="+",bd=6,relief=GROOVE,font="latin 16 ",padx=5)
    b5.pack(side=LEFT,padx=8,pady=8)
    b5.bind("<Button-1>", click)
    b6=Button(f3,text="-",bd=6,relief=GROOVE,font="latin 16 ",padx=6)
    b6.pack(side=LEFT,padx=8,pady=8)
    b6.bind("<Button-1>", click)
    b7=Button(f4,text="*",bd=6,relief=GROOVE,font="latin 16 ",padx=5)
    b7.pack(side=LEFT,padx=8,pady=8)
    b7.bind("<Button-1>", click)
    """basic buttons"""
    b8=Button(f5,text="C",bg="red",bd=6,relief=GROOVE,font="latin 16 ",padx=5,activebackground="green")
    b8.pack(side=LEFT,padx=8,pady=8)
    b8.bind("<Button-1>", click)
    b9=Button(f5,text="0",bd=6,relief=GROOVE,font="latin 16 ",padx=5)
    b9.pack(side=LEFT,padx=8,pady=8)
    b9.bind("<Button-1>", click)
    b10=Button(f5,text="=",bg="green",bd=6,relief=GROOVE,font="latin 16 ",padx=5)
    b10.pack(side=LEFT,padx=8,pady=8)
    b10.bind("<Button-1>", click)
    b11=Button(f5,text="/",bd=6,relief=GROOVE,font="latin 16 ",padx=6,activebackground="yellow",)
    b11.pack(side=LEFT,padx=8,pady=8)
    b11.bind("<Button-1>", click)
    """button works end here"""


    """calculator works End here"""

    """restaurants works starts from here"""
    food=IntVar()
    f4=Frame(root,bg="#00ff80")
    f4.pack(side=LEFT,anchor=NW)
    r1=Radiobutton(root,text="VEG",bd=3,relief=SUNKEN,bg="green",value=1,variable=food,font="times 12 ",command=foodwork)
    r1.pack(side=LEFT,anchor=NW,padx=8)
    r1=Radiobutton(root,text="NON-VEG",bd=3,relief=SUNKEN,bg="RED",value=2,variable=food,font="times 12 ",command=foodwork)
    r1.pack(side=LEFT,anchor=NW,padx=8)
    r1=Radiobutton(root,text="BOTH",bd=3,relief=SUNKEN,bg="BLUE",value=3,variable=food,font="times 12 ",command=foodwork)
    r1.pack(side=LEFT,anchor=NW,padx=8)

    pic=Image.open("images.jpeg")
    pics=ImageTk.PhotoImage(pic)
    piclab=Label(f1,image=pics)
    piclab.pack(side=BOTTOM,anchor=SW,fill=Y)


    """order review"""
    can=Canvas(root,bg=chos2)
    can.pack(side=BOTTOM,fill=BOTH)
    l = Listbox(can, width=20, font="latin 20 bold",bg=chos3,fg="black")
    l.pack(padx=6, pady=5, side=LEFT, anchor=W)


    b20=Button(can,width=15,bg="green",text="Order",font="latin 20 bold",activebackground="yellow",command=take_order)
    b20.pack(padx=6,pady=5,side=TOP,anchor=W,fill=X)
    b20 = Button(can, width=15, bg="blue", text="FEEDBACK", font="latin 20 bold",activebackground="yellow",command= feedback)
    b20.pack(padx=6, pady=5, side=TOP, anchor=W,fill=X)
    b20 = Button(can,width=15, bg="teal", text="Payment", font="latin 20 bold",activebackground="yellow",command=payment)
    b20.pack(padx=6, pady=5, side=TOP, anchor=W,fill=X)
    b20 = Button(can, width=15, bg=chos6, text="Cancel", font="latin 20 bold",activebackground="yellow",command=cancel_food)
    b20.pack(padx=6, pady=5, side=TOP, anchor=W,fill=X)
    b20 = Button(can, width=15, bg="red",fg="white", text="Exit", font="latin 20 bold", activebackground="#ff8000",
                 command=exit)
    b20.pack(padx=6, pady=5, side=LEFT, anchor=E,)
    b21 = Button(can, width=15, bg=chos4, fg="white", text="Remove", font="latin 20 bold", activebackground="#ff8000",
                 command=htade)
    b21.pack(padx=6, pady=5, side=RIGHT, anchor=E, )

    l.insert(END, "Order Review")

root.mainloop()
"""End of this projet"""
"""Next of this projet piano"""
"""======================================================================================"""