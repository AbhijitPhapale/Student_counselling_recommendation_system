from tkinter import*
from tkinter import messagebox
import tkinter.messagebox
import cv2
import PIL.Image, PIL.ImageTk
import sqlite3
import random

conn = sqlite3.connect('database.sql')

conn.execute('''create table IF NOT EXISTS students
            (FirstName varchar(50),
            LastName varchar(50),
            RollNo int(12) primary key not null,
            BoardMarks float(4),
            Percentage varchar(3),
            Email varchar(100),
            Mobile int(12),
            cc1 varchar(50),
            bc1 varchar(50),
            cc2 varchar(50),
            bc2 varchar(50),
            cc3 varchar(50),
            bc3 varchar(50),
            cc4 varchar(50),
            bc4 varchar(50),
            cc5 varchar(50),
            bc5 varchar(50),
            cc6 varchar(50),
            bc6 varchar(50),
            alloted varchar(50),
            alloted_branch varchar(50));''')

advtech = {'IIT_t1':['IIT Bombay','IIT Kharagpur','IIT Delhi','IIT Roorkee','IIT Madras','IIT Guwahati','IIT Kanpur'],
           'IIT_t2':['IIT Pallakad','IIT Patna','IIT Jammu','IIT Bhuwaneshhwar','IIT Gandhinagar','IIT-ISM Dhanbad','IIT-BHU Varanasi'],
           'range':['IISC Banglore','IIRS','NISER','RGIPT','IIEST','IISER Pune','IISER Mohali','IISER Kolkata'],
           'NIT':['NIT Tiruchi','NIT Patna','NIT Sikkim','NIT Surathkal','NIT Delhi','NIT Assam','IIFT Ranchi','IIIT Delhi','DTU Delhi','IIIT Bhagalpur'],
           'private':['LPU Jalandhar','SRM chennai','VIT Vellore','BITS Pilani','BIT Mesra','Parul university']
        }

admed = {'AIIMS':['AIIMS Delhi','AIIMS Patna','AIIMS Rishikesh','AIIMS GOA','AIIMS GAYA'],
         'NEET':['Maulana Abdul kalam Medical College','PMCH Patna']}
branches ={'tech':['Civil Engineering','Computer Science & Engineering','Electronice & Communication Engineering','Mechanical Engineering','Electrical Engineering'],
           'med':['Cardiology','Neurology','Oncology','Genetics','Agriculture']
    }

def save_info():
    
    FirstName = fst.get()
    LastName = lst.get()     
    RollNo = int(rollno.get())
    Email = mail.get()
    Mobile = int(mob.get())
    boardmarks = int(marks.get())
    Percentage = int(percent.get())
    #Tech
    cc1 = var1.get()
    bc1 = var4.get()
    cc2 = var2.get()
    bc2 = var5.get()
    cc3 = var3.get()
    bc3 = var6.get()
    #Med
    cc4 = var7.get()
    bc4 = var10.get()
    cc5 = var8.get()
    bc5 = var11.get()
    cc6 = var9.get()
    bc6 = var12.get()

    lst1 =[cc1,cc2,cc3,cc4,cc5,cc6]
    lst2 = [bc1,bc2,bc3]
    lst3 = [bc4,bc5,bc6]
    allocated = random.choice(lst1)
    if allocated in [cc1,cc2,cc3]:
    	allocated_branch = random.choice(lst2)
    else:
    	
     allocated_branch = random.choice(lst3)
    
    
    messagebox.showinfo(title = "Summary",message="\tFirst Name: {0}\n\tLast Name : {1}\n\tRoll NO. : {2}\n\tMarks : {3}\n\tEmail : {4}\n\tMobile No. : {5}\n\tCollege Choices : {6},{7},{8},{9},{10},{11}\n\tDesired Branches : {12},{13},{14},{15},{16},{17}".format(FirstName,LastName,RollNo,boardmarks,Email,Mobile,cc1,cc2,cc3,cc4,cc5,cc6,bc1,bc2,bc3,bc4,bc5,bc6))
    messagebox.showinfo(title = "Expected Allotment Result",message = "Dear {0},\nBased on your choices we have alloted\nyou college,below..\n\tAlloted Collage = {1}\n\tAlloted Branch = {2}".format(FirstName,allocated,allocated_branch))
    messagebox.showinfo(title='You are Registered Successfully!' ,message ='\tRegistration Completed!\n\tYou Have Been Registered Successfully!\n\tFurther Information Regarding seat \n\tallotment will be sent to you on\n\t your Registered Mobile No.\n\tThank You..')

    conn.execute("insert into students(FirstName,LastName,RollNo, Boardmarks ,Percentage, Email, Mobile,  cc1, bc1, cc2, bc2,cc3,bc3,cc4,bc4,cc5,bc5,cc6,bc6,alloted,alloted_branch) \
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?)",(FirstName,LastName,RollNo, boardmarks, Percentage, Email,Mobile, cc1, bc1, cc2, bc2, cc3, bc3,cc4,bc4,cc5,bc5,cc6,bc6,allocated,allocated_branch))

    conn.commit()

    screen.destroy()

#initialising GUI

screen = Tk()
screen.geometry("1300x720",)
screen.title("ONLINE COLLEGE COUNSELLING PORTAL - 2022")
screen.configure(background='skyblue')

heading = Label(text="ONLINE COUNSELLING FORM", bg = "yellow", fg = "Red", width = "500", height = "2",font="Sans-serif")
heading.pack()


#inserting Image File(JPG)
cv_img = cv2.imread("Counselling.jpg")
cv_img = cv2.cvtColor(cv2.imread("Counselling.jpg"), cv2.COLOR_BGR2RGB)
height, width, no_channels = cv_img.shape
canvas = tkinter.Canvas(screen, width = width, height = height)
canvas.place(x=1100, y=50)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

cv_img = cv2.blur(cv_img, (2, 2))
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)


firstname_text = Label(text = "First Name: ",font='serif',fg='purple',bg='yellow')
lastname_text = Label(text = "Last Name: ",font='serif',fg='purple',bg='yellow')
email_text = Label(text = "Email: ",font='serif',fg='red',bg='yellow')
phoneno_text = Label(text = "Mobile No.: ",font='serif',fg='blue',bg='yellow')
rollno = Label(text = "Board Roll No.: ",font='serif',fg='red',bg='yellow')
Marks= Label(text="Enter Marks(in Xiith Board Exam): ",font='serif',fg='red',bg='yellow')
Percentage=Label(text="Percentage in Board Exam: ",font='serif',fg='red',bg='yellow')

College = Label(text="For Engineering Colleges(Left side screen): ",font='Sans-serif',fg='Blue',bg='yellow')
#Tech
col11 = Label(text = "College Choice 1: ",font="Gotham")
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()

col1 = OptionMenu(screen,var1, advtech['IIT_t1'][0], advtech['IIT_t1'][1], advtech['IIT_t1'][2], advtech['IIT_t1'][3], advtech['IIT_t1'][4], advtech['IIT_t1'][5], advtech['IIT_t1'][6],advtech['IIT_t2'][0],advtech['IIT_t2'][1],advtech['IIT_t2'][2],advtech['IIT_t2'][3],advtech['IIT_t2'][4],advtech['IIT_t2'][5],advtech['IIT_t2'][6],advtech['NIT'][0],advtech['NIT'][1],advtech['NIT'][2],advtech['NIT'][3],advtech['NIT'][4],advtech['NIT'][5],advtech['NIT'][6],advtech['NIT'][7],advtech['NIT'][8],advtech['NIT'][9],advtech['range'][0],advtech['range'][1],advtech['range'][2],advtech['range'][3],advtech['range'][4],advtech['range'][5],advtech['range'][6],advtech['range'][7],advtech['private'][0],advtech['private'][1],advtech['private'][2],advtech['private'][3],advtech['private'][4],advtech['private'][5])
col1.configure(font=("Arial",8),width=30)
col1.place(x=80, y=400)


Branch = Label(text= "Branch :")
bch1 = OptionMenu(screen,var4, branches['tech'][0],branches['tech'][ 1],branches['tech'][2],branches['tech'][3],branches['tech'][4])
bch1.configure(font=("Arial",8),width=30)
bch1.place(x=350, y=400)

col22 = Label(text = "College Choice 2: ",font="Gotham")
col2 = OptionMenu(screen,var2,advtech['IIT_t1'][0], advtech['IIT_t1'][1], advtech['IIT_t1'][2], advtech['IIT_t1'][3], advtech['IIT_t1'][4], advtech['IIT_t1'][5], advtech['IIT_t1'][6],advtech['IIT_t2'][0],advtech['IIT_t2'][1],advtech['IIT_t2'][2],advtech['IIT_t2'][3],advtech['IIT_t2'][4],advtech['IIT_t2'][5],advtech['IIT_t2'][6],advtech['NIT'][0],advtech['NIT'][1],advtech['NIT'][2],advtech['NIT'][3],advtech['NIT'][4],advtech['NIT'][5],advtech['NIT'][6],advtech['NIT'][7],advtech['NIT'][8],advtech['NIT'][9],advtech['range'][0],advtech['range'][1],advtech['range'][2],advtech['range'][3],advtech['range'][4],advtech['range'][5],advtech['range'][6],advtech['range'][7],advtech['private'][0],advtech['private'][1],advtech['private'][2],advtech['private'][3],advtech['private'][4],advtech['private'][5])
col2.configure(font=("Arial",8),width=30)
col2.place(x=80, y=490)

bch22 = Label(text= "Branch :")
bch2 = OptionMenu(screen,var5, branches['tech'][0],branches['tech'][ 1],branches['tech'][2],branches['tech'][3],branches['tech'][4])
bch2.configure(font=("Arial",8),width=30)
bch2.place(x=350, y=490)
col33 = Label(text = "College Choice 3: ",font="Gotham")
col33.place(x = 100)
col3 = OptionMenu(screen,var3,advtech['IIT_t1'][0], advtech['IIT_t1'][1], advtech['IIT_t1'][2], advtech['IIT_t1'][3], advtech['IIT_t1'][4], advtech['IIT_t1'][5], advtech['IIT_t1'][6],advtech['IIT_t2'][0],advtech['IIT_t2'][1],advtech['IIT_t2'][2],advtech['IIT_t2'][3],advtech['IIT_t2'][4],advtech['IIT_t2'][5],advtech['IIT_t2'][6],advtech['NIT'][0],advtech['NIT'][1],advtech['NIT'][2],advtech['NIT'][3],advtech['NIT'][4],advtech['NIT'][5],advtech['NIT'][6],advtech['NIT'][7],advtech['NIT'][8],advtech['NIT'][9],advtech['range'][0],advtech['range'][1],advtech['range'][2],advtech['range'][3],advtech['range'][4],advtech['range'][5],advtech['range'][6],advtech['range'][7],advtech['private'][0],advtech['private'][1],advtech['private'][2],advtech['private'][3],advtech['private'][4],advtech['private'][5])
col3.configure(font=("Arial",8),width=30)
col3.place(x=80, y=580)

bch33 = Label(text= "Branch :")
bch3 = OptionMenu(screen,var6,branches['tech'][0],branches['tech'][ 1],branches['tech'][2],branches['tech'][3],branches['tech'][4])
bch3.configure(font=("Arial",8),width=30)
bch3.place(x=350, y=580)

#Med
College2 = Label(text="For Medical Colleges(Right side screen): ",font='Sans-serif',fg='Blue',bg='yellow')
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = StringVar()
var11 = StringVar()
var12 = StringVar()
col44 = Label(text = "College Choice 5: ",font="Gotham")
col44.place(x = 700,y=360)
col4 = OptionMenu(screen,var7, admed['AIIMS'][0],admed['AIIMS'][1],admed['AIIMS'][2],admed['AIIMS'][3],admed['AIIMS'][4],admed['NEET'][0],admed['NEET'][1])
col4.configure(font=("Arial",8),width=30)
col4.place(x=700, y=400)


Branch = Label(text= "Branch :")
bch4 = OptionMenu(screen,var8,branches['med'][0],branches['med'][1],branches['med'][2],branches['med'][3],branches['med'][4])
bch4.configure(font=("Arial",8),width=30)
bch4.place(x=970, y=400)

col55 = Label(text = "College Choice 6: ",font="Gotham")
col55.place(x = 700,y = 450)
col5 = OptionMenu(screen,var9,admed['AIIMS'][0],admed['AIIMS'][1],admed['AIIMS'][2],admed['AIIMS'][3],admed['AIIMS'][4],admed['NEET'][0],admed['NEET'][1])
col5.configure(font=("Arial",8),width=30)
col5.place(x=700, y=500)

bch55 = Label(text= "Branch :")
bch5 = OptionMenu(screen,var10, branches['med'][0],branches['med'][1],branches['med'][2],branches['med'][3],branches['med'][4])
bch5.configure(font=("Arial",8),width=30)
bch5.place(x=970, y=500)

col66 = Label(text = "College Choice 7: ",font="Gotham")
col66.place(x = 700,y=540)
col6 = OptionMenu(screen,var11,admed['AIIMS'][0],admed['AIIMS'][1],admed['AIIMS'][2],admed['AIIMS'][3],admed['AIIMS'][4],admed['NEET'][0],admed['NEET'][1])
col6.configure(font=("Arial",8),width=30)
col6.place(x=700, y=580)

bch66 = Label(text= "Branch :")
bch6 = OptionMenu(screen,var12,branches['med'][0],branches['med'][1],branches['med'][2],branches['med'][3],branches['med'][4])
bch6.configure(font=("Arial",8),width=30)
bch6.place(x=970, y=580)


####
firstname_text.place(x = 230, y = 70)
lastname_text.place(x = 600, y = 70)
rollno.place(x = 230, y = 140)
Marks.place(x = 230, y = 200)
Percentage.place(x = 550, y = 200)
email_text.place(x = 380, y = 250)
phoneno_text.place(x = 600, y = 140)
College.place(x= 150,y=300)
College2.place(x = 820, y = 300)
col11.place(x = 80, y = 360)
col22.place(x = 80, y = 450)
col33.place(x = 80, y = 540)


fst = StringVar()
lst = StringVar()
rollno = IntVar()
marks = IntVar()
percent = IntVar()
mail = StringVar()
mob = IntVar()
firstname_entry = Entry(textvariable = fst, width="30",fg='red',bg='lightpink')
lastname_entry = Entry(textvariable = lst, width="30",fg='red',bg='lightpink')
rollno_entry = Entry(textvariable = rollno, width="30",fg='red',bg='lightpink')
Marks = Entry(textvariable = marks, width="5",fg='blue',bg='lightpink')
percent = Entry(textvariable = percent, width="10",fg='blue',bg='lightpink')
email_entry = Entry(textvariable = mail, width="50",fg='blue',bg='yellow')
phoneno_entry = Entry(textvariable = mob, width="30",fg='red',bg='lightpink')


firstname_entry.place(x=330, y=70)
lastname_entry.place(x=700, y=70)
rollno_entry.place(x=350, y=140)
email_entry.place(x=500, y=250)
phoneno_entry.place(x=700, y=140)
Marks.place(x=500, y=200)
percent.place(x=780, y=200)

register = Button(text = "Submit For Counsellong", width = "40", height = "2", command= save_info, bg = "blue",fg='yellow')
register.place(x=500, y = 620)


screen.mainloop()