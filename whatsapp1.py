import pywhatkit as kit
window=Tk()
window.geometry("1050x900+260+10")
window.title("WHATSAPP BOT")
window.config(bg="black")

def sub_function():
    e1=a.get()
    e2=b.get()
    e3=c.get()
    e4=d.get()

a=StringVar()
b=StringVar()
c=IntVar()
d=IntVar()
def main_function():
    kit.sendwhatmsg(a.get(),b.get(),c.get(),d.get())


slideword=" "
count=0

def slidetext():
    global count,slideword
    text="WHATSAPP BOT MESSAGE"
    if(count>=len(text)):
        count=0
        slideword=" "
    slideword+=text[count]
    count+=1
    label.configure(text=slideword)
    label.after(1000,slidetext)


label=Label(window,text=" ",font="arial 30 bold",bg="black",fg="green")
label.place(x=10,y=10)
slidetext()

lbl1=Label(text="MOBILE NO",bg="black",fg="green",font="arial 40 bold")
lbl1.place(x=0,y=250)
entry_one=Entry(window,font="arial 25 bold",textvariable=a)
entry_one.place(x=500,y=250,width=500)


lbl2=Label(text="MESSAGE",bg="black",fg="green",font="arial 40 bold")
lbl2.place(x=0,y=350)
entry_two=Entry(window,font="arial 25 bold",textvariable=b)
entry_two.place(x=500,y=350,width=500)

lbl3=Label(text="DURATION",bg="black",fg="green",font="arial 40 bold")
lbl3.place(x=0,y=520)
entry_one=Entry(window,font="arial 25 bold",textvariable=c)
entry_one.place(x=500,y=550,width=200)

entry_four=Entry(window,font="arial 25 bold",textvariable=d)
entry_four.place(x=800,y=550,width=200)


button=Button(window,text="whatsapp",bg="green",fg="black",font="arial 30 bold",command=main_function)
button.place(x=0,y=800,width=1100)

window.mainloop()