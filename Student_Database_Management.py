from tkinter import *
from tkinter import messagebox
import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import scrolledtext
from dbhandler import *
import socket
import requests
import os


  
win = Tk()
win.geometry("300x300+250+250")
win.title("---Splash---")
canvas = Canvas(win, width = 300, height = 300,bg="green")
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("clouds.gif"))  
canvas.create_image(15, 15, anchor=NW, image=img)
import socket
import requests
try:
    socket.create_connection(("www.google.com",80))
    
    res=requests.get("https://ipinfo.io")

    data=res.json()  #javascript object notation
    print(data)
    city=data['city']
    
    
    a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
    a2="&q="+city
    a3="&appid=&&&&&&"
    addr=a1+a2+a3
    label1=Label(win,text=city,bg="Red",fg='black',font=("Times", 20, "bold"))
    label1.place(x=35,y=250)
    res=requests.get(addr)
    data=res.json()
    
    main=data['main']
    
    temp=main['temp']
    
    label2=Label(win,text=temp,bg="Red",fg='black',font=("Times", 20, "bold"))
    label2.place(x=170,y=250)
except OSError as e:
    messagebox.showerror("Unable to Connect")
    
    


win.after(6000,win.destroy)
win.mainloop()


#spalshcodeend



root=Tk()
root.title("S.M.S")
root.geometry("300x300+250+250")

root.configure(background="blue")

    


##########################-------------VIEW SECTION--------------##################################################################################

viewFrame=Toplevel(root)
viewFrame.title("View Student")
viewFrame.geometry("300x300+250+250")
viewFrame.withdraw()
viewFrame.configure(background="blue")

def f6():
    root.deiconify()
    viewFrame.withdraw()
viewFrame.protocol("WM_DELETE_WINDOW",f6)


st=scrolledtext.ScrolledText(viewFrame,width=20,height=10)
def f4():
    viewFrame.withdraw()
    st.delete('1.0',END)
    root.deiconify()

btnViewBack=Button(viewFrame,text='Back',font=('arial',10,'bold'),bg='ivory4',width=20,command=f4)
st.pack(pady=10)
btnViewBack.pack(pady=10)



def f3():
    root.withdraw()
    viewFrame.deiconify()
    data = viewStudent()
    st.insert(INSERT,data)


btnView=Button(root,text='View',font=("arial",10,"bold"),bg='ivory4',width=10,command=f3)

def f85():
    ans=messagebox.askyesno("Exit","Are you sure you want to exit?")
    if ans:
        viewFrame.destroy()
viewFrame.protocol("WM_DELETE_WINDOW",f85)






########################-------------ADD SECTION--------------#######################################################################



addFrame=Toplevel(root)
addFrame.title("Add Student")
addFrame.geometry("300x300+250+250")
addFrame.withdraw()
addFrame.configure(background="blue")





def f7():
    root.deiconify()
    addFrame.withdraw()
addFrame.protocol("WM_DELETE_WINDOW",f7)





lblAddRno=Label(addFrame,bg='blue',text="Rno",font=('arial',10,'bold'),width=20)
entAddRno=Entry(addFrame,bd=2,font=('arial',10,'bold'),width=20)
lblAddName=Label(addFrame,bg='blue',text="Name",font=('arial',10,'bold'),width=20)
entAddName=Entry(addFrame,bd=4,font=('arial',10,'bold'),width=20)





def f5():
    try:
        
        rno=int(entAddRno.get())    
        name=entAddName.get()
        if (len(name)==0 or not name.isalpha()):
            messagebox.showerror("Failure","Invalid name")
            return
        if (rno < 0):
            messagebox.showerror("Failure","Enter positive number")
            return
        addStudent(rno,name)
        entAddRno.delete(0,END)
        entAddName.delete(0,END)
        entAddRno.focus()
    except TypeError:
        
        messagebox.showerror("Failure","TypeError")
    except ValueError:
        
        messagebox.showerror("Failure","Only Integers allowed in Rno.")
    except IndexError:
        messagebox.showerror("Failure","Only Characters allowed" )





btnAddSave=Button(addFrame,text='Save',bg='ivory4',font=("arial",10,'bold'),width=20,command=f5)



def f2():
    addFrame.withdraw()
    root.deiconify()

btnAddBack=Button(addFrame,text="Back",bg='ivory4',font=("arial",10,'bold'),width=20,command=f2)




lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)





def f1():
    root.withdraw()
    addFrame.deiconify()

btnAdd=Button(root,text="Add",bg='ivory4',font=("arial",10,'bold'),width=10,command=f1)



def f83():
    ans=messagebox.askyesno("Exit","Are you sure you want to exit?")
    if ans:
        addFrame.destroy()
addFrame.protocol("WM_DELETE_WINDOW",f83)



########################------------UPDATE SECTION-----------------##############################################################




updateFrame=Toplevel(root)
updateFrame.title("Update Student")
updateFrame.geometry("300x300+250+250")
updateFrame.withdraw()
updateFrame.configure(background="blue")





def fu1():
    root.deiconify()
    updateFrame.withdraw()
updateFrame.protocol("WM_DELETE_WINDOW",fu1)





lblupRno=Label(updateFrame,bg='blue',text="Rno",font=('arial',10,'bold'),width=20)
entupRno=Entry(updateFrame,bd=2,font=('arial',10,'bold'),width=20)
lblupName=Label(updateFrame,bg='blue',text="Name",font=('arial',10,'bold'),width=20)
entupName=Entry(updateFrame,bd=4,font=('arial',10,'bold'),width=20)





def fu2():
    try:
        rno=entupRno.get()
        name=entupName.get()
        if (len(name)==0 or not name.isalpha()):
            messagebox.showerror("Failure","Invalid name")
            return
        if rno<0:
            messagebox.showerror("Failure","Enter positive number")
            return
            
        updateStudent(int(rno),name)
        entupRno.delete(0,END)
        entupName.delete(0,END)
        entupRno.focus()
    except TypeError:
        
        messagebox.showerror("Failure","TypeError")
    except ValueError:
        
        messagebox.showerror("Failure","Only Integers allowed in Rno.")
    except IndexError:
        messagebox.showerror("Failure","Only Characters allowed" )







btnupSave=Button(updateFrame,bg='ivory4',text='Save',font=("arial",10,'bold'),width=20,command=fu2)



def fu3():
    updateFrame.withdraw()
    root.deiconify()

btnupBack=Button(updateFrame,bg='ivory4',text="Back",font=("arial",10,'bold'),width=20,command=fu3)




lblupRno.pack(pady=10)
entupRno.pack(pady=10)
lblupName.pack(pady=10)
entupName.pack(pady=10)
btnupSave.pack(pady=10)
btnupBack.pack(pady=10)





def fu4():
    root.withdraw()
    updateFrame.deiconify()

btnUpdate=Button(root,bg='ivory4',text="Update",font=("arial",10,'bold'),width=10,command=fu4)






def f82():
    ans=messagebox.askyesno("Exit","Are you sure you want to exit?")
    if ans:
        updateFrame.destroy()
updateFrame.protocol("WM_DELETE_WINDOW",f82)











######################--------------DELETE SECTION-----------------###################################





delFrame=Toplevel(root)
delFrame.title("Delete Student")
delFrame.geometry("300x300+250+250")
delFrame.withdraw()
delFrame.configure(background="blue")





def fd1():
    root.deiconify()
    delFrame.withdraw()
delFrame.protocol("WM_DELETE_WINDOW",fd1)





lbldelRno=Label(delFrame,bg='blue',text="Rno",font=('arial',10,'bold'),width=20)
entdelRno=Entry(delFrame,bd=2,font=('arial',10,'bold'),width=20)






def fd2():
    try:
        rno=int(entdelRno.get())
        delStudent(rno)
        entdelRno.delete(0,END)
        entdelRno.focus()
    except AttributeError:
        messagebox.showerror("Failure","Enter digits only")
    except ValueError:
        messagebox.showerror("Failure","Enter digits only")





btndelSave=Button(delFrame,bg='ivory4',text='Delete',font=("arial",10,'bold'),width=20,command=fd2)



def fd3():
    delFrame.withdraw()
    root.deiconify()

btndelBack=Button(delFrame,bg='ivory4',text="Back",font=("arial",10,'bold'),width=20,command=fd3)




lbldelRno.pack(pady=10)
entdelRno.pack(pady=10)
btndelSave.pack(pady=10)
btndelBack.pack(pady=10)





def fd4():
    root.withdraw()
    delFrame.deiconify()
    
btnDelete=Button(root,bg='ivory4',text='Delete',font=("arial",10,"bold"),width=10,command=fd4)




def f81():
    ans=messagebox.askyesno("Exit","Are you sure you want to exit?")
    if ans:
        delFrame.destroy()
delFrame.protocol("WM_DELETE_WINDOW",f81)







#####################-------------Main Button Pack Section----------##########################################
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)    
btnDelete.pack(pady=10)


def f8():
    ans=messagebox.askyesno("Exit","Are you sure you want to exit?")
    if ans:
        root.destroy()
root.protocol("WM_DELETE_WINDOW",f8)




root.mainloop()

    

##########splash screen
