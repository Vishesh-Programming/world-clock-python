from datetime import datetime
import pytz
from tkinter import *
import time
import math

root=Tk()
root.title("World Clock")
root.geometry("1145x600")

# Adding title for the program
worldClockLabel = Label(text="World Clock",font=("Arial" , 50))
worldClockLabel.grid(row=0 , column=0 , columnspan=4)

c_width,c_height=270,270 # canvas width height
# Creating canvas for analog clocks
c1 = Canvas(root, width=c_width, height=c_height,bg='lightgreen', relief=SUNKEN , borderwidth=1)
c2 = Canvas(root, width=c_width, height=c_height,bg='lightgreen', relief=SUNKEN , borderwidth=1)
c3 = Canvas(root, width=c_width, height=c_height,bg='lightgreen', relief=SUNKEN , borderwidth=1)
c4 = Canvas(root, width=c_width, height=c_height,bg='lightgreen', relief=SUNKEN , borderwidth=1)

# Placing all the canvas using grid method 
c1.grid(row=1,column=0,padx=5,pady=5)
c2.grid(row=1,column=1,padx=5,pady=5)
c3.grid(row=1,column=2,padx=5,pady=5)
c4.grid(row=1,column=3,padx=5,pady=5)

# creating circle for the clock
dial=c1.create_oval(10, 10, 260, 260,width=15,outline='#FF0000',fill='#FFFFFF')
dial2=c2.create_oval(10, 10, 260, 260,width=15,outline='#FF0000',fill='#FFFFFF')
dial3=c3.create_oval(10, 10, 260, 260,width=15,outline='#FF0000',fill='#FFFFFF')
dial4=c4.create_oval(10, 10, 260, 260,width=15,outline='#FF0000',fill='#FFFFFF')

# center of clock 
x,y=135,135 # center 
x1,y1,x2,y2=x,y,x,10 # second needle 

center=c1.create_oval(x-8,y-8,x+8,y+8,fill='#c0c0c0')  # creating circle at the center of clock
center2=c2.create_oval(x-8,y-8,x+8,y+8,fill='#c0c0c0')
center3=c3.create_oval(x-8,y-8,x+8,y+8,fill='#c0c0c0')
center4=c4.create_oval(x-8,y-8,x+8,y+8,fill='#c0c0c0')

r1=280 # dial lines for one minute 
r2=210 # for hour numbers  after the lines 
rs=105 # length of second needle 
rm=90 # length of minute needle
rh=80 # lenght of hour needle

in_degree = 0
home=pytz.timezone("Asia/kolkata")
local_time=datetime.now(home)
in_degree_s=int(local_time.strftime('%S')) *6 # local second 
in_degree_m=int(local_time.strftime('%M'))*6 # local minutes  
in_degree_h=int(local_time.strftime('%I')) * 30 # 12 hour format 

if(in_degree_h==360):
    in_degree_h=0 # adjusting 12 O'clock to 0 

# Initialize the second needle based on local seconds value  
in_radian = math.radians(in_degree_s) 
x2=x+rs*math.sin(in_radian)
y2=y-rs*math.cos(in_radian)
second=c1.create_line(x,y,x2,y2,fill='red',width=2) # draw the second needle

def my_second():
    '''
    handles the movement of second hand in the clock
    '''
    global in_degree_s,second
    in_radian = math.radians(in_degree_s)
    c1.delete(second) # delete the needle 
    x2=x+rs*math.sin(in_radian) # Horizontal coordinate of outer edge
    y2=y-rs*math.cos(in_radian) # vertical coordinate of outer adge
    second=c1.create_line(x,y,x2,y2,arrow='last',fill='red',width=2)
    if(in_degree_s>=360): # one rotattion is over if reached 360 
        in_degree_s=0 # start from zero angle again 
        my_minute()  # call the minute needle to move one segment. 
    in_degree_s=in_degree_s+6 # increment of one segment is 6 degree 
    c1.after(1000,my_second) # timer calling recrusive after 1 second

# Initialize Minutes needle based on local time minute value 
in_radian = math.radians(in_degree_m)
x2=x+rm*math.sin(in_radian)
y2=y-rm*math.cos(in_radian) 
minute=c1.create_line(x,y,x2,y2,width=4,fill='green')

def my_minute():
    '''
    handles the movement of minute hand
    '''
    global in_degree_m,minute
    in_degree_m=in_degree_m+6 # increment for each segment 
    in_radian = math.radians(in_degree_m) # coverting to radian 
    c1.delete(minute) # delete the previous needle
    x2=x+rm*math.sin(in_radian) # Horizontal coordinate of outer edge
    y2=y-rm*math.cos(in_radian) # vertical coordinate of outer dege
    minute=c1.create_line(x,y,x2,y2,width=4,fill='green')
    my_hour() # calling hour needle to move 
    if(in_degree_m>=360): # One rotation of 360 degree is over 
        in_degree_m=0

# initialize hour needle based on local hour 
# Adding extra hour needle  movment based on local minute value
# For 7 Hour 45 minutes, hour needle need to move beyond 7 
in_degree_h=in_degree_h+(in_degree_m*0.0833333)          
in_radian = math.radians(in_degree_h)
x2=x+rh*math.sin(in_radian)
y2=y-rh*math.cos(in_radian)
hour=c1.create_line(x,y,x2,y2,width=6,fill='#a83e32')

def my_hour():
    '''
    handles the movement of hour hand
    '''
    global in_degree_h,hour
    in_degree_h=in_degree_h+0.5 # increment in each step
    in_radian = math.radians(in_degree_h) # in radian 
    c1.delete(hour) # deleting hour needle 
    x2=x+rh*math.sin(in_radian) # Horizontal coordinate for outer edge
    y2=y-rh*math.cos(in_radian) # vertical coordinate for outer adge 
    hour=c1.create_line(x,y,x2,y2,width=6,fill='#a83e32')
    if(in_degree_h>=360):
        in_degree_h=0

my_second() # calling to start the analog clock

in_degree2 = 0
home2=pytz.timezone("America/New_York")
local_time2=datetime.now(home2)
in_degree_s2=int(local_time2.strftime('%S')) *6 # local second 
in_degree_m2=int(local_time2.strftime('%M'))*6 # local minutes  
in_degree_h2=int(local_time2.strftime('%I')) * 30 # 12 hour format 

if(in_degree_h2==360):
    in_degree_h2=0 # adjusting 12 O'clock to 0 

# Initialize the second needle based on local seconds value  
in_radian = math.radians(in_degree_s2) 
x2=x+rs*math.sin(in_radian)
y2=y-rs*math.cos(in_radian)
second2=c2.create_line(x,y,x2,y2,fill='red',width=2)# draw the second needle


def my_second2():
    '''
    handles the movement of second hand in the clock
    '''
    global in_degree_s2,second2
    in_radian = math.radians(in_degree_s2)
    c2.delete(second2) # delete the needle 
    x2=x+rs*math.sin(in_radian) # Horizontal coordinate of outer edge
    y2=y-rs*math.cos(in_radian) # vertical coordinate of outer adge
    second2=c2.create_line(x,y,x2,y2,arrow='last',fill='red',width=2)
  

    if(in_degree_s2>=360): # one rotattion is over if reached 360 
        in_degree_s2=0 # start from zero angle again 
        my_minute2()  # call the minute needle to move one segment. 
    in_degree_s2=in_degree_s2+6 # increment of one segment is 6 degree 
    c2.after(1000,my_second2) # timer calling recrusive after 1 second

# Initialize Minutes needle based on local time minute value 
in_radian = math.radians(in_degree_m2)
x2=x+rm*math.sin(in_radian)
y2=y-rm*math.cos(in_radian) 
minute2=c2.create_line(x,y,x2,y2,width=4,fill='green')

def my_minute2():
    '''
    handles the movement of minute hand
    '''
    global in_degree_m2,minute2
    in_degree_m2=in_degree_m2+6 # increment for each segment 
    in_radian = math.radians(in_degree_m2) # coverting to radian 
    c2.delete(minute2) # delete the previous needle
    x2=x+rm*math.sin(in_radian) # Horizontal coordinate of outer edge
    y2=y-rm*math.cos(in_radian) # vertical coordinate of outer dege
    minute2=c2.create_line(x,y,x2,y2,width=4,fill='green')
    my_hour2() # calling hour needle to move 
    if(in_degree_m2>=360): # One rotation of 360 degree is over 
        in_degree_m2=0

# initialize hour needle based on local hour 
# Adding extra hour needle  movment based on local minute value
# For 7 Hour 45 minutes, hour needle need to move beyond 7 
in_degree_h2=in_degree_h2+(in_degree_m2*0.0833333)          
in_radian = math.radians(in_degree_h2)
x2=x+rh*math.sin(in_radian)
y2=y-rh*math.cos(in_radian)
hour2=c2.create_line(x,y,x2,y2,width=6,fill='#a83e32')

def my_hour2():
    '''
    handles the movement of hour hand
    '''
    global in_degree_h2,hour2
    in_degree_h2=in_degree_h2+0.5 # increment in each step
    in_radian = math.radians(in_degree_h2) # in radian 
    c2.delete(hour2) # deleting hour needle 
    x2=x+rh*math.sin(in_radian) # Horizontal coordinate for outer edge
    y2=y-rh*math.cos(in_radian) # vertical coordinate for outer adge 
    hour2=c2.create_line(x,y,x2,y2,width=6,fill='#a83e32')
    if(in_degree_h2>=360):
        in_degree_h2=0

my_second2() # calling to start the analog clock

in_degree3 = 0
home3=pytz.timezone("europe/london")
local_time3=datetime.now(home3)
in_degree_s3=int(local_time3.strftime('%S')) *6 # local second 
in_degree_m3=int(local_time3.strftime('%M'))*6 # local minutes  
in_degree_h3=int(local_time3.strftime('%I')) * 30 # 12 hour format 

if(in_degree_h3==360):
    in_degree_h3=0 # adjusting 12 O'clock to 0 

# Initialize the second needle based on local seconds value  
in_radian = math.radians(in_degree_s3) 
x2=x+rs*math.sin(in_radian)
y2=y-rs*math.cos(in_radian)
second3=c3.create_line(x,y,x2,y2,fill='red',width=2)# draw the second needle


def my_second3():
    '''
    handles the movement of second hand in the clock
    '''
    global in_degree_s3,second3
    in_radian = math.radians(in_degree_s3)
    c3.delete(second3) # delete the needle 
    x2=x+rs*math.sin(in_radian) # Horizontal coordinate of outer edge
    y2=y-rs*math.cos(in_radian) # vertical coordinate of outer adge
    second3=c3.create_line(x,y,x2,y2,arrow='last',fill='red',width=2)
  

    if(in_degree_s3>=360): # one rotattion is over if reached 360 
        in_degree_s3=0 # start from zero angle again 
        my_minute3()  # call the minute needle to move one segment. 
    in_degree_s3=in_degree_s3+6 # increment of one segment is 6 degree 
    c3.after(1000,my_second3) # timer calling recrusive after 1 second

# Initialize Minutes needle based on local time minute value 
in_radian = math.radians(in_degree_m3)
x2=x+rm*math.sin(in_radian)
y2=y-rm*math.cos(in_radian) 
minute3=c3.create_line(x,y,x2,y2,width=4,fill='green')

def my_minute3():
    '''
    handles the movement of minute hand
    '''
    global in_degree_m3,minute3
    in_degree_m3=in_degree_m3+6 # increment for each segment 
    in_radian = math.radians(in_degree_m3) # coverting to radian 
    c3.delete(minute3) # delete the previous needle
    x2=x+rm*math.sin(in_radian) # Horizontal coordinate of outer edge
    y2=y-rm*math.cos(in_radian) # vertical coordinate of outer dege
    minute3=c3.create_line(x,y,x2,y2,width=4,fill='green')
    my_hour3() # calling hour needle to move 
    if(in_degree_m3>=360): # One rotation of 360 degree is over 
        in_degree_m3=0

# initialize hour needle based on local hour 
# Adding extra hour needle  movment based on local minute value
# For 7 Hour 45 minutes, hour needle need to move beyond 7 
in_degree_h3=in_degree_h3+(in_degree_m3*0.0833333)          
in_radian = math.radians(in_degree_h3)
x2=x+rh*math.sin(in_radian)
y2=y-rh*math.cos(in_radian)
hour3=c3.create_line(x,y,x2,y2,width=6,fill='#a83e32')

def my_hour3():
    '''
    handles the movement of hour hand
    '''
    global in_degree_h3,hour3
    in_degree_h3=in_degree_h3+0.5 # increment in each step
    in_radian = math.radians(in_degree_h3) # in radian 
    c3.delete(hour3) # deleting hour needle 
    x2=x+rh*math.sin(in_radian) # Horizontal coordinate for outer edge
    y2=y-rh*math.cos(in_radian) # vertical coordinate for outer adge 
    hour3=c3.create_line(x,y,x2,y2,width=6,fill='#a83e32')
    if(in_degree_h3>=360):
        in_degree_h3=0

my_second3() # calling to start the analog clock

in_degree4 = 0
home4=pytz.timezone("Asia/Tokyo")
local_time4=datetime.now(home4)
in_degree_s4=int(local_time4.strftime('%S')) *6 # local second 
in_degree_m4=int(local_time4.strftime('%M'))*6 # local minutes  
in_degree_h4=int(local_time4.strftime('%I')) * 30 # 12 hour format 

if(in_degree_h4==360):
    in_degree_h4=0 # adjusting 12 O'clock to 0 

# Initialize the second needle based on local seconds value  
in_radian = math.radians(in_degree_s4) 
x2=x+rs*math.sin(in_radian)
y2=y-rs*math.cos(in_radian)
second4=c4.create_line(x,y,x2,y2,fill='red',width=2)# draw the second needle


def my_second4():
    '''
    handles the movement of second hand in the clock
    '''
    global in_degree_s4,second4
    in_radian = math.radians(in_degree_s4)
    c4.delete(second4) # delete the needle 
    x2=x+rs*math.sin(in_radian) # Horizontal coordinate of outer edge
    y2=y-rs*math.cos(in_radian) # vertical coordinate of outer adge
    second4=c4.create_line(x,y,x2,y2,arrow='last',fill='red',width=2)
  

    if(in_degree_s4>=360): # one rotattion is over if reached 360 
        in_degree_s4=0 # start from zero angle again 
        my_minute4()  # call the minute needle to move one segment. 
    in_degree_s4=in_degree_s4+6 # increment of one segment is 6 degree 
    c4.after(1000,my_second4) # timer calling recrusive after 1 second

# Initialize Minutes needle based on local time minute value 
in_radian = math.radians(in_degree_m4)
x2=x+rm*math.sin(in_radian)
y2=y-rm*math.cos(in_radian) 
minute4=c4.create_line(x,y,x2,y2,width=4,fill='green')

def my_minute4():
    '''
    handles the movement of minute hand
    '''
    global in_degree_m4,minute4
    in_degree_m4=in_degree_m4+6 # increment for each segment 
    in_radian = math.radians(in_degree_m4) # coverting to radian 
    c4.delete(minute4) # delete the previous needle
    x2=x+rm*math.sin(in_radian) # Horizontal coordinate of outer edge
    y2=y-rm*math.cos(in_radian) # vertical coordinate of outer dege
    minute4=c4.create_line(x,y,x2,y2,width=4,fill='green')
    my_hour4() # calling hour needle to move 
    if(in_degree_m4>=360): # One rotation of 360 degree is over 
        in_degree_m4=0

# initialize hour needle based on local hour 
# Adding extra hour needle  movment based on local minute value
# For 7 Hour 45 minutes, hour needle need to move beyond 7 
in_degree_h4=in_degree_h4+(in_degree_m4*0.0833333)          
in_radian = math.radians(in_degree_h4)
x2=x+rh*math.sin(in_radian)
y2=y-rh*math.cos(in_radian)
hour4=c4.create_line(x,y,x2,y2,width=6,fill='#a83e32')

def my_hour4():
    '''
    handles the movement of hour hand
    '''
    global in_degree_h4,hour4
    in_degree_h4=in_degree_h4+0.5 # increment in each step
    in_radian = math.radians(in_degree_h4) # in radian 
    c4.delete(hour4) # deleting hour needle 
    x2=x+rh*math.sin(in_radian) # Horizontal coordinate for outer edge
    y2=y-rh*math.cos(in_radian) # vertical coordinate for outer adge 
    hour4=c4.create_line(x,y,x2,y2,width=6,fill='#a83e32')
    if(in_degree_h4>=360):
        in_degree_h4=0

my_second4() # calling to start the analog clock

def time1():
    '''
    handles the current time of Asia/Kolkata
    '''
    home=pytz.timezone("Asia/kolkata")
    local_time=datetime.now(home)
    current_time=local_time.strftime("%a %H:%M:%S")
    clock.config(text=current_time)
    name.config(text="India")
    clock.after(200,time2)

    
def time2():
    '''
    handles the current time of America/New_York
    '''
    home2=pytz.timezone("America/New_York")
    local_time2=datetime.now(home2)
    current_time2=local_time2.strftime("%a %H:%M:%S")
    clock2.config(text=current_time2)
    name2.config(text="New York")
    clock2.after(200,time1)

def time3():
    '''
    handles the current time of europe/london
    '''
    home3=pytz.timezone("europe/london")
    local_time3=datetime.now(home3)
    current_time3=local_time3.strftime("%a %H:%M:%S")
    clock3.config(text=current_time3)
    name3.config(text="London")
    clock3.after(200,time3)

def time4():
    '''
    handles the current time of Asia/Tokyo
    '''
    home4=pytz.timezone("Asia/Tokyo")
    local_time4=datetime.now(home4)
    current_time4=local_time4.strftime("%a %H:%M:%S")
    clock4.config(text=current_time4)
    name4.config(text="Tokyo")
    clock4.after(200,time4)
  
#First Time Zone
f=Frame(root,bd=5)
f.place(x=10,y=418,width=220,height=150)
name=Label(f,font=("Helvetica",25,"bold"))
name.place(x=50,y=10)
logo=PhotoImage(file="in.png")
image_label=Label(root,image=logo)
image_label.place(x=20,y=450)
clock=Label(f,font=("Helvetica",20))
clock.place(x=5,y=80)

#Second Time Zone
f2=Frame(root,bd=5)
f2.place(x=300,y=418,width=220,height=150)
name2=Label(f2,font=("Helvetica",25,"bold"))
name2.place(x=30,y=10)
logo2=PhotoImage(file="us.png")
image_label2=Label(root,image=logo2)
image_label2.place(x=290,y=450)
clock2=Label(f2,font=("Helvetica",20))
clock2.place(x=5,y=80)

#Third Time Zone
f3=Frame(root,bd=5)
f3.place(x=600,y=418,width=220,height=150)
name3=Label(f3,font=("Helvetica",25,"bold"))
name3.place(x=50,y=10)
logo3=PhotoImage(file="gb.png")
image_label3=Label(root,image=logo3)
image_label3.place(x=600,y=450)
clock3=Label(f3,font=("Helvetica",20))
clock3.place(x=5,y=80)

#Fourth Time Zone
f4=Frame(root,bd=5)
f4.place(x=900,y=418,width=220,height=150)
name4=Label(f4,font=("Helvetica",25,"bold"))
name4.place(x=50,y=10)
logo4=PhotoImage(file="jp.png")
image_label4=Label(root,image=logo4)
image_label4.place(x=900,y=450)
clock4=Label(f4,font=("Helvetica",20))
clock4.place(x=5,y=80)

# calling the function to initiate the clocks
time1()
time2()
time3()
time4()
    
root.mainloop()