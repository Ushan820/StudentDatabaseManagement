import cx_Oracle
from tkinter import messagebox

def addStudent(rno,name):
    con=None
    cursor=None
    try:
        con=cx_Oracle.connect("system/abc123")
        cursor=con.cursor()
        '''sql="create table Student(rno int primary key,name varchar(10))"
        cursor.execute(sql)'''
        
        sql="Insert into Student Values ('%d','%s')"
        args=(rno,name)
        
        cursor.execute(sql % args)
        con.commit()
        
        print(cursor.rowcount,"row inserted")
        msg=str(cursor.rowcount)+"rows inserted"
        messagebox.showinfo("Success",msg)
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("Issue ",e)
        messagebox.showerror("Failure",str(e))
    except TypeError:
        con.rollback()
        messagebox.showerror("Failure","TypeError")
    except ValueError:
        con.rollback()
        messagebox.showerror("Failure","Only Integers allowed")
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()










def viewStudent():
    con=None
    cursor=None
    try:
        con=cx_Oracle.connect("system/abc123")
        cursor=con.cursor()
        sql="Select * from Student"
        
        cursor.execute(sql)
        
        data=cursor.fetchall()
        info=''
        for i in data:
            rno=i[0]
            name=i[1]
            info=info+"Rno. "+str(rno)+"Name "+name+"\n"
    except cx_Oracle.DatabaseError as e:
        
        print("Issue ",e)
        
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
    return info











def updateStudent(rno,name):
    con=None
    cursor=None
    try:
        con=cx_Oracle.connect("system/abc123")
        cursor=con.cursor()
        
        
        sql="Update Student set name='%s' where rno='%d'"
        args=(name,rno)
        
        cursor.execute(sql % args)
        con.commit()
        
        if cursor.rowcount!=0:
            msg=str(cursor.rowcount)+"rows updated"
            messagebox.showinfo("Success",msg)
        else:
            messagebox.showerror("Failure ","Rno not Present")
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("Issue : ")
        messagebox.showerror("Failure ",str(e))
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()









def delStudent(rno):
    con=None
    cursor=None
    try:
        con=cx_Oracle.connect("system/abc123")
        cursor=con.cursor()
        
        
        sql="delete from Student where rno='%d'"
        args=(rno)
        
        cursor.execute(sql % args)
        con.commit()
        if cursor.rowcount!=0:
            msg=str(cursor.rowcount)+"rows deleted"
            messagebox.showinfo("Success",msg)
        else:
            messagebox.showinfo("Failure","Invalid Rno.")
            
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("Issue : ",e)
        messagebox.showerror("Failure ",str(e))
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()












            
            
        
