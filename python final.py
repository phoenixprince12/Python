# -*- coding: cp1252 -*-
import sqlite3
from tkMessageBox import *
con=sqlite3.Connection('mydb')
cur=con.cursor()
cur.execute("create table if not exists userid(username varchar(20) primary key,fname varchar(40),lname varchar(40),password varchar(40))")

from Tkinter import*
root=Tk()
root.title("Mining Department Dtabase")
a=PhotoImage(file="nm.gif")
Label(root,image=a).grid(row=0, column=0 ,rowspan=100, columnspan=100)
Label(root, text="WELCOME", font=("times", 50), fg="white", bg="Khaki2", width=28).grid(row=0, column=0)
Label(root, text="Presented By: Prajwal Singh", font=("times", 15), fg="coral2", bg="cyan").grid(row=1, column=0)
Label(root, text="Enrollment No.: 161B144", font=("times", 15), fg="white", bg="orchid1").grid(row=2, column=0)
Label(root, text="Batch: B-5", font=("algerian", 15), fg
      ="white", bg="coral2").grid(row=3, column=0)
Label(root, text="Mobie No.: 9754312568", font=("times", 15), fg="white", bg="SteelBlue1").grid(row=4, column=0)
Label(root, text="Email: prajwal28091997@gmail.com", font=("times", 15), fg="white", bg="orchid1").grid(row=5, column=0)
Label(root, text="Guided by: Dr. Mahesh Kumar", font=("times", 15), fg="white", bg="orange red").grid(row=6, column=0)

def now():
    root.destroy()
    root1=Tk()
    root1.title("enter into mining databse")  

    def account():
        user=username.get()
        cur.execute("select username from userid where username=(?)",(user,))
        a=cur.fetchall()
        if a != []:
            showerror('Error',"Username Already Exists")
        else:
            l = (username.get(), fname.get(), lname.get(), password.get())
            cur.execute("insert into userid values(?,?,?,?)",l)
            showinfo('Congratulations !!',"You have been signed up.\nNow, you are ready to go")
            con.commit()
            username.delete(0,40)
            fname.delete(0,40)
            lname.delete(0,40)
            password.delete(0,40)
        
    def login():
        usr = user.get()
        paw = pas.get()
        cur.execute("select * from userid where username=(?) and password=(?)", (usr, paw,))
        a = cur.fetchall()
        if a==[]:
            showerror('Log In Failed', "Invalid Username or Password")
        else:
            root1.destroy()
            profile()
                

    
    Label(root1, text="Username: ", font=("Indigo", 15),fg=('purple')).grid(row=3, column=0)
    img = PhotoImage(file="ii.gif")
    Label(root1,image=img).grid(row=1,column=0, columnspan=4)
    user = Entry(width=30, font=("arial", 11), bg=('gold'))
    user.grid(row=3, column=1)
    Label(root1, text="Password: ", font=("Indigo", 15),fg=('purple')).grid(row=4, column=0)
    pas = Entry(width=30, font=("arial", 11), bg=('gold'))
    pas.grid(row=4, column=1)
    Button(root1, text="Log In", compound='center', font=("arial", 10), bg='blue', fg='white', width=10, command=lambda: login()).grid(row=5, columnspan=2)

    
    Label(root1, text="Username: ", font=("Indigo", 15),fg=('purple')).grid(row=3, column=2)
    username = Entry(root1, width=30, font=("arial", 11), bg=('gold') )
    username.grid(row=3, column=3)

    Label(root1, text="Firstname: ", font=("Indigo", 15),fg=('purple')).grid(row=4, column=2)
    fname = Entry(root1, width=30, font=("arial", 11), bg=('gold'))
    fname.grid(row=4, column=3)

    Label(root1, text="Lastname: ", font=("Indigo", 15),fg=('purple')).grid(row=5, column=2)
    lname = Entry(root1, width=30, font=("arial", 11), bg=('gold'))
    lname.grid(row=5, column=3)

    Label(root1, text="Password: ", font=("Indigo", 15),fg=('purple')).grid(row=6, column=2)
    password = Entry(root1, width=30, font=("arial", 11), bg=('gold'))
    password.grid(row=6, column=3)

    Button(root1, text="Sign Up", compound='center', font=("arial", 10), bg='red', fg='green', width=10, command=lambda: account()).grid(row=7, column=3, columnspan=2)
    root1.mainloop()

def profile():
    form=Tk()
    Label(form,text='Mining Department Records',font= "times 60 bold italic",bg='red').grid(row=0,column=0)
    Label(form,text='Coal Mining Extracttion methods',font= "times 40",bg='Blue').grid(row=1,column=0)
    v=IntVar()
    r=Radiobutton(form,text="Surface Mining",variable=v,value=1)
    r.grid(row=2,column=0)
    r1=Radiobutton(form,text="Strip Mining",variable=v,value=2)
    r1.grid(row=3,column=0)
    r2=Radiobutton(form,text="Contour Mining",variable=v,value=3) 
    r2.grid(row=4,column=0)
    r3=Radiobutton(form,text="Mountain Top Mining",variable=v,value=4)
    r3.grid(row=5,column=0)
    r4=Radiobutton(form,text="Underground Mining",variable=v,value=5)
    r4.grid(row=6,column=0)
    
    def fun():
        a=['Surface Mining']
        b=['Strip Mining']
        c=['Contour Mining']
        d=['Mountain Top Mining']
        e=['Underground Mining']
        if v.get()==1:
            
            showinfo('Surface Mining',"When coal seams are near the surface, it may be economical to extract the coal using open cut (also referred to as open cast, open pit, mountaintop removal or strip) mining methods. Open cast coal mining recovers a greater proportion of the coal deposit than underground methods, as more of the coal seams in the strata may be exploited. This equipment can include the following: Draglines which operate by removing the overburden, power shovels, large trucks in which transport overburden and coal, bucket wheel excavators, and conveyors. In this mining method, explosives are first used in order to break through the surface or overburden, of the mining area. The overburden is then removed by draglines or by shovel and truck. Once the coal seam is exposed, it is drilled, fractured and thoroughly mined in strips. The coal is then loaded onto large trucks or conveyors for transport to either the coal preparation plant or directly to where it will be used.")
        if v.get()==2:
            showinfo('Strip Mining',"Strip mining exposes coal by removing earth above each coal seam. This earth is referred to as overburden and is removed in long strips. The overburden from the first strip is deposited in an area outside the planned mining area and referred to as out-of-pit dumping. Overburden from subsequent strips are deposited in the void left from mining the coal and overburden from the previous strip. This is referred to as in-pit dumping.It is often necessary to fragment the overburden by use of explosives. This is accomplished by drilling holes into the overburden, filling the holes with explosives, and detonating the explosive. The overburden is then removed, using large earth-moving equipment, such as draglines, shovel and trucks, excavator and trucks, or bucket-wheels and conveyors. This overburden is put into the previously mined (and now empty) strip. When all the overburden is removed, the underlying coal seam will be exposed (a 'block' of coal). This block of coal may be drilled and blasted (if hard) or otherwise loaded onto trucks or conveyors for transport to the coal preparation (or wash) plant. Once this strip is empty of coal, the process is repeated with a new strip being created next to it. This method is most suitable for areas with flat terrain.")
        if v.get()==3:
            showinfo('Contour Mining',"The contour mining method consists of removing overburden from the seam in a pattern following the contours along a ridge or around the hillside. This method is most commonly used in areas with rolling to steep terrain. It was once common to deposit the spoil on the downslope side of the bench thus created, but this method of spoil disposal consumed much additional land and created severe landslide and erosion problems. To alleviate these problems, a variety of methods were devised to use freshly cut overburden to refill mined-out areas. These haul-back or lateral movement methods generally consist of an initial cut with the spoil deposited downslope or at some other site and spoil from the second cut refilling the first. A ridge of undisturbed natural material 15 to 20 ft (5 to 6 m) wide is often intentionally left at the outer edge of the mined area. This barrier adds stability to the reclaimed slope by preventing spoil from slumping or sliding downhill.")
        if v.get()==4:
            showinfo('Mountain Top Mining',"Mountaintop coal mining is a surface mining practice involving removal of mountaintops to expose coal seams, and disposing of associated mining overburden in adjacent valley fills. Valley fills occur in steep terrain where there are limited disposal alternatives.Mountaintop removal combines area and contour strip mining methods. In areas with rolling or steep terrain with a coal seam occurring near the top of a ridge or hill, the entire top is removed in a series of parallel cuts. Overburden is deposited in nearby valleys and hollows. This method usually leaves ridge and hill tops as flattened plateaus.[4] The process is highly controversial for the drastic changes in topography, the practice of creating head-of-hollow-fills, or filling in valleys with mining debris, and for covering streams and disrupting ecosystems")
        if v.get()==5:
            showinfo('Underground Mining',"Most coal seams are too deep underground for opencast mining and require underground mining, a method that currently accounts for about 60 percent of world coal production.[5] In deep mining, the room and pillar or bord and pillar method progresses along the seam, while pillars and timber are left standing to support the mine roof. Once room and pillar mines have been developed to a stopping point (limited by geology, ventilation, or economics), a supplementary version of room and pillar mining, termed second mining or retreat mining, is commonly started. Miners remove the coal in the pillars, thereby recovering as much coal from the coal seam as possible. A work area involved in pillar extraction is called a pillar section.")
    Button(form,text='See Details',command=fun).grid(row=7,column=0 )
    def funt():
        a=['','Surface Mining']
        b=['Strip Mining']
        c=['Contour Mining']
        d=['Mountain Top Mining']
        e=['Underground Mining']
        if v.get()==1:
            form.destroy()
            surface()
        if v.get()==2:
            form.destroy()
            strip()
        if v.get()==3:
            form.destroy()
            contour()
        if v.get()==4:
            form.destroy()
            mountaintop()
        if v.get()==5:
            form.destroy()
            underground()
        
    Button(form,text='Proceed',command=funt,bg='red').grid(row=7,column=1 )
    form.mainloop()
    
def surface():
    global forn
    forn=Tk()
    img = PhotoImage(file="ew.gif")
    Label(forn,image=img).grid(row=5,column=0)
    Label(forn,text='Surface Mining',font= "times 60 bold italic",bg='red').grid(row=0,column=0)
    Label(forn,text='About what do you want to know',font= "times 20",bg='Blue').grid(row=1,column=0)
    w=IntVar()
    r5=Radiobutton(forn,text="Machinery",variable=w,value=6)
    r5.grid(row=2,column=0)
    r6=Radiobutton(forn,text="Employees",variable=w,value=7)
    r6.grid(row=3,column=0)

    def fun1():
        if int(w.get()) == 6:
            machinery()
        if int(w.get()) == 7:
            employees()
            
        
    Button(forn,text='show',command=fun1).grid(row=4,column=0)
   
    Button(forn,text='back',command=main).grid(row=4,column=1)
    forn.mainloop()
def main():
    forn.destroy()
    profile()
def machinery():
    
    form1= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date(10),machinery varchar(20))")
    Label(form1,text='Machine details are as follows',font= "times 60 bold italic",bg='red').grid(row=0,column=0)
    Label(form1,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(form1)
    ab.grid(row=1,column=2)
    Label(form1,text="Workers needed").grid(row=2,column=0)
    ac=Entry(form1)
    ac.grid(row=2,column=2)
    Label(form1,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(form1)
    ad.grid(row=3,column=2)
    Label(form1,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(form1,text='Articulated dump truck',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(form1,text='Bucket wheel excavator',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(form1,text='Cable excavator',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(form1,text='Continuous miner',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(form1,text='Conveyor',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(form1,text='Crawler tractor',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(form1,text='Dragline',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(form1,text='Dredger',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(form1,text='Excavator',variable=ae,value=9)
    ae8.grid(row=10,column=0)
    ae9=Radiobutton(form1,text='Front Shovel',variable=ae,value=10)
    ae9.grid(row=10,column=2)
    ae10=Radiobutton(form1,text='Loader backhoe',variable=ae,value=11)
    ae10.grid(row=11,column=0)
    ae11=Radiobutton(form1,text='Motor grader',variable=ae,value=12)
    ae11.grid(row=11,column=2)
    ae12=Radiobutton(form1,text='Rock truck',variable=ae,value=13)
    ae12.grid(row=12,column=0)
    ae13=Radiobutton(form1,text='Water truck',variable=ae,value=14)
    ae13.grid(row=12,column=2)
    ae14=Radiobutton(form1,text='Wheel dozer',variable=ae,value=15)
    ae14.grid(row=13,column=0)
    ae15=Radiobutton(form1,text='Wheel loader',variable=ae,value=16)
    ae15.grid(row=13,column=2)
    
    def insert():
        u=(ae.get())
        if u==1:
            a="Articulated dump truck"
        elif u==2:
            a="Bucket wheel excavator"
        elif u==3:
            a="Cable excavator"
        elif u==4:
            a="Continuous miner"
        elif u==5:
            a="Conveyor"
        elif u==6:
            a="Crawler tractor"
        elif u==7:
            a="Dragline"
        elif u==8:
            a="Dredger"
        elif u==9:
            a="Excavator"
        elif u==10:
            a="Front Shovel"
        elif u==11:
            a="Loader backhoe"
        elif u==12:
            a="Motor grader"
        elif u==13:
            a="Rock truck"
        elif u==14:
            a="Water truck"
        elif u==15:
            a="Wheel dozer"
        elif u==16:
            a="Wheel loader"    
        else:
            a='0'
        
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        
        
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(form1,text="fetched record is:")
        Label(form1,text=a).grid(row=16,column=0)
    Button(form1,text='INSERT',command=insert).grid(row=14,column=0)
    Button(form1,text='SHOW ALL',command=showall).grid(row=14,column=2)

    form1.mainloop()

def employees():
    form2=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(form2,text='Employee details are as follows',font= "times 60 bold italic",bg='red').grid(row=0,column=0)
    Label(form2,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(form2)
    ba.grid(row=1,column=2)
    Label(form2,text="Enter First name").grid(row=2,column=0)
    bb=Entry(form2)
    bb.grid(row=2,column=2)
    Label(form2,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(form2)
    bc.grid(row=3,column=2)
    Label(form2,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(form2)
    bd.grid(row=4,column=2)
    Label(form2,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(form2)
    be.grid(row=5,column=2)
    Label(form2,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(form2)
    bf.grid(row=6,column=2)
    Label(form2,text="Select salary ").grid(row=7,column=0)
    bg=Entry(form2)
    bg.grid(row=7,column=2)
    Label(form2,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(form2,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(form2,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(form2,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(form2,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(form2,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(form2,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        Showinfo[text=="record created"]
        con.commit()
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(form2,text="fetched record is:")
        Label(form2,text=a).grid(row=16,column=0)
    Button(form2,text='INSERT',command=insert).grid(row=15,column=0)
    Button(form2,text='SHOW ALL',command=showall).grid(row=15,column=1)
    forn.destoy()
    
def strip():
    global form3
    form3=Tk()
    img = PhotoImage(file="st.gif")
    Label(form3,image=img).grid(row=5,column=0)
    Label(form3,text='Strip Mining',font= "times 60 bold italic",bg='red').grid(row=0,column=0)
    Label(form3,text='About what do you want to know',font= "times 20",bg='Blue').grid(row=1,column=0)
    x=IntVar()
    r1=Radiobutton(form3,text="Machinery",variable=x,value=1)
    r1.grid(row=2,column=0)
    r2=Radiobutton(form3,text="Employees",variable=x,value=2)
    r2.grid(row=3,column=0)

    def fun2():
        if int(x.get()) == 1:
            machinery1()
        if int(x.get()) == 2:
            employees1()
            
        
    Button(form3,text='show2',command=fun2).grid(row=4,column=0)
    Button(form3,text='back',command=main10).grid(row=4,column=1)
    form3.mainloop()
def main10():
    form3.destroy()
    profile()
   
    
def machinery1():
    
    form4= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date,machinery varchar(20))")
    Label(form4,text='Machine details are as follows',font= "times 60 bold italic",bg='purple').grid(row=0,column=0)
    Label(form4,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(form4)
    ab.grid(row=1,column=2)
    Label(form4,text="Workers needed").grid(row=2,column=0)
    ac=Entry(form4)
    ac.grid(row=2,column=2)
    Label(form4,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(form4)
    ad.grid(row=3,column=2)
    Label(form4,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(form4,text='Articulated dump truck',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(form4,text='Bucket wheel excavator',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(form4,text='Cable excavator',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(form4,text='Continuous miner',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(form4,text='Conveyor',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(form4,text='Crawler tractor',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(form4,text='Dragline',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(form4,text='Dredger',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(form4,text='Excavator',variable=ae,value=9)
    ae8.grid(row=10,column=0)
    ae9=Radiobutton(form4,text='Front Shovel',variable=ae,value=10)
    ae9.grid(row=10,column=2)
    ae10=Radiobutton(form4,text='Loader backhoe',variable=ae,value=11)
    ae10.grid(row=11,column=0)
    ae11=Radiobutton(form4,text='Motor grader',variable=ae,value=12)
    ae11.grid(row=11,column=2)
    ae12=Radiobutton(form4,text='Rock truck',variable=ae,value=13)
    ae12.grid(row=12,column=0)
    ae13=Radiobutton(form4,text='Water truck',variable=ae,value=14)
    ae13.grid(row=12,column=2)
    ae14=Radiobutton(form4,text='Wheel dozer',variable=ae,value=15)
    ae14.grid(row=13,column=0)
    ae15=Radiobutton(form4,text='Wheel loader',variable=ae,value=16)
    ae15.grid(row=13,column=2)
    
    def insert():
        u=(ae.get())
        if u==1:
            a="Articulated dump truck"
        elif u==2:
            a="Bucket wheel excavator"
        elif u==3:
            a="Cable excavator"
        elif u==4:
            a="Continuous miner"
        elif u==5:
            a="Conveyor"
        elif u==6:
            a="Crawler tractor"
        elif u==7:
            a="Dragline"
        elif u==8:
            a="Dredger"
        elif u==9:
            a="Excavator"
        elif u==10:
            a="Front Shovel"
        elif u==11:
            a="Loader backhoe"
        elif u==12:
            a="Motor grader"
        elif u==13:
            a="Rock truck"
        elif u==14:
            a="Water truck"
        elif u==15:
            a="Wheel dozer"
        elif u==16:
            a="Wheel loader"    
        else:
            a='0'
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        
        
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(form4,text="fetched record is:")
        Label(form4,text=a).grid(row=16,column=0)
    Button(form4,text='INSERT',command=insert).grid(row=14,column=0)
    Button(form4,text='SHOW ALL',command=showall).grid(row=14,column=2)

    form4.mainloop()

def employees1():
    form5=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(form5,text='Employee details are as follows',font= "times 60 bold italic",bg='red').grid(row=0,column=0)
    Label(form5,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(form5)
    ba.grid(row=1,column=2)
    Label(form5,text="Enter First name").grid(row=2,column=0)
    bb=Entry(form5)
    bb.grid(row=2,column=2)
    Label(form5,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(form5)
    bc.grid(row=3,column=2)
    Label(form5,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(form5)
    bd.grid(row=4,column=2)
    Label(form5,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(form5)
    be.grid(row=5,column=2)
    Label(form5,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(form5)
    bf.grid(row=6,column=2)
    Label(form5,text="Select salary ").grid(row=7,column=0)
    bg=Entry(form5)
    bg.grid(row=7,column=2)
    Label(form5,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(form5,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(form5,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(form5,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(form5,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(form5,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(form5,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        con.commit()
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(form5,text="fetched record is:")
        Label(form5,text=a).grid(row=16,column=0)
    Button(form5,text='INSERT',command=insert).grid(row=15,column=0)
    Button(form5,text='SHOW ALL',command=showall).grid(row=15,column=1)

def contour():
    global con1
    con1=Tk()
    img = PhotoImage(file="su.gif")
    Label(con1,image=img).grid(row=5,column=0)
    Label(con1,text='Contour Mining',font= "times 60 bold italic",bg='Brown').grid(row=0,column=0)
    Label(con1,text='About what do you want to know',font= "times 20",bg='Blue').grid(row=1,column=0)
    y=IntVar()
    r1=Radiobutton(con1,text="Machinery",variable=y,value=35)
    r1.grid(row=2,column=0)
    r2=Radiobutton(con1,text="Employees",variable=y,value=36)
    r2.grid(row=3,column=0)

    def fun3():
        if int(y.get()) == 35:
            machinery2()
        if int(y.get()) == 36:
            employees2()
            
        
    Button(con1,text='show3',command=fun3).grid(row=4,column=0)
    Button(con1,text='back',command=main9).grid(row=4,column=1)
    con1.mainloop()
def main9():
    con1.destroy()
    profile()
    
def machinery2():
    
    mac3= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date,machinery varchar(20))")
    Label(mac3,text='Machine details are as follows',font= "times 60 bold italic",bg='orange').grid(row=0,column=0)
    Label(mac3,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(mac3)
    ab.grid(row=1,column=2)
    Label(mac3,text="Workers needed").grid(row=2,column=0)
    ac=Entry(mac3)
    ac.grid(row=2,column=2)
    Label(mac3,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(mac3)
    ad.grid(row=3,column=2)
    Label(mac3,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(mac3,text='D8-D11 Dozers',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(mac3,text='980-993 Wheel Loaders',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(mac3,text='Articulated Trucks',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(mac3,text='773-793 Trucks',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(mac3,text='Highwall Miner',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(mac3,text='329-390 Excavators',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(mac3,text='14-16 Motorgraders',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(mac3,text='Drills (Rotary and Track)',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(mac3,text='Hydraulic Mining Shovels',variable=ae,value=9)
    ae8.grid(row=10,column=0)
    
    
    def insert():
        u=(ae.get())
        if u==1:
            a="D8-D11 Dozers"
        elif u==2:
            a="980-993 Wheel Loaders"
        elif u==3:
            a="Articulated Trucks"
        elif u==4:
            a="773-793 Trucks"
        elif u==5:
            a="Highwall Miner"
        elif u==6:
            a="329-390 Excavators"
        elif u==7:
            a="14-16 Motorgraders"
        elif u==8:
            a="Drills (Rotary and Track)"
        elif u==9:
            a="Hydraulic Mining Shovels"
            
        else:
            a='0'
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(mac3,text="fetched record is:")
        Label(mac3,text=a).grid(row=16,column=0)
    Button(mac3,text='INSERT',command=insert).grid(row=14,column=0)
    Button(mac3,text='SHOW ALL',command=showall).grid(row=14,column=2)
    mac3.mainloop()

def employees2():
    emp3=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(emp3,text='Employee details are as follows',font= "times 60 bold italic",bg='pink').grid(row=0,column=0)
    Label(emp3,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(emp3)
    ba.grid(row=1,column=2)
    Label(emp3,text="Enter First name").grid(row=2,column=0)
    bb=Entry(emp3)
    bb.grid(row=2,column=2)
    Label(emp3,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(emp3)
    bc.grid(row=3,column=2)
    Label(emp3,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(emp3)
    bd.grid(row=4,column=2)
    Label(emp3,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(emp3)
    be.grid(row=5,column=2)
    Label(emp3,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(emp3)
    bf.grid(row=6,column=2)
    Label(emp3,text="Select salary ").grid(row=7,column=0)
    bg=Entry(emp3)
    bg.grid(row=7,column=2)
    Label(emp3,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(emp3,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(emp3,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(emp3,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(emp3,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(emp3,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(emp3,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        con.commit()
        
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(emp3,text="fetched record is:")
        Label(emp3,text=a).grid(row=16,column=0)
    Button(emp3,text='INSERT',command=insert).grid(row=15,column=0)
    Button(emp3,text='SHOW ALL',command=showall).grid(row=15,column=1)

def mountaintop():
    global mou
    mou=Tk()
    img = PhotoImage(file="mo.gif")
    Label(mou,image=img).grid(row=5,column=0)
    Label(mou,text='Mountaintop Mining',font= "times 60 bold italic",bg='Pink').grid(row=0,column=0)
    Label(mou,text='About what do you want to know',font= "times 20",bg='Gray').grid(row=1,column=0)
    z=IntVar()
    r1=Radiobutton(mou,text="Machinery",variable=z,value=50)
    r1.grid(row=2,column=0)
    r2=Radiobutton(mou,text="Employees",variable=z,value=51)
    r2.grid(row=3,column=0)

    def fun4():
        if int(z.get()) == 50:
            machinery3()
        if int(z.get()) == 51:
            employees3()
            
    Button(mou,text='show4',command=fun4).grid(row=4,column=0)
    Button(mou,text='back',command=main8).grid(row=4,column=1)
    mou.mainloop()
def main8():
    mou.destroy()
    profile()
    
def machinery3():
    
    mac4= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date,machinery varchar(20))")
    Label(mac4,text='Machine details are as follows',font= "times 60 bold italic",bg='yellow').grid(row=0,column=0)
    Label(mac4,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(mac4)
    ab.grid(row=1,column=2)
    Label(mac4,text="Workers needed").grid(row=2,column=0)
    ac=Entry(mac4)
    ac.grid(row=2,column=2)
    Label(mac4,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(mac4)
    ad.grid(row=3,column=2)
    Label(mac4,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(mac4,text='Ball Mill',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(mac4,text='Belt Conveyor',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(mac4,text='BWZ Heavy Duty Apron Feeder',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(mac4,text='CS Cone Crusher',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(mac4,text='Hammer Crusher',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(mac4,text='HJ Series Jaw Crusher',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(mac4,text='HPC Cone Crusher',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(mac4,text='HST Cone Crusher',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(mac4,text='K Series Mobile Crushing Plant',variable=ae,value=9)
    ae8.grid(row=10,column=0)
    ae9=Radiobutton(mac4,text='LM Vertical Grinding Mills',variable=ae,value=10)
    ae9.grid(row=10,column=2)
    ae10=Radiobutton(mac4,text='LSX Sand Washing Machine',variable=ae,value=11)
    ae10.grid(row=11,column=0)
    ae11=Radiobutton(mac4,text='Mobile Jaw Crusher',variable=ae,value=12)
    
    
    def insert():
        u=(ae.get())
        if u==1:
            a="'Ball Mill"
        elif u==2:
            a="Belt Conveyor"
        elif u==3:
            a="BWZ Heavy Duty Apron Feeder"
        elif u==4:
            a="CS Cone Crusher"
        elif u==5:
            a="Hammer Crusher"
        elif u==6:
            a="HJ Series Jaw Crusher"
        elif u==7:
            a="HPC Cone Crusher"
        elif u==8:
            a="HST Cone Crusher"
        elif u==9:
            a="K Series Mobile Crushing Plant"
        elif u==10:
            a="LM Vertical Grinding Mills"
        elif u==11:
            a="LSX Sand Washing Machine"
        elif u==12:
            a="Mobile Jaw Crusher"
            
        else:
            a='0'
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(mac4,text="fetched record is:")
        Label(mac4,text=a).grid(row=16,column=0)
    Button(mac4,text='INSERT',command=insert).grid(row=14,column=0)
    Button(mac4,text='SHOW ALL',command=showall).grid(row=14,column=2)

    mac4.mainloop()

def employees3():
    emp4=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(emp4,text='Employee details are as follows',font= "times 60 bold italic",bg='red').grid(row=0,column=0)
    Label(emp4,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(emp4)
    ba.grid(row=1,column=2)
    Label(emp4,text="Enter First name").grid(row=2,column=0)
    bb=Entry(emp4)
    bb.grid(row=2,column=2)
    Label(emp4,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(emp4)
    bc.grid(row=3,column=2)
    Label(emp4,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(emp4)
    bd.grid(row=4,column=2)
    Label(emp4,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(emp4)
    be.grid(row=5,column=2)
    Label(emp4,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(emp4)
    bf.grid(row=6,column=2)
    Label(emp4,text="Select salary ").grid(row=7,column=0)
    bg=Entry(emp4)
    bg.grid(row=7,column=2)
    Label(emp4,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(emp4,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(emp4,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(emp4,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(emp4,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(emp4,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(emp4,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        con.commit()
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(emp4,text="fetched record is:")
        Label(emp4,text=a).grid(row=16,column=0)
    Button(emp4,text='INSERT',command=insert).grid(row=15,column=0)
    Button(emp4,text='SHOW ALL',command=showall).grid(row=15,column=1)


def underground():
    global und
    und=Toplevel()
    Label(und,text='Underground Mining',font= "times 60 bold italic",bg='silver').grid(row=0,column=0)
    Label(und,text='Methods of UnderGround Mining',font= "times 20",bg='green').grid(row=1,column=0)
    un=IntVar()
    r5=Radiobutton(und,text="Longwall Mining",variable=un,value=101)
    r5.grid(row=2,column=0)
    r6=Radiobutton(und,text="Continuous Mining",variable=un,value=102)
    r6.grid(row=3,column=0)
    r7=Radiobutton(und,text="Room and Pillar Mining",variable=un,value=103)
    r7.grid(row=4,column=0)
    r8=Radiobutton(und,text="Blast Mining",variable=un,value=104)
    r8.grid(row=5,column=0)
    r9=Radiobutton(und,text="Shortwall Mining",variable=un,value=105)
    r9.grid(row=6,column=0)
    r10=Radiobutton(und,text="Retreat Mining",variable=un,value=106)
    r10.grid(row=7,column=0)

    def fun5():
        a1=['Longwall Mining']
        b1=['Continuous Mining']
        c1=['Room and Pillar Mining']
        d1=['Blast Mining']
        e1=['Shortwall Mining']
        f1=['Retreat Mining']
        if un.get()==101:
            showinfo('Longwall Mining',"Longwall mining accounts for about 50 percent of underground production. The longwall shearer has a face of 1,000 feet (300 m) or more. It is a sophisticated machine with a rotating drum that moves mechanically back and forth across a wide coal seam. The loosened coal falls onto an armored chain conveyor or pan line that takes the coal to the conveyor belt for removal from the work area. Longwall systems have their own hydraulic roof supports which advance with the machine as mining progresses. As the longwall mining equipment moves forward, overlying rock that is no longer supported by coal is allowed to fall behind the operation in a controlled manner. The supports make possible high levels of production and safety. Sensors detect how much coal remains in the seam while robotic controls enhance efficiency. Longwall systems allow a 60-to-100 percent coal recovery rate when surrounding geology allows their use. Once the coal is removed, usually 75 percent of the section, the roof is allowed to collapse in a safe manner.")
        if un.get()==102:
            showinfo('Continuous Mining',"Continuous mining utilizes a Continuous Miner Machine with a large rotating steel drum equipped with tungsten carbide picks that scrape coal from the seam. Operating in a “room and pillar” (also known as “bord and pillar”) system—where the mine is divided into a series of 20-to-30-foot (5–10 m) “rooms” or work areas cut into the coalbed—it can mine as much as 14 tons of coal a minute, more than a non-mechanised mine of the 1920s would produce in an entire day. Continuous miners account for about 45 percent of underground coal production. Conveyors transport the removed coal from the seam. Remote-controlled continuous miners are used to work in a variety of difficult seams and conditions, and robotic versions controlled by computers are becoming increasingly common. Continuous mining is a misnomer, as room and pillar coal mining is very cyclical. In the US, one can generally cut 20 feet (6 meters) (or a bit more with MSHA permission) (12 meters or roughly 40 ft in South Africa before the Continuous Miner goes out and the roof is supported by the Roof Bolter), after which, the face has to be serviced, before it can be advanced again. During servicing, the continuous miner moves to another face. Some continuous miners can bolt and rock dust the face (two major components of servicing) while cutting coal, while a trained crew may be able to advance ventilation, to truly earn the continuous label. However, very few mines are able to achieve it. Most continuous mining machines in use in the US lack the ability to bolt and dust. This may partly be because incorporation of bolting makes the machines wider, and therefore, less maneuverable.")
        if un.get()==103:
            showinfo('Room and Pillar Mining',"Room and pillar mining consists of coal deposits that are mined by cutting a network of rooms into the coal seam. Pillars of coal are left behind in order to keep up the roof. The pillars can make up to forty percent of the total coal in the seam, however where there was space to leave head and floor coal there is evidence from recent open cast excavations that 18th-century operators used a variety of room and pillar techniques to remove 92 percent of the in situ coal. However, this can be extracted at a later stage (see retreat mining).")
        if un.get()==104:
            showinfo('Blast Mining',"Blast mining or conventional mining, is an older practice that uses explosives such as dynamite to break up the coal seam, after which the coal is gathered and loaded onto shuttle cars or conveyors for removal to a central loading area. This process consists of a series of operations that begins with “cutting” the coalbed so it will break easily when blasted with explosives. This type of mining accounts for less than 5 percent of total underground production in the US today.")
        if un.get()==105:
            showinfo('Shortwall Mining',"Shortwall mining, a method currently accounting for less than 1 percent of deep coal production, involves the use of a continuous mining machine with movable roof supports, similar to longwall. The continuous miner shears coal panels 150 to 200 feet (45 to 60 metres) wide and more than a half-mile (1 km) long, having regard to factors such as geological strata.")
        if un.get()==106:
            showinfo('Retreat Mining',"Retreat mining is a method in which the pillars or coal ribs used to hold up the mine roof are extracted; allowing the mine roof to collapse as the mining works back towards the entrance. This is one of the most dangerous forms of mining, owing to imperfect predictability of when the roof will collapse and possibly crush or trap workers in the mine.")
    Button(und,text='See Details',command=fun5).grid(row=8,column=0 )

    def funt2():
        a1=['Longwall Mining']
        b1=['Continuous Mining']
        c1=['Room and Pillar Mining']
        d1=['Blast Mining']
        e1=['Shortwall Mining']
        f1=['Retreat Mining']
        if un.get()==101:
            und.destroy()
            longwall()
        if un.get()==102:
            und.destroy()
            continuous()
        if un.get()==103:
            und.destroy()
            room()
        if un.get()==104:
            und.destroy()
            blast()
        if un.get()==105:
            und.destroy()
            shortwall()
        if un.get()==106:
            und.destroy()
            retreat()
    Button(und,text='Proceed',command=funt2).grid(row=8,column=1 )
    Button(und,text='back',command=main7).grid(row=9,column=0)
    und.mainloop()
def main7():
    und.destroy()
    profile()

def longwall():
    global lon3
    lon3=Toplevel()
    img = PhotoImage(file="ln.gif")
    Label(lon3,image=img).grid(row=5,column=0)
    Label(lon3,text='longwall Mining',font= "times 60 bold italic",bg='green').grid(row=0,column=0)
    Label(lon3,text='About what do you want to know',font= "times 20",bg='orange').grid(row=1,column=0)
    ln=IntVar()
    l5=Radiobutton(lon3,text="Machinery",variable=ln,value=60)
    l5.grid(row=2,column=0)
    l6=Radiobutton(lon3,text="Employees",variable=ln,value=61)
    l6.grid(row=3,column=0)

    def fun1():
        if int(ln.get()) == 60:
            machinery11()
        if int(ln.get()) == 61:
            employees11()
            
        
    Button(lon3,text='showa11',command=fun1).grid(row=4,column=0)
    Button(lon3,text='back',command=main6).grid(row=4,column=1)
    lon3.mainloop()
def main6():
    lon3.destroy()
    underground() 
def machinery11():
    
    mac11= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date,machinery varchar(20))")
    Label(mac11,text='Machine details are as follows',font= "times 60 bold italic",bg='purple').grid(row=0,column=0)
    Label(mac11,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(mac11)
    ab.grid(row=1,column=2)
    Label(mac11,text="Workers needed").grid(row=2,column=0)
    ac=Entry(mac11)
    ac.grid(row=2,column=2)
    Label(mac11,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(mac11)
    ad.grid(row=3,column=2)
    Label(mac11,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(mac11,text='Longwall Shearers',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(mac11,text='Plow System',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(mac11,text='Armoured Face Conveyors',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(mac11,text='Longwall Facebolte',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(mac11,text='Roof Support Carriers',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(mac11,text=' Roadheaders',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(mac11,text=' roof support equipments of gate roads',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(mac11,text=' Power Drive System',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(mac11,text=' exploratory and blast hole drilling for gate roads',variable=ae,value=9)
    ae8.grid(row=10,column=0)
    ae9=Radiobutton(mac11,text='conveyor belts',variable=ae,value=10)
    ae9.grid(row=10,column=2)
    
    def insert():
        u=(ae.get())
        if u==1:
            a="Longwall Shearers"
        elif u==2:
            a="Plow System"
        elif u==3:
            a="Armoured Face Conveyors"
        elif u==4:
            a="Longwall Facebolte"
        elif u==5:
            a="Roof Support Carriers"
        elif u==6:
            a="Roadheaders"
        elif u==7:
            a="roof support equipments of gate roads"
        elif u==8:
            a="Power Drive System"
        elif u==9:
            a="exploratory and blast hole drilling for gate roads"
        elif u==10:
            a="conveyor belts"    
        else:
            a='0'
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(mac11,text="fetched record is:")
        Label(mac11,text=a).grid(row=16,column=0)
    Button(mac11,text='INSERT',command=insert).grid(row=14,column=0)
    Button(mac11,text='SHOW ALL',command=showall).grid(row=14,column=2)

    mac11.mainloop()

def employees11():
    emp11=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(emp11,text='Employee details are as follows',font= "times 60 bold italic",bg='sky blue').grid(row=0,column=0)
    Label(emp11,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(emp11)
    ba.grid(row=1,column=2)
    Label(emp11,text="Enter First name").grid(row=2,column=0)
    bb=Entry(emp11)
    bb.grid(row=2,column=2)
    Label(emp11,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(emp11)
    bc.grid(row=3,column=2)
    Label(emp11,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(emp11)
    bd.grid(row=4,column=2)
    Label(emp11,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(emp11)
    be.grid(row=5,column=2)
    Label(emp11,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(emp11)
    bf.grid(row=6,column=2)
    Label(emp11,text="Select salary ").grid(row=7,column=0)
    bg=Entry(emp11)
    bg.grid(row=7,column=2)
    Label(emp11,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(emp11,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(emp11,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(emp11,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(emp11,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(emp11,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(emp11,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        con.commit()
        
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(emp11,text="fetched record is:")
        Label(emp11,text=a).grid(row=16,column=0)
    Button(emp11,text='INSERT',command=insert).grid(row=15,column=0)
    Button(emp11,text='SHOW ALL',command=showall).grid(row=15,column=1)

def continuous():
    global con5
    con5=Toplevel()
    img = PhotoImage(file="el.gif")
    Label(con5,image=img).grid(row=5,column=0)
    Label(con5,text='Continuous Mining',font= "times 60 bold italic",bg='green').grid(row=0,column=0)
    Label(con5,text='About what do you want to know',font= "times 20",bg='orange').grid(row=1,column=0)
    co=IntVar()
    l5=Radiobutton(con5,text="Machinery",variable=co,value=62)
    l5.grid(row=2,column=0)
    l6=Radiobutton(con5,text="Employees",variable=co,value=63)
    l6.grid(row=3,column=0)

    def fun1():
        if int(co.get()) == 62:
            machinery12()
        if int(co.get()) == 63:
            employees12()
            
        
    Button(con5,text='show11',command=fun1).grid(row=4,column=0)
    Button(con5,text='back',command=main5).grid(row=4,column=1)
    con5.mainloop()
def main5():
    con5.destroy()
    underground()    
def machinery12():
    
    mac12= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date,machinery varchar(20))")
    Label(mac12,text='Machine details are as follows',font= "times 60 bold italic",bg='purple').grid(row=0,column=0)
    Label(mac12,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(mac12)
    ab.grid(row=1,column=2)
    Label(mac12,text="Workers needed").grid(row=2,column=0)
    ac=Entry(mac12)
    ac.grid(row=2,column=2)
    Label(mac12,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(mac12)
    ad.grid(row=3,column=2)
    Label(mac12,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(mac12,text='Ball Mill',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(mac12,text='Mobile Jaw Crusher',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(mac12,text='MTM Trapezium Grinder',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(mac12,text='MTW Milling Machine',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(mac12,text='PE Jaw Crusher',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(mac12,text='PEW Jaw Crusher',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(mac12,text='PF Impact Crusher',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(mac12,text='PFW Impact Crusher',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(mac12,text='VSI5X Crusher',variable=ae,value=9)
    ae8.grid(row=10,column=0)
        
    def insert():
        u=(ae.get())
        if u==1:
            a="Ball Mill"
        elif u==2:
            a="Mobile Jaw Crusher"
        elif u==3:
            a="MTM Trapezium Grinder"
        elif u==4:
            a="MTW Milling Machine"
        elif u==5:
            a="PE Jaw Crusher"
        elif u==6:
            a="PEW Jaw Crusher"
        elif u==7:
            a="PF Impact Crusher"
        elif u==8:
            a="PFW Impact Crusher"
        elif u==9:
            a="VSI5X Crusher" 
        else:
            a='0'
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(mac12,text="fetched record is:")
        Label(mac12,text=a).grid(row=16,column=0)
    Button(mac12,text='INSERT',command=insert).grid(row=14,column=0)
    Button(mac12,text='SHOW ALL',command=showall).grid(row=14,column=2)
    mac12.mainloop()

def employees12():
    emp12=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(emp12,text='Employee details are as follows',font= "times 60 bold italic",bg='sky blue').grid(row=0,column=0)
    Label(emp12,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(emp12)
    ba.grid(row=1,column=2)
    Label(emp12,text="Enter First name").grid(row=2,column=0)
    bb=Entry(emp12)
    bb.grid(row=2,column=2)
    Label(emp12,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(emp12)
    bc.grid(row=3,column=2)
    Label(emp12,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(emp12)
    bd.grid(row=4,column=2)
    Label(emp12,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(emp12)
    be.grid(row=5,column=2)
    Label(emp12,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(emp12)
    bf.grid(row=6,column=2)
    Label(emp12,text="Select salary ").grid(row=7,column=0)
    bg=Entry(emp12)
    bg.grid(row=7,column=2)
    Label(emp12,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(emp12,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(emp12,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(emp12,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(emp12,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(emp12,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(emp12,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        con.commit()
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(emp12,text="fetched record is:")
        Label(emp12,text=a).grid(row=16,column=0)
    Button(emp12,text='INSERT',command=insert).grid(row=15,column=0)
    Button(emp12,text='SHOW ALL',command=showall).grid(row=15,column=1)

def room():
    global roo
    roo=Toplevel()
    img = PhotoImage(file="rm.gif")
    Label(roo,image=img).grid(row=5,column=0)
    Label(roo,text='Room and Pillar',font= "times 60 bold italic",bg='green').grid(row=0,column=0)
    Label(roo,text='About what do you want to know',font= "times 20",bg='orange').grid(row=1,column=0)
    ln=IntVar()
    l5=Radiobutton(roo,text="Machinery",variable=ln,value=60)
    l5.grid(row=2,column=0)
    l6=Radiobutton(roo,text="Employees",variable=ln,value=61)
    l6.grid(row=3,column=0)

    def fun1():
        if int(ln.get()) == 60:
            machinery11()
        if int(ln.get()) == 61:
            employees11()
            
        
    Button(roo,text='show11',command=fun1).grid(row=4,column=0)
    Button(roo,text='back',command=main4).grid(row=4,column=1)
    roo.mainloop()
def main4():
    roo.destroy()
    underground()
    
def machinery11():
    
    mac13= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date,machinery varchar(20))")
    Label(mac13,text='Machine details are as follows',font= "times 60 bold italic",bg='purple').grid(row=0,column=0)
    Label(mac13,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(mac13)
    ab.grid(row=1,column=2)
    Label(mac13,text="Workers needed").grid(row=2,column=0)
    ac=Entry(mac13)
    ac.grid(row=2,column=2)
    Label(mac13,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(mac13)
    ad.grid(row=3,column=2)
    Label(mac13,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(mac13,text='Continuous Haulage Machines',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(mac13,text='Continuous Miners',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(mac13,text='Face Haulers',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(mac13,text='Feeder Breakers',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(mac13,text='Roof Bolters',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(mac13,text='Scoops',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(mac13,text='VSI Crusher',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(mac13,text='Hammer Crusher',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(mac13,text='PY Cone Crusher',variable=ae,value=9)
    ae8.grid(row=10,column=0)
    ae9=Radiobutton(mac13,text='HPC Cone Crusher',variable=ae,value=10)
    ae9.grid(row=10,column=2)
    ae10=Radiobutton(mac13,text='PFW Impact Crusher',variable=ae,value=11)
    ae10.grid(row=11,column=0)
    ae11=Radiobutton(mac13,text='Raymond Mill',variable=ae,value=12)
    ae11.grid(row=11,column=2)
    ae12=Radiobutton(mac13,text='Belt Conveyor',variable=ae,value=13)
    ae12.grid(row=12,column=0)
    ae13=Radiobutton(mac13,text='XSD Sand Washer',variable=ae,value=14)
    ae13.grid(row=12,column=2)
    ae14=Radiobutton(mac13,text='Wharf Belt Conveyor',variable=ae,value=15)
    ae14.grid(row=13,column=0)
    ae15=Radiobutton(mac13,text='Mobile Jaw Crusher',variable=ae,value=16)
    ae15.grid(row=13,column=2)
    
    def insert():
        u=(ae.get())
        if u==1:
            a="Continuous Haulage Machines"
        elif u==2:
            a="Continuous Miners"
        elif u==3:
            a="Face Haulers"
        elif u==4:
            a="Feeder Breakers"
        elif u==5:
            a="Roof Bolters"
        elif u==6:
            a="Scoops"
        elif u==7:
            a="VSI Crusher"
        elif u==8:
            a="Hammer Crusher"
        elif u==9:
            a="PY Cone Crusher"
        elif u==10:
            a="HPC Cone Crusher"
        elif u==11:
            a="PFW Impact Crusher"
        elif u==12:
            a="Raymond Mill"
        elif u==13:
            a="Belt Conveyor"
        elif u==14:
            a="XSD Sand Washer"
        elif u==15:
            a="Wharf Belt Conveyor"
        elif u==16:
            a="Mobile Jaw Crusher"    
        else:
            a='0'
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(mac13,text="fetched record is:")
        Label(mac13,text=a).grid(row=16,column=0)
    Button(mac13,text='INSERT',command=insert).grid(row=14,column=0)
    Button(mac13,text='SHOW ALL',command=showall).grid(row=14,column=2)

    mac13.mainloop()

def employees11():
    emp13=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(emp13,text='Employee details are as follows',font= "times 60 bold italic",bg='sky blue').grid(row=0,column=0)
    Label(emp13,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(emp13)
    ba.grid(row=1,column=2)
    Label(emp13,text="Enter First name").grid(row=2,column=0)
    bb=Entry(emp13)
    bb.grid(row=2,column=2)
    Label(emp13,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(emp13)
    bc.grid(row=3,column=2)
    Label(emp13,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(emp13)
    bd.grid(row=4,column=2)
    Label(emp13,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(emp13)
    be.grid(row=5,column=2)
    Label(emp13,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(emp13)
    bf.grid(row=6,column=2)
    Label(emp13,text="Select salary ").grid(row=7,column=0)
    bg=Entry(emp13)
    bg.grid(row=7,column=2)
    Label(emp13,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(emp13,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(emp13,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(emp13,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(emp13,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(emp13,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(emp13,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        con.commit()
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(emp13,text="fetched record is:")
        Label(emp13,text=a).grid(row=16,column=0)
    Button(emp13,text='INSERT',command=insert).grid(row=15,column=0)
    Button(emp13,text='SHOW ALL',command=showall).grid(row=15,column=1)

def blast():
    global bla
    bla=Toplevel()
    a=PhotoImage(file="db.gif")
    Label(bla,image=a).grid(row=5, column=0 )
    Label(bla,text='Blast Mining',font= "times 60 bold italic",bg='green').grid(row=0,column=0)
    Label(bla,text='About what do you want to know',font= "times 20",bg='orange').grid(row=1,column=0)
    ln=IntVar()
    l5=Radiobutton(bla,text="Machinery",variable=ln,value=60)
    l5.grid(row=2,column=0)
    l6=Radiobutton(bla,text="Employees",variable=ln,value=61)
    l6.grid(row=3,column=0)

    def fun1():
        if int(ln.get()) == 60:
            machinery11()
        if int(ln.get()) == 61:
            employees11()
            
        
    Button(bla,text='show11',command=fun1,bg='yellow').grid(row=4,column=0)
    Button(bla,text='back',command=main3,bg='yellow').grid(row=4,column=1)
    bla.mainloop()
def main3():
    bla.destroy()
    underground()
    
def machinery11():
    
    mac14= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date,machinery varchar(20))")
    Label(mac14,text='Machine details are as follows',font= "times 60 bold italic",bg='purple').grid(row=0,column=0)
    Label(mac14,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(mac14)
    ab.grid(row=1,column=2)
    Label(mac14,text="Workers needed").grid(row=2,column=0)
    ac=Entry(mac14)
    ac.grid(row=2,column=2)
    Label(mac14,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(mac14)
    ad.grid(row=3,column=2)
    Label(mac14,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(mac14,text='Rock bolts',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(mac14,text='rock dowels',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(mac14,text='Shotcrete',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(mac14,text='Ribs or mining arches and lagging',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(mac14,text='Cable bolts',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(mac14,text='Crawler tractor',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(mac14,text='In-situ concrete',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(mac14,text='Dredger',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(mac14,text='Excavator',variable=ae,value=9)
    ae8.grid(row=10,column=0)
    ae9=Radiobutton(mac14,text='Front Shovel',variable=ae,value=10)
    ae9.grid(row=10,column=2)
    ae10=Radiobutton(mac14,text='Loader backhoe',variable=ae,value=11)
    ae10.grid(row=11,column=0)
    ae11=Radiobutton(mac14,text='Motor grader',variable=ae,value=12)
    ae11.grid(row=11,column=2)
    
    def insert():
        u=(ae.get())
        if u==1:
            a="Rock bolts"
        elif u==2:
            a="rock dowels"
        elif u==3:
            a="Shotcrete"
        elif u==4:
            a="Ribs or mining arches and lagging"
        elif u==5:
            a="Cable bolts"
        elif u==6:
            a="Crawler tractor"
        elif u==7:
            a="In-situ concrete"
        elif u==8:
            a="Dredger"
        elif u==9:
            a="Excavator"
        elif u==10:
            a="Front Shovel"
        elif u==11:
            a="Loader backhoe"
        elif u==12:
            a="Motor grader"   
        else:
            a='0'
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(mac14,text="fetched record is:")
        Label(mac14,text=a).grid(row=16,column=0)
    Button(mac14,text='INSERT',command=insert).grid(row=14,column=0)
    Button(mac14,text='SHOW ALL',command=showall).grid(row=14,column=2)
    mac14.mainloop()

def employees11():
    emp14=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(emp14,text='Employee details are as follows',font= "times 60 bold italic",bg='sky blue').grid(row=0,column=0)
    Label(emp14,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(emp14)
    ba.grid(row=1,column=2)
    Label(emp14,text="Enter First name").grid(row=2,column=0)
    bb=Entry(emp14)
    bb.grid(row=2,column=2)
    Label(emp14,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(emp14)
    bc.grid(row=3,column=2)
    Label(emp14,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(emp14)
    bd.grid(row=4,column=2)
    Label(emp14,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(emp14)
    be.grid(row=5,column=2)
    Label(emp14,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(emp14)
    bf.grid(row=6,column=2)
    Label(emp14,text="Select salary ").grid(row=7,column=0)
    bg=Entry(emp14)
    bg.grid(row=7,column=2)
    Label(emp14,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(emp14,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(emp14,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(emp14,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(emp14,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(emp14,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(emp14,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        con.commit()
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(emp14,text="fetched record is:")
        Label(emp14,text=a).grid(row=16,column=0)
    Button(emp14,text='INSERT',command=insert).grid(row=15,column=0)
    Button(emp14,text='SHOW ALL',command=showall).grid(row=15,column=1)

def shortwall():
    global sh
    sh=Toplevel()
    img = PhotoImage(file="sh.gif")
    Label(sh,image=img).grid(row=5,column=0)
    Label(sh,text='Shortwall Mining',font= "times 60 bold italic",bg='green').grid(row=0,column=0)
    Label(sh,text='About what do you want to know',font= "times 20",bg='orange').grid(row=1,column=0)
    ln=IntVar()
    l5=Radiobutton(sh,text="Machinery",variable=ln,value=60)
    l5.grid(row=2,column=0)
    l6=Radiobutton(sh,text="Employees",variable=ln,value=61)
    l6.grid(row=3,column=0)

    def fun1():
        if int(ln.get()) == 60:
            machinery11()
        if int(ln.get()) == 61:
            employees11()
            
        
    Button(sh,text='show11',command=fun1).grid(row=4,column=0)
    Button(sh,text='back',command=main2).grid(row=4,column=1)
    sh.mainloop()
def main2():
    sh.destroy()
    underground()   
def machinery11():
    
    mac15= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date,machinery varchar(20))")
    Label(mac15,text='Machine details are as follows',font= "times 60 bold italic",bg='purple').grid(row=0,column=0)
    Label(mac15,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(mac15)
    ab.grid(row=1,column=2)
    Label(mac15,text="Workers needed").grid(row=2,column=0)
    ac=Entry(mac15)
    ac.grid(row=2,column=2)
    Label(mac15,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(mac15)
    ad.grid(row=3,column=2)
    Label(mac15,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(mac15,text='PE JAW CRUSHER',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(mac15,text='PFW IMPACT CRUSHER',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(mac15,text='PF IMPACT CRUSHER',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(mac15,text='HST CONE CRUSHER',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(mac15,text='HPT CONE CRUSHER',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(mac15,text='CS CONE CRUSHER',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(mac15,text='PY CONE CRUSHER',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(mac15,text='VSI5X CRUSHER',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(mac15,text='VSI CRUSHER',variable=ae,value=9)
    ae8.grid(row=10,column=0)
    ae9=Radiobutton(mac15,text='VIBRATING FEEDER',variable=ae,value=10)
    ae9.grid(row=10,column=2)
    ae10=Radiobutton(mac15,text='FLOTATION MACHINE',variable=ae,value=11)
    ae10.grid(row=11,column=0)
    ae11=Radiobutton(mac15,text='HIGH-FREQUENCY SCREEN',variable=ae,value=12)
    ae11.grid(row=11,column=2)
    ae12=Radiobutton(mac15,text='HYDROCYCLONE',variable=ae,value=13)
    ae12.grid(row=12,column=0)
    ae13=Radiobutton(mac15,text='MAGNETIC SEPARATION MACHINE',variable=ae,value=14)
    ae13.grid(row=12,column=2)
    ae14=Radiobutton(mac15,text='SPIRAL CLASSIFIER',variable=ae,value=15)
    ae14.grid(row=13,column=0)
    ae15=Radiobutton(mac15,text='K SERIES MOBILE CRUSHING PLANT',variable=ae,value=16)
    ae15.grid(row=13,column=2)
    
    def insert():
        u=(ae.get())
        if u==1:
            a="PE JAW CRUSHER"
        elif u==2:
            a="PFW IMPACT CRUSHER"
        elif u==3:
            a="PF IMPACT CRUSHER"
        elif u==4:
            a="HST CONE CRUSHER"
        elif u==5:
            a="HPT CONE CRUSHER"
        elif u==6:
            a="CS CONE CRUSHER"
        elif u==7:
            a="PY CONE CRUSHER"
        elif u==8:
            a="VSI5X CRUSHER"
        elif u==9:
            a="VSI CRUSHER"
        elif u==10:
            a="VIBRATING FEEDER"
        elif u==11:
            a="FLOTATION MACHINE"
        elif u==12:
            a="HIGH-FREQUENCY SCREEN"
        elif u==13:
            a="HYDROCYCLONE"
        elif u==14:
            a="MAGNETIC SEPARATION MACHINE"
        elif u==15:
            a="SPIRAL CLASSIFIER"
        elif u==16:
            a="K SERIES MOBILE CRUSHING PLANT"    
        else:
            a='0'
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(mac15,text="fetched record is:")
        Label(mac15,text=a).grid(row=16,column=0)
    Button(mac15,text='INSERT',command=insert).grid(row=14,column=0)
    Button(mac15,text='SHOW ALL',command=showall).grid(row=14,column=2)

    mac15.mainloop()

def employees11():
    emp15=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(emp15,text='Employee details are as follows',font= "times 60 bold italic",bg='sky blue').grid(row=0,column=0)
    Label(emp15,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(emp15)
    ba.grid(row=1,column=2)
    Label(emp15,text="Enter First name").grid(row=2,column=0)
    bb=Entry(emp15)
    bb.grid(row=2,column=2)
    Label(emp15,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(emp15)
    bc.grid(row=3,column=2)
    Label(emp15,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(emp15)
    bd.grid(row=4,column=2)
    Label(emp15,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(emp15)
    be.grid(row=5,column=2)
    Label(emp15,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(emp15)
    bf.grid(row=6,column=2)
    Label(emp15,text="Select salary ").grid(row=7,column=0)
    bg=Entry(emp15)
    bg.grid(row=7,column=2)
    Label(emp15,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(emp15,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(emp15,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(emp15,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(emp15,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(emp15,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(emp15,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        Showinfo[text=="record created"]
        con.commit()
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(emp15,text="fetched record is:")
        Label(emp15,text=a).grid(row=16,column=0)
    Button(emp15,text='INSERT',command=insert).grid(row=15,column=0)
    Button(emp15,text='SHOW ALL',command=showall).grid(row=15,column=1)
    
    
def retreat():
    global ret
    ret=Toplevel()
    img = PhotoImage(file="im.gif")
    Label(ret,image=img).grid(row=5,column=0)
    Label(ret,text='Retreat Mining',font= "times 60 bold italic",bg='green').grid(row=0,column=0)
    Label(ret,text='About what do you want to know',font= "times 20",bg='orange').grid(row=1,column=0)
    ln=IntVar()
    l5=Radiobutton(ret,text="Machinery",variable=ln,value=60)
    l5.grid(row=2,column=0)
    l6=Radiobutton(ret,text="Employees",variable=ln,value=61)
    l6.grid(row=3,column=0)

    def fun1():
        if int(ln.get()) == 60:
            machinery11()
        if int(ln.get()) == 61:
            employees11()
            
        
    Button(ret,text='show11',command=fun1).grid(row=4,column=0)
    Button(ret,text='back',command=main1).grid(row=4,column=1)
    ret.mainloop()
def main1():
    ret.destroy()
    underground()    
def machinery11():
    
    mac16= Toplevel()
    cur.execute("create table if not exists mac1(manu number primary key not null,workers_needed number(4),day_manufactured date,machinery varchar(20))")
    Label(mac16,text='Machine details are as follows',font= "times 60 bold italic",bg='purple').grid(row=0,column=0)
    Label(mac16,text="Enter manufactured number").grid(row=1,column=0)
    ab=Entry(mac16)
    ab.grid(row=1,column=2)
    Label(mac16,text="Workers needed").grid(row=2,column=0)
    ac=Entry(mac16)
    ac.grid(row=2,column=2)
    Label(mac16,text="Manufactured date").grid(row=3,column=0)
    ad=Entry(mac16)
    ad.grid(row=3,column=2)
    Label(mac16,text="Select Machinery ").grid(row=5,column=0)
    ae=IntVar()
    ae0=Radiobutton(mac16,text='Articulated dump truck',variable=ae,value=1)
    ae0.grid(row=6,column=0)
    ae1=Radiobutton(mac16,text='Bucket wheel excavator',variable=ae,value=2)
    ae1.grid(row=6,column=2)
    ae2=Radiobutton(mac16,text='Cable excavator',variable=ae,value=3)
    ae2.grid(row=7,column=0)
    ae3=Radiobutton(mac16,text='Continuous miner',variable=ae,value=4)
    ae3.grid(row=7,column=2)
    ae4=Radiobutton(mac16,text='Conveyor',variable=ae,value=5)
    ae4.grid(row=8,column=0)
    ae5=Radiobutton(mac16,text='Crawler tractor',variable=ae,value=6)
    ae5.grid(row=8,column=2)
    ae6=Radiobutton(mac16,text='Dragline',variable=ae,value=7)
    ae6.grid(row=9,column=0)
    ae7=Radiobutton(mac16,text='Dredger',variable=ae,value=8)
    ae7.grid(row=9,column=2)
    ae8=Radiobutton(mac16,text='Excavator',variable=ae,value=9)
    ae8.grid(row=10,column=0)
    ae9=Radiobutton(mac16,text='Front Shovel',variable=ae,value=10)
    ae9.grid(row=10,column=2)
    ae10=Radiobutton(mac16,text='Loader backhoe',variable=ae,value=11)
    ae10.grid(row=11,column=0)
    ae11=Radiobutton(mac16,text='Motor grader',variable=ae,value=12)
    ae11.grid(row=11,column=2)
    ae12=Radiobutton(mac16,text='Rock truck',variable=ae,value=13)
    ae12.grid(row=12,column=0)
    ae13=Radiobutton(mac16,text='Water truck',variable=ae,value=14)
    ae13.grid(row=12,column=2)
    ae14=Radiobutton(mac16,text='Wheel dozer',variable=ae,value=15)
    ae14.grid(row=13,column=0)
    ae15=Radiobutton(mac16,text='Wheel loader',variable=ae,value=16)
    ae15.grid(row=13,column=2)
    
    def insert():
        u=(ae.get())
        if u==1:
            a="Articulated dump truck"
        elif u==2:
            a="Bucket wheel excavator"
        elif u==3:
            a="Cable excavator"
        elif u==4:
            a="Continuous miner"
        elif u==5:
            a="Conveyor"
        elif u==6:
            a="Crawler tractor"
        elif u==7:
            a="Dragline"
        elif u==8:
            a="Dredger"
        elif u==9:
            a="Excavator"
        elif u==10:
            a="Front Shovel"
        elif u==11:
            a="Loader backhoe"
        elif u==12:
            a="Motor grader"
        elif u==13:
            a="Rock truck"
        elif u==14:
            a="Water truck"
        elif u==15:
            a="Wheel dozer"
        elif u==16:
            a="Wheel loader"    
        else:
            a='0'
        d=[(ab.get(),ac.get(),ad.get(),a)]  
        cur.executemany("insert into mac1 values(?,?,?,?)",d)
        con.commit()
        ab.delete(0,END)
        ac.delete(0,END)
        ad.delete(0,END)
        con.commit()
        
    def showall():
        cur.execute('select * from mac1')
        a=cur.fetchall()
        Label(mac16,text="fetched record is:")
        Label(mac16,text=a).grid(row=16,column=0)
    Button(mac16,text='INSERT',command=insert).grid(row=14,column=0)
    Button(mac16,text='SHOW ALL',command=showall).grid(row=14,column=2)
    mac16.mainloop()

def employees11():
    emp16=Toplevel()
    cur.execute("create table if not exists emp1(ID number primary key not null,first_name varchar(20),last_name varchar(20),dob date,father_name varchar(20),post varchar(20),salary number(8),degree varchar(12))")
    Label(emp16,text='Employee details are as follows',font= "times 60 bold italic",bg='sky blue').grid(row=0,column=0)
    Label(emp16,text="Enter ID number").grid(row=1,column=0)
    ba=Entry(emp16)
    ba.grid(row=1,column=2)
    Label(emp16,text="Enter First name").grid(row=2,column=0)
    bb=Entry(emp16)
    bb.grid(row=2,column=2)
    Label(emp16,text="Enter Last name").grid(row=3,column=0)
    bc=Entry(emp16)
    bc.grid(row=3,column=2)
    Label(emp16,text="Enter Date Of Birth").grid(row=4,column=0)
    bd=Entry(emp16)
    bd.grid(row=4,column=2)
    Label(emp16,text="Enter Father's name").grid(row=5,column=0)
    be=Entry(emp16)
    be.grid(row=5,column=2)
    Label(emp16,text="Enter post of Employee").grid(row=6,column=0)
    bf=Entry(emp16)
    bf.grid(row=6,column=2)
    Label(emp16,text="Select salary ").grid(row=7,column=0)
    bg=Entry(emp16)
    bg.grid(row=7,column=2)
    Label(emp16,text="Select Degree ").grid(row=8,column=0)
    bh=IntVar()
    bh0=Radiobutton(emp16,text='10th',variable=bh,value=1)
    bh0.grid(row=9,column=0)
    bh1=Radiobutton(emp16,text='12th',variable=bh,value=3)
    bh1.grid(row=10,column=0)
    bh1=Radiobutton(emp16,text='Diploma',variable=bh,value=4)
    bh1.grid(row=11,column=0)
    bh1=Radiobutton(emp16,text='Graduate',variable=bh,value=5)
    bh1.grid(row=12,column=0)
    bh1=Radiobutton(emp16,text='Post Graduate',variable=bh,value=6)
    bh1.grid(row=13,column=0)
    bh1=Radiobutton(emp16,text='P.H.D.',variable=bh,value=7)
    bh1.grid(row=14,column=0)

    def insert():
        x=(bh.get())
        if x==1:
            b="10th"
        elif x==2:
            b="12th"
        elif x==3:
            b="Diploma"
        elif x==4:
            b="Graduate"
        elif x==5:
            b="Post Graduate"
        elif x==6:
            b="P.H.D."
        else:
            b='0'

        f=[(ba.get(),bb.get(),bc.get(),bd.get(),be.get(),bf.get(),bg.get(),b)]  
        cur.executemany("insert into emp1 values(?,?,?,?,?,?,?,?)",f)
        con.commit()
    def showall():
        cur.execute('select * from emp1')
        a=cur.fetchall()
        Label(emp16,text="fetched record is:")
        Label(emp16,text=a).grid(row=16,column=0)
    Button(emp16,text='INSERT',command=insert).grid(row=15,column=0)
    Button(emp16,text='SHOW ALL',command=showall).grid(row=15,column=1)
      
Button(root,text="Proceed ",command=now).grid(row=7,column=0)
mainloop()
