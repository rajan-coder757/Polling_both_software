import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pymysql


def forg():
    t=tkinter.Tk()
    t.geometry('1600x800')
    t.title('forget password')
  







    # login  screen code start

    def login():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        uname=c.get()
        password=e.get()
        sql="select * from users where userid=%s and email=%s"
        cur.execute(sql,[(uname),(password)])
        result=cur.fetchall()
        if result:
            messagebox.showinfo('confirm','detail confirm')
            
            forget()
            t.destroy()
        else:
            messagebox.showinfo('incorrect','enter correct details')
      



    c1=Canvas(t,width=1600,height=700,bg='white',)
    c1.place(x=0,y=0)
    ca=Canvas(t,width=1600,height=60,bg='royal blue',)
    ca.place(x=0,y=0)
    cb=Canvas(t,width=1600,height=100,bg='white')
    cb.place(x=0,y=50)
    cd=Canvas(t,width=1600,height=800,bg='blue')
    cd.place(x=0,y=150)
    cd=Canvas(t,width=400,height=400,bg='royal blue')
    cd.place(x=480,y=250)

    a=Label(t,text='User Id & Email',font=('Arial black',20),bg='royal blue',foreground="white")
    a.place(x=570,y=260)
    b=Label(t,text='User id',font=('Arial black',14),bg='royal blue',foreground="white")
    b.place(x=520,y=350)
    c=Entry(t,width=30,relief="solid")
    c.place(x=640,y=360)

    d=Label(t,text='Email Id',font=('Arial black',14),bg='royal blue',foreground="white")
    d.place(x=520,y=425)
    e=Entry(t,width=30,relief="solid")
    e.place(x=640,y=430)
    b1=Button(t,text="confirm",width=30,height=1,font=('Arial black',10),bg='blue',foreground="white",command=login)
    b1.place(x=550,y=505)


    sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
    sa.place(x=30,y=70)
    sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
    sb.place(x=30,y=95)
    sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
    sc.place(x=1000,y=65)
    sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
    sd.place(x=30,y=10)
    se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
    se.place(x=1100,y=5)








def adminscreen():
   
    t=tkinter.Tk()
    t.geometry('1600x800')
    t.title('Election commision of india')






    # admin pannel code start

    def adminpannel():
        
        t=tkinter.Tk()
        t.geometry('1600x800')
        t.title('insert data')
        
        
        
        
        
        
        
        #Analys code start
        
        def analys():
            
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')
            
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='testdb')
            cur=db.cursor()
            ct=[]
            sal=[]
            sql='select ,sum(salary) from employee group by city'
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                ct.append(res[0])
                sal.append(res[1])
            plt.pie(sal,labels=ct)
            plt.show()
            
            
            
            
            
            
            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
            
            
        
        
        
        
        #result code start
        def results():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('Result')

            i=0
            xa=[]
            xb=[]
            xc=[]
            count=0
            def filldata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select count(canid),canid,wardno from votings group by canid,wardno"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    xa.append(res[2])
                    xb.append(res[1])
                    xc.append(res[0])
                    global count
                    count=count+1
                db.close()
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                
                
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
            def previous():    
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
               
            def showlast():
                global count
                count=count-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                b.insert(0,xa[count])
                d.insert(0,xb[count])
                f.insert(0,xc[count])
               
                
                    
                




                
            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select candidate,totalvote from result where wardno=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    b.insert(0,str(data[0]))
                    d.insert(0,data[1])
                    f.insert(0,str(data[2]))
                    
                            
                    
            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
               
                
                
            heading=Label(t,text='RESULT',font=('Arial Black',25),bg='white',fg='royal blue')
            heading.place(x=600,y=100) 
            a=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=50,relief="solid",font=('Arial Black',14),fg='royal blue')
            b.place(x=400,y=165)
            c=Label(t,text='Candidate',font=('Agency FB',16),bg='white')
            c.place(x=300,y=210)
            d=Entry(t,width=50,relief="solid",font=('Arial Black',14),fg='royal blue')
            d.place(x=400,y=215)
            e=Label(t,text='Total votes',font=('Agency FB',16),bg='white')
            e.place(x=300,y=260)
            f=Entry(t,width=50,relief="solid",font=('Arial Black',14),fg='royal blue')
            f.place(x=400,y=265)

            b1=Button(t,text="Firts",font=('Bernard MT Condensed',14),command=showfirst, bg='royal blue')
            b1.place(x=450,y=350)
            b2=Button(t,text="Next",font=('Bernard MT Condensed',14),command=shownext, bg='royal blue')
            b2.place(x=550,y=350)
            b3=Button(t,text="Last",font=('Bernard MT Condensed',14),command=showlast, bg='royal blue')
            b3.place(x=650,y=350)
            b4=Button(t,text="Previous",font=('Bernard MT Condensed',14),command=previous, bg='royal blue')
            b4.place(x=750,y=350)
            b4=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close, bg='royal blue')
            b4.place(x=1150,y=170)

            filldata()
            showfirst()

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
            
            # result code end
            
            
        










#---------------------------------------------------------voting group code start------------------------------------------------#








        # voting delete code start

        def voted():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            elist=[]
            def fill():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select voteid from votings"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    elist.append(res[0])
                db.close
                    
                

            def deletedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="delete from votings where voteid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('delete','Data delete')
                t.destroy()
                b.delete(0,100)
                
            def close():
                t.destroy()
                
                
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)




            a=Label(t,text='Vote Id',font=('Agency FB',16),bg='white')
            a.place(x=300,y=200)
            b=ttk.Combobox(t,width=80)
            fill()
            b['values']=elist
            b.place(x=400,y=205)
            b1=Button(t,text="Delete",font=('Bernard MT Condensed',14),command=deletedata,bg='royal blue')
            b1.place(x=550,y=280)
            b2=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close,bg='royal blue')
            b2.place(x=650,y=280)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)




        #voting delete code end







        # voting show code start

        def votes():
            t=tkinter.Tk()
            t.geometry('800x800')
            t.title('insert data')

            i=0
            xa=[]
            xb=[]
            xc=[]
            xd=[]

            count=0
            def filldata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select voteid,canid,userid,wardno from votings"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    xa.append(res[0])
                    xb.append(res[1])
                    xc.append(res[2])
                    xd.append(res[3])
                    global count
                    count=count+1
                db.close()
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
            def previous():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                
            def showlast():
                global count
                count=count-1
            
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                b.insert(0,xa[count])
                d.insert(0,xb[count])
                f.insert(0,xc[count])
                h.insert(0,xd[count])
                
                
                    
                




                
            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select name,address,phone,email,wordno from user where userid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    
                            
                    
              
                
            def close():
                t.destroy()
                
                
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
                
                
                
                

            a=Label(t,text='Vote Id',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            c=Label(t,text='Cand Id',font=('Agency FB',16),bg='white')
            c.place(x=300,y=210)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=215)
            e=Label(t,text='User Id',font=('Agency FB',16),bg='white')
            e.place(x=300,y=260)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=265)
            g=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
            g.place(x=300,y=310)
            h=Entry(t,width=80,relief="solid")
            h.place(x=400,y=315)
            b1=Button(t,text="Firts",font=('Bernard MT Condensed',14),command=showfirst, bg='royal blue')
            b1.place(x=400,y=365)
            b2=Button(t,text="Next",font=('Bernard MT Condensed',14),command=shownext, bg='royal blue')
            b2.place(x=500,y=365)
            b3=Button(t,text="Last",font=('Bernard MT Condensed',14),command=showlast, bg='royal blue')
            b3.place(x=600,y=365)
            b4=Button(t,text="Previous",font=('Bernard MT Condensed',14),command=previous, bg='royal blue')
            b4.place(x=700,y=365)
            b5=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close, bg='royal blue')
            b5.place(x=550,y=430)
            filldata()
            showfirst()


            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        # voting show code end
            









        # voting find code start

        def votef():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select canid,userid,wardno from votings where voteid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                 
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    d.insert(0,str(data[0]))
                    f.insert(0,str(data[1]))
                    h.insert(0,str(data[2]))
                    
                    
            def updatedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=int(d.get())
                xf=int(f.get())
                xh=int(h.get())
                sql="update votings set canid=%d, userid=%d,wardno=%d where voteid=%d"%(xd,xf,xh,xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('update','Data update')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
               
                
                    
                

            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)



            a=Label(t,text='Vote Id',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find,bg='royal blue')
            b1.place(x=600,y=210)
            c=Label(t,text='Cand Id',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=265)
            e=Label(t,text='User Id',font=('Agency FB',16),bg='white')
            e.place(x=300,y=310)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=315)
            g=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
            g.place(x=300,y=360)
            h=Entry(t,width=80,relief="solid")
            h.place(x=400,y=365)
            b3=Button(t,text="Update",font=('Bernard MT Condensed',14),command=updatedata,bg='royal blue')
            b3.place(x=550,y=415)
            b4=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b4.place(x=650,y=415)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
            
            
        #voting find code start






        # voting update code start

        def voteu():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select canid,userid,wardno from voting where voteid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                 
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    d.insert(0,str(data[0]))
                    f.insert(0,str(data[1]))
                    h.insert(0,str(data[2]))
                    
                    
            def updatedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=int(d.get())
                xf=int(f.get())
                xh=int(h.get())
                sql="update voting set canid=%d, userid=%d,wardno=%d where voteid=%d"%(xd,xf,xh,xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('update','Data update')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
               
                
                    
                

            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)



            a=Label(t,text='Vote Id',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find,bg='royal blue')
            b1.place(x=600,y=210)
            c=Label(t,text='Cand Id',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=265)
            e=Label(t,text='User Id',font=('Agency FB',16),bg='white')
            e.place(x=300,y=310)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=315)
            g=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
            g.place(x=300,y=360)
            h=Entry(t,width=80,relief="solid")
            h.place(x=400,y=365)
            b3=Button(t,text="Update",font=('Bernard MT Condensed',14),command=updatedata,bg='royal blue')
            b3.place(x=550,y=415)
            b4=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b4.place(x=650,y=415)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)



        # voting update code end









        #voting isert code start

        def votei():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            elist=[]
            def fill():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select canid from candidates"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    elist.append(res[0])
                db.close
                
            elistb=[]
            def fillb():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select wardno from wards"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    elistb.append(res[0])
                db.close
                    

            def insertdata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
               
                xd=int(d.get())
                xf=int(f.get())
                xh=int(h.get())
                sql="insert into votings (canid,userid,wardno) values(%d,%d,%d)"%(xd,xf,xh)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Save','Data save')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                


                    
            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)



            c=Label(t,text='Cand Id',font=('Agency FB',16),bg='white')
            c.place(x=300,y=215)
            d=ttk.Combobox(t,width=77)
            fill()
            d['values']=elist
            d.place(x=400,y=220)
            e=Label(t,text='User Id',font=('Agency FB',16),bg='white')
            e.place(x=300,y=265)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=270)
            g=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
            g.place(x=300,y=315)
            h=ttk.Combobox(t,width=77)
            fillb()
            h['values']=elistb
            h.place(x=400,y=320)

            b1=Button(t,text="Save",font=('Bernard MT Condensed',14),command=insertdata,bg='royal blue')
            b1.place(x=500,y=370)
            b2=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b2.place(x=600,y=370)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)


        #voting isert code end




        #-------------------------------------------------------voting group code end-------------------------------------------------#




















        #---------------------------------------------------schedule group code start-----------------------------------------------------#



        #schedule delete code start

        def schd():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            elist=[]
            def fill():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select wardno from schedule"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    elist.append(res[0])
                db.close
                    
                

            def deletedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="delete from schedule where wardno=%d"%(xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('delete','Data delete')
                b.delete(0,100)
                
                

            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)



            a=Label(t,text='ward no',font=('Agency FB',16),bg='white')
            a.place(x=300,y=200)
            b=ttk.Combobox(t,width=80)
            fill()
            b['values']=elist
            b.place(x=410,y=200)
            b1=Button(t,text="Delete",font=('Bernard MT Condensed',14),command=deletedata,bg='royal blue')
            b1.place(x=550,y=250)
            b2=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close,bg='royal blue')
            b2.place(x=650,y=250)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        # schedule delete code end













        # schedule show code start
        def schs():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            i=0
            xa=[]
            xb=[]
            count=0
            def filldata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select wardno,dateofelection from schedule"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    xa.append(res[0])
                    xb.append(res[1])
                    global count
                    count=count+1
                db.close()
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                
                
                
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                
            def previous():    
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100) 
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                
               
            def showlast():
                global count
                count=count-1
                
                b.delete(0,100)
                d.delete(0,100)
                b.insert(0,xa[count])
                d.insert(0,xb[count])
                
               
                
                    
                




                
            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select wardno,dateofelection from schedule where wardno=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    b.delete(0,100)
                    d.delete(0,100)
                    b.insert(0,str(data[0]))
                    d.insert(0,str(data[1]))
                    
                    
                            
                    
            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
               
                
                
             
            a=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=420,y=165)
            c=Label(t,text='Date of Election',font=('Agency FB',16),bg='white')
            c.place(x=300,y=210)
            d=Entry(t,width=80,relief="solid")
            d.place(x=420,y=215)


            b1=Button(t,text="Firts",font=('Bernard MT Condensed',14),command=showfirst, bg='royal blue')
            b1.place(x=450,y=260)
            b2=Button(t,text="Next",font=('Bernard MT Condensed',14),command=shownext, bg='royal blue')
            b2.place(x=550,y=260)
            b3=Button(t,text="Last",font=('Bernard MT Condensed',14),command=showlast, bg='royal blue')
            b3.place(x=650,y=260)
            b4=Button(t,text="Previous",font=('Bernard MT Condensed',14),command=previous, bg='royal blue')
            b4.place(x=750,y=260)
            b4=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close, bg='royal blue')
            b4.place(x=610,y=320)

            filldata()
            showfirst()

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        # schedule show code end
















        #schedule find code start
        def schf():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select wardno,dateofelection from schedule where wardno=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    
                    d.delete(0,100)
                    d.insert(0,data[1])
                    
                    
                    
                

            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550) 




            a=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=420,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find, bg='royal blue')
            b1.place(x=550,y=210)
            c=Label(t,text='Date of Election',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=420,y=265)
            b3=Button(t,text="Close",font=('Bernard MT Condensed',14), bg='royal blue',command=close)
            b3.place(x=550,y=310)


            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
            
        # schdeule find code end














        # schedule update code start

        def schu():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select wardno,dateofelection from schedule where wardno=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    
                    d.delete(0,100)
                    d.insert(0,str(data[1]))
                    
                    
                    
                    
                    
            def updatedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=d.get()    
                sql="update schedule set dateofelection='%s'where wardno=%d"%(xd,xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('update','Data update')
                b.delete(0,100)
                d.delete(0,100)
                
                
                
                

            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)        
                





            a=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=420,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find,bg='royal blue')
            b1.place(x=600,y=210)
            c=Label(t,text=' Date of Election',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=420,y=265)
            b3=Button(t,text="Update",font=('Bernard MT Condensed',14),command=updatedata,bg='royal blue')
            b3.place(x=550,y=310)
            b3=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b3.place(x=650,y=315)

            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        # schedule update code end















        # schedule insert code start 

        def schi():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')
            def insertdata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=d.get()
                sql="insert into schedule values(%d,'%s')"%(xb,xd)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Save','Data save')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                
                
            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550) 





            a=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=420,y=165)
            c=Label(t,text=' Date of Election',font=('Agency FB',16),bg='white')
            c.place(x=300,y=210)
            d=Entry(t,width=80,relief="solid")
            d.place(x=420,y=215)
            b1=Button(t,text="Save",font=('Bernard MT Condensed',14),command=insertdata,bg='royal blue')
            b1.place(x=550,y=260)
            b2=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b2.place(x=650,y=265)


            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
            




        # schedule insert end here





        #----------------------------------------------------------schedule group code end-------------------------------------------------#


















        #----------------------------------------------------candidate group code start-------------------------------------------------#





        # candidate delete code start

        def cand():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            elist=[]
            def fill():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select canid from candidates"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    elist.append(res[0])
                db.close
                    
                

            def deletedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="delete from user where userid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('delete','Data delete')
                t.destroy()
                b.delete(0,100)
                
            def close():
                t.destroy()
                
                
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)




            a=Label(t,text='Cand Id',font=('Agency FB',16),bg='white')
            a.place(x=300,y=200)
            b=ttk.Combobox(t,width=80)
            fill()
            b['values']=elist
            b.place(x=400,y=205)
            b1=Button(t,text="Delete",font=('Bernard MT Condensed',14),command=deletedata,bg='royal blue')
            b1.place(x=550,y=280)
            b2=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close,bg='royal blue')
            b2.place(x=650,y=280)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)


        # candidate delete code end













        # candidate show code start

        def cans():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            i=0
            xa=[]
            xb=[]
            xc=[]
            xd=[]
            xe=[]
            xf=[]
            xg=[]
            count=0
            def filldata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select canid,canname,email,phone,address,govtid,wardno from candidates"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    xa.append(res[0])
                    xb.append(res[1])
                    xc.append(res[2])
                    xd.append(res[3])
                    xe.append(res[4])
                    xf.append(res[5])
                    xg.append(res[6])
                    global count
                    count=count+1
                db.close()
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                n.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                j.insert(0,xe[i])
                l.insert(0,xf[i])
                n.insert(0,xg[i])
                
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                n.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                j.insert(0,xe[i])
                l.insert(0,xf[i])
                n.insert(0,xg[i])
            def previous():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                n.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                j.insert(0,xe[i])
                l.insert(0,xf[i])
                n.insert(0,xg[i])
            def showlast():
                global count
                count=count-1
                
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                n.delete(0,100)
                b.insert(0,xa[count])
                d.insert(0,xb[count])
                f.insert(0,xc[count])
                h.insert(0,xd[count])
                j.insert(0,xe[count])
                l.insert(0,xf[count])
                n.insert(0,xg[count])
                
                    
                




            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select canname,email,phone,address,govtid,wardno from candidates where canid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                 
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    j.delete(0,100)
                    l.delete(0,100)
                    n.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    j.insert(0,data[3])
                    l.insert(0,str(data[4]))
                    n.insert(0,str(data[5]))

                            
                    
              
                
            def close():
                t.destroy()
                
                
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
                
                
                
                

            a=Label(t,text='Cand id',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            c=Label(t,text='Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=215)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=220)
            e=Label(t,text='Email',font=('Agency FB',16),bg='white')
            e.place(x=300,y=265)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=270)
            g=Label(t,text='Phone',font=('Agency FB',16),bg='white')
            g.place(x=300,y=315)
            h=Entry(t,width=80,relief="solid")
            h.place(x=400,y=320)
            i=Label(t,text='Address',font=('Agency FB',16),bg='white')
            i.place(x=300,y=365)
            j=Entry(t,width=80,relief="solid")
            j.place(x=400,y=370)
            k=Label(t,text='Govt Id',font=('Agency FB',16),bg='white')
            k.place(x=300,y=415)
            l=Entry(t,width=80,relief="solid")
            l.place(x=400,y=420)
            m=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            m.place(x=300,y=460)
            n=Entry(t,width=80,relief="solid")
            n.place(x=400,y=465)
            b1=Button(t,text="Firts",font=('Bernard MT Condensed',14),command=showfirst, bg='royal blue')
            b1.place(x=400,y=515)
            b2=Button(t,text="Next",font=('Bernard MT Condensed',14),command=shownext, bg='royal blue')
            b2.place(x=500,y=515)
            b3=Button(t,text="Last",font=('Bernard MT Condensed',14),command=showlast, bg='royal blue')
            b3.place(x=600,y=515)
            b4=Button(t,text="Previous",font=('Bernard MT Condensed',14),command=previous, bg='royal blue')
            b4.place(x=700,y=515)
            b5=Button(t,text="Close",width=10,font=('Bernard MT Condensed',14),command=close, bg='royal blue')
            b5.place(x=1000,y=200)
            filldata()
            showfirst()


            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        # candidate show code end









        # candidate find code start

        def canf():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select canname,email,phone,address,govtid,wardno from candidates where canid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    j.delete(0,100)
                    l.delete(0,100)
                    n.delete(0,100)
                    
                    d.insert(0,data[0])             
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    j.insert(0,data[3])
                    l.insert(0,str(data[4]))
                    n.insert(0,str(data[5]))




            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))                
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)



            a=Label(t,text='Cand Id',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=450,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find, bg='royal blue')
            b1.place(x=700,y=210)
            c=Label(t,text='Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=450,y=265)
            e=Label(t,text='Email',font=('Agency FB',16),bg='white')
            e.place(x=300,y=310)
            f=Entry(t,width=80,relief="solid")
            f.place(x=450,y=315)
            g=Label(t,text='Phone',font=('Agency FB',16),bg='white')
            g.place(x=300,y=360)
            h=Entry(t,width=80,relief="solid")
            h.place(x=450,y=365)
            i=Label(t,text='Address',font=('Agency FB',16),bg='white')
            i.place(x=300,y=410)
            j=Entry(t,width=80,relief="solid")
            j.place(x=450,y=415)
            k=Label(t,text='Govt Id',font=('Agency FB',16),bg='white')
            k.place(x=300,y=460)
            l=Entry(t,width=80,relief="solid")
            l.place(x=450,y=465)
            m=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            m.place(x=300,y=510)
            n=Entry(t,width=80,relief="solid")
            n.place(x=450,y=515)
            b3=Button(t,text="Close",font=('Bernard MT Condensed',14), bg='royal blue',command=close)
            b3.place(x=700,y=550)


            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
            
        # candidate find code end









        # candidate update code start

        def canu():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select canname,email,phone,address,govtid,wardno from candidates where canid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                 
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    j.delete(0,100)
                    l.delete(0,100)
                    n.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    j.insert(0,data[3])
                    l.insert(0,str(data[4]))
                    n.insert(0,str(data[5]))
                    
            def updatedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=d.get()
                xf=f.get()
                xh=int(h.get())
                xj=j.get()
                xl=int(l.get())
                xn=int(l.get())
                sql="update candidates set canname='%s', email='%s', phone=%d, address='%s',govtid=%d,wardno=%d where canid=%d"%(xd,xf,xh,xj,xl,xn,xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('update','Data update')
                t.destroy()
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                n.delete(0,100)
                
                
                    
                

            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)



            a=Label(t,text='Cand Id',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find,bg='royal blue')
            b1.place(x=600,y=210)
            c=Label(t,text='Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=265)
            e=Label(t,text='Email',font=('Agency FB',16),bg='white')
            e.place(x=300,y=310)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=315)
            g=Label(t,text='Phone',font=('Agency FB',16),bg='white')
            g.place(x=300,y=360)
            h=Entry(t,width=80,relief="solid")
            h.place(x=400,y=365)
            i=Label(t,text='Address',font=('Agency FB',16),bg='white')
            i.place(x=300,y=410)
            j=Entry(t,width=80,relief="solid")
            j.place(x=400,y=415)
            k=Label(t,text='Govt Id',font=('Agency FB',16),bg='white')
            k.place(x=300,y=460)
            l=Entry(t,width=80,relief="solid")
            l.place(x=400,y=465)
            m=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            m.place(x=300,y=510)
            n=Entry(t,width=80,relief="solid")
            n.place(x=400,y=515)
            b2=Button(t,text="Update",font=('Bernard MT Condensed',14),command=updatedata,bg='royal blue')
            b2.place(x=550,y=550)
            b3=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b3.place(x=650,y=550 )

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
            
        #candidate update code end
            
            
            
            
            


        # candidate insert code start

        def cani():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.config(bg='#808069')
            t.title('Candidate insert')
                

            def insertdata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=d.get()
                xf=f.get()
                xh=int(h.get())
                xj=j.get()
                xl=int(l.get())
                xn=int(n.get())
                sql="insert into candidates values(%d,'%s','%s',%d,'%s',%d,%d)"%(xb,xd,xf,xh,xj,xl,xn)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Save','Data save')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                n.delete(0,100)
                
            def close():
                t.destroy()
                
                
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)


            a=Label(t,text='Cand id',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            c=Label(t,text='Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=215)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=220)
            e=Label(t,text='Email',font=('Agency FB',16),bg='white')
            e.place(x=300,y=265)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=270)
            g=Label(t,text='Phone',font=('Agency FB',16),bg='white')
            g.place(x=300,y=315)
            h=Entry(t,width=80,relief="solid")
            h.place(x=400,y=320)
            i=Label(t,text='Address',font=('Agency FB',16),bg='white')
            i.place(x=300,y=365)
            j=Entry(t,width=80,relief="solid")
            j.place(x=400,y=370)
            k=Label(t,text='Govt Id',font=('Agency FB',16),bg='white')
            k.place(x=300,y=415)
            l=Entry(t,width=80,relief="solid")
            l.place(x=400,y=420)
            m=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            m.place(x=300,y=460)
            n=Entry(t,width=80,relief="solid")
            n.place(x=400,y=465)
            b1=Button(t,text="Register",font=('Arial Black',12),command=insertdata,bg='royal blue',foreground="white")
            b1.place(x=500,y=510)
            b2=Button(t,text="Close",font=('Arial Black',12),bg='royal blue',command=close,foreground="white")
            b2.place(x=650,y=510)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)






        # candidate insert code end




        #----------------------------------------------------------candidate group code end------------------------------------------------#

















        #------------------------------------------------------------ ward group code start----------------------------------------------#





        # ward delete code start

        def wardd():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            elist=[]
            def fill():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select wardno from wards"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    elist.append(res[0])
                db.close
                    
                

            def deletedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="delete from wards where wardno=%d"%(xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('delete','Data delete')
                b.deletre(0,100)
                
                

            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)



            a=Label(t,text='ward no',font=('Agency FB',16),bg='white')
            a.place(x=300,y=200)
            b=ttk.Combobox(t,width=80)
            fill()
            b['values']=elist
            b.place(x=410,y=200)
            b1=Button(t,text="Delete",font=('Bernard MT Condensed',14),command=deletedata,bg='royal blue')
            b1.place(x=550,y=250)
            b2=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close,bg='royal blue')
            b2.place(x=650,y=250)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        # ward delete code end









        # ward show code start

        def wards():
            
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')
            
            i=0
            xa=[]
            xb=[]
            xc=[]
            count=0
            def filldata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select wardno,wardname,remark from wards"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    xa.append(res[0])
                    xb.append(res[1])
                    xc.append(res[2])
                    global count
                    count=count+1
                db.close()
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                
                
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
            def previous():    
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
               
            def showlast():
                global count
                count=count-1
                
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                b.insert(0,xa[count])
                d.insert(0,xb[count])
                f.insert(0,xc[count])
               
                
                    
                
            
            
            
            
                
            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select wardname,remark from wards where wardno=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    b.insert(0,str(data[0]))
                    d.insert(0,data[1])
                    f.insert(0,str(data[2]))
                    
                            
                    
            def close():
                  t.destroy()
                    
                
            
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
               
                
                
             
            a=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            c=Label(t,text='Ward Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=210)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=215)
            e=Label(t,text='Remark',font=('Agency FB',16),bg='white')
            e.place(x=300,y=260)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=265)
            
            b1=Button(t,text="Firts",font=('Bernard MT Condensed',14),command=showfirst, bg='royal blue')
            b1.place(x=450,y=310)
            b2=Button(t,text="Next",font=('Bernard MT Condensed',14),command=shownext, bg='royal blue')
            b2.place(x=550,y=310)
            b3=Button(t,text="Last",font=('Bernard MT Condensed',14),command=showlast, bg='royal blue')
            b3.place(x=650,y=310)
            b4=Button(t,text="Previous",font=('Bernard MT Condensed',14),command=previous, bg='royal blue')
            b4.place(x=750,y=310)
            b4=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close, bg='royal blue')
            b4.place(x=610,y=380)
            
            filldata()
            showfirst()
            
            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        #ward show code end
            












        # ward find code start

        def wardf():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select wardname,remark from wards where wardno=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    
                    d.delete(0,100)
                    f.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    
                    
                

            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550) 




            a=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find, bg='royal blue')
            b1.place(x=550,y=210)
            c=Label(t,text='Ward Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=265)
            e=Label(t,text='Remark',font=('Agency FB',16),bg='white')
            e.place(x=300,y=310)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=315)
            b3=Button(t,text="Close",font=('Bernard MT Condensed',14), bg='royal blue',command=close)
            b3.place(x=550,y=365)


            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)



        #ward find code end



        # ward update code start

        def wardu():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select wardname,remark from wards where wardno=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    
                    d.delete(0,100)
                    f.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    
                    
                    
                    
            def updatedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=d.get()
                xf=f.get()    
                sql="update wards set wardname='%s', remark='%s' where wardno=%d"%(xd,xf,xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('update','Data update')
                d.delete(0,100)
                f.delete(0,100)
                
                
                

            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)        
                





            a=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find,bg='royal blue')
            b1.place(x=600,y=210)
            c=Label(t,text=' Ward Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=265)
            e=Label(t,text='Remark',font=('Agency FB',16),bg='white')
            e.place(x=300,y=310)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=315)
            b3=Button(t,text="Update",font=('Bernard MT Condensed',14),command=updatedata,bg='royal blue')
            b3.place(x=550,y=360)
            b3=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b3.place(x=650,y=365)

            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        # ward update code end











        # ward insert code start

        def wardi():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')
            def insertdata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=d.get()
                xf=f.get()
                sql="insert into wards values(%d,'%s','%s')"%(xb,xd,xf)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Save','Data save')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                
                
            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550) 





            a=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            c=Label(t,text=' Ward Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=210)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=215)
            e=Label(t,text='Remark',font=('Agency FB',16),bg='white')
            e.place(x=300,y=260)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=265)
            b1=Button(t,text="Save",font=('Bernard MT Condensed',14),command=insertdata,bg='royal blue')
            b1.place(x=550,y=310)
            b2=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b2.place(x=650,y=315)


            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
            
        # ward insert code end




        #------------------------------------------------------ ward group code end--------------------------------------------------------#
            























        #-------------------------------------------------user group code start--------------------------------------------------------#




        # user delete code start
        def userd():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            elist=[]
            def fill():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select userid from users"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    elist.append(res[0])
                db.close
                    
                

            def deletedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="delete from users where userid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('delete','Data delete')
                b.deletre(0,100)
                
            def close():
                t.destroy()
                
                
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)




            a=Label(t,text='User ID',font=('Agency FB',16),bg='white')
            a.place(x=300,y=200)
            b=ttk.Combobox(t,width=80)
            fill()
            b['values']=elist
            b.place(x=400,y=205)
            b1=Button(t,text="Delete",font=('Bernard MT Condensed',14),command=deletedata,bg='royal blue')
            b1.place(x=550,y=280)
            b2=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close,bg='royal blue')
            b2.place(x=650,y=280)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
            
            
            
        #user delete code end








        # user show code start

        def users():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            i=0
            xa=[]
            xb=[]
            xc=[]
            xd=[]
            xe=[]
            xf=[]
            count=0
            def filldata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select userid,name,address,phone,email,wordno from users"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    xa.append(res[0])
                    xb.append(res[1])
                    xc.append(res[2])
                    xd.append(res[3])
                    xe.append(res[4])
                    xf.append(res[5])
                    global count
                    count=count+1
                db.close()
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                j.insert(0,xe[i])
                l.insert(0,xf[i])
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                j.insert(0,xe[i])
                l.insert(0,xf[i])
            def previous():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                j.insert(0,xe[i])
                l.insert(0,xf[i])
            def showlast():
                global count
                count=0
                count=count-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                b.insert(0,xa[count])
                d.insert(0,xb[count])
                f.insert(0,xc[count])
                h.insert(0,xd[count])
                j.insert(0,xe[count])
                l.insert(0,xe[count])
                
                    
                




                
            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select name,address,phone,email,wordno from users where userid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    j.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    j.insert(0,data[3])
                            
                    
              
                
            def close():
                t.destroy()
                
                
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
                
                
                
                

            a=Label(t,text='User ID',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            c=Label(t,text='Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=210)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=215)
            e=Label(t,text='Address',font=('Agency FB',16),bg='white')
            e.place(x=300,y=260)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=265)
            g=Label(t,text='Phone',font=('Agency FB',16),bg='white')
            g.place(x=300,y=310)
            h=Entry(t,width=80,relief="solid")
            h.place(x=400,y=315)
            ia=Label(t,text='Email',font=('Agency FB',16),bg='white')
            ia.place(x=300,y=360)
            j=Entry(t,width=80,relief="solid")
            j.place(x=400,y=365)
            k=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
            k.place(x=300,y=410)
            l=Entry(t,width=80,relief="solid")
            l.place(x=400,y=415)
            b1=Button(t,text="Firts",font=('Bernard MT Condensed',14),command=showfirst, bg='royal blue')
            b1.place(x=400,y=465)
            b2=Button(t,text="Next",font=('Bernard MT Condensed',14),command=shownext, bg='royal blue')
            b2.place(x=500,y=465)
            b3=Button(t,text="Last",font=('Bernard MT Condensed',14),command=showlast, bg='royal blue')
            b3.place(x=600,y=465)
            b4=Button(t,text="Previous",font=('Bernard MT Condensed',14),command=previous, bg='royal blue')
            b4.place(x=700,y=465)
            b5=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close, bg='royal blue')
            b5.place(x=550,y=530)
            filldata()
            showfirst()


            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

            

          
        # user show code end
            















        # user find code start

        def userf():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select name,address,phone,email,wordno from users where userid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                 
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    j.delete(0,100)
                    l.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    j.insert(0,data[3])
                    l.insert(0,str(data[4]))
                




            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)



            a=Label(t,text='User ID',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=450,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find, bg='royal blue')
            b1.place(x=600,y=210)
            c=Label(t,text='Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=450,y=265)
            e=Label(t,text='Address',font=('Agency FB',16),bg='white')
            e.place(x=300,y=310)
            f=Entry(t,width=80,relief="solid")
            f.place(x=450,y=315)
            g=Label(t,text='Phone',font=('Agency FB',16),bg='white')
            g.place(x=300,y=360)
            h=Entry(t,width=80,relief="solid")
            h.place(x=450,y=365)
            i=Label(t,text='Email',font=('Agency FB',16),bg='white')
            i.place(x=300,y=410)
            j=Entry(t,width=80,relief="solid")
            j.place(x=450,y=415)
            k=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            k.place(x=300,y=460)
            l=Entry(t,width=80,relief="solid")
            l.place(x=450,y=465)
            b3=Button(t,text="Close",font=('Bernard MT Condensed',14), bg='royal blue',command=close)
            b3.place(x=600,y=510)


            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        # user find code end






        # user update code start

        def useru():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')
            
            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select name,address,phone,email,wordno from users where userid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    j.delete(0,100)
                    l.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    j.insert(0,data[3])
                    l.insert(0,str(data[4]))
                    
            def updatedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=d.get()
                xf=f.get()
                xh=int(h.get())
                xj=j.get()
                xl=int(l.get())
                sql="update users set name='%s', address='%s', phone=%d, email='%s',wordno=%d where userid=%d"%(xd,xf,xh,xj,xl,xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('update','Data update')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                
                
                    
                
            
            def close():
                  t.destroy()
                    
                
            
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
            
            
            
            a=Label(t,text='User ID',font=('Agency FB',16),bg='white')
            a.place(x=300,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=165)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find,bg='royal blue')
            b1.place(x=600,y=210)
            c=Label(t,text='Name',font=('Agency FB',16),bg='white')
            c.place(x=300,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=400,y=265)
            e=Label(t,text='Address',font=('Agency FB',16),bg='white')
            e.place(x=300,y=310)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=315)
            g=Label(t,text='Phone',font=('Agency FB',16),bg='white')
            g.place(x=300,y=360)
            h=Entry(t,width=80,relief="solid")
            h.place(x=400,y=365)
            i=Label(t,text='Email',font=('Agency FB',16),bg='white')
            i.place(x=300,y=410)
            j=Entry(t,width=80,relief="solid")
            j.place(x=400,y=415)
            k=Label(t,text='Ward no',font=('Agency FB',16),bg='white')
            k.place(x=300,y=460)
            l=Entry(t,width=80,relief="solid")
            l.place(x=400,y=465)
            b3=Button(t,text="Update",font=('Bernard MT Condensed',14),command=updatedata,bg='royal blue')
            b3.place(x=550,y=515)
            b3=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b3.place(x=650,y=515)
            
            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        # user update code end




















        # user insert code start
        def useri():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            xa=[]
            i=0
            count=0


                
                
            def insertdata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xbd=int(bd.get())
                xd=d.get()
                xf=f.get()
                xh=int(h.get())
                xj=j.get()
                xl=int(l.get())
                sql="insert into users values(%d,%d,'%s','%s',%d,'%s',%d)"%(xb,xbd,xd,xf,xh,xj,xl)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('register','register successfully')
                t.destroy()
                b.delete(0,100)
                bd.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                l.delete(0,100)
                
                
                  

            def filldata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select userid from users"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    xa.append(res[0])
                    global count
                    count=count+1
                db.close()
                
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                b.insert(0,xa[-1]+1)
               


                    
            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            cd=Canvas(t,width=250,height=520,bg='royal blue')
            cd.place(x=0,y=150)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=300,y=550)


            a=Label(t,text='User id',font=('Agency FB',16),bg='white')
            a.place(x=400,y=160)
            b=Entry(t,width=80,relief="solid")
            b.place(x=500,y=165)
            filldata()
            showfirst()
            bc=Label(t,text='Password',font=('Agency FB',16),bg='white')
            bc.place(x=400,y=215)
            bd=Entry(t,width=80,relief="solid")
            bd.place(x=500,y=220)
            c=Label(t,text='Name',font=('Agency FB',16),bg='white')
            c.place(x=400,y=260)
            d=Entry(t,width=80,relief="solid")
            d.place(x=500,y=265)
            e=Label(t,text='Address',font=('Agency FB',16),bg='white')
            e.place(x=400,y=310)
            f=Entry(t,width=80,relief="solid")
            f.place(x=500,y=315)
            g=Label(t,text='Phone',font=('Agency FB',16),bg='white')
            g.place(x=400,y=360)
            h=Entry(t,width=80,relief="solid")
            h.place(x=500,y=365)
            i=Label(t,text='Email',font=('Agency FB',16),bg='white')
            i.place(x=400,y=410)
            j=Entry(t,width=80,relief="solid")
            j.place(x=500,y=415)
            k=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
            k.place(x=400,y=460)
            l=Entry(t,width=80,relief="solid")
            l.place(x=500,y=465)
            b1=Button(t,text="REGISTER",width=20,height=2,font=('Arial black',10),bg='white',command=insertdata)
            b1.place(x=30,y=200)
            b2=Button(t,text="CLOSE",width=20,height=2,font=('Arial black',10),bg='white',command=close)
            b2.place(x=30,y=350)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        #user insert code end








        #-------------------------------------------------------user group code end-------------------------------------------------------#



























        #------------------------------ admin group code start------------------------------------------------------------------------------



        # admin delete code start

        def admind():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')
            elist=[]
            def fill():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select adminid from admin"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    elist.append(res[0])
                db.close

            def deletedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="delete from admin where adminid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('delete','Data delete')
                b.deletre(0,100)
                
                
            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)

                

            a=Label(t,text='Admin ID:-',font=('Agency FB',16),bg='white')
            a.place(x=300,y=200)
            b=ttk.Combobox(t,width=80)
            fill()
            b['values']=elist
            b.place(x=400,y=200)
            b1=Button(t,text="Delete",font=('Bernard MT Condensed',14),command=deletedata,bg='royal blue')
            b1.place(x=550,y=300)
            b2=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b2.place(x=650,y=300)
            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)


        #admin delete code end





















        #admin show code start


        def admins():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            i=0
            xa=[]
            xb=[]
            xc=[]
            xd=[]
            xe=[]
            count=0
            def filldata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                sql="select adminid,password,name,email,phone from admin"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    xa.append(res[0])
                    xb.append(res[1])
                    xc.append(res[2])
                    xd.append(res[3])
                    xe.append(res[4])
                    global count
                    count=count+1
                db.close()
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                j.insert(0,xe[i])
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                j.insert(0,xe[i])
            def previous():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                b.insert(0,xa[i])
                d.insert(0,xb[i])
                f.insert(0,xc[i])
                h.insert(0,xd[i])
                j.insert(0,xe[i])
            def showlast():
                global count
                count=count-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                b.insert(0,xa[count])
                d.insert(0,xb[count])
                f.insert(0,xc[count])
                h.insert(0,xd[count])
                j.insert(0,xe[count])
                
                    
                




                
            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select password,name,email,phone from admin where admin=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    j.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    j.insert(0,data[3])
                            
                    
            def close():
                  t.destroy()
                    
                

            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
                
                
                
               
            a=Label(t,text='Admin ID',font=('Agency FB',16),bg='white')
            a.place(x=300,y=180)
            b=Entry(t,width=80,relief="solid")
            b.place(x=400,y=185)
            c=Label(t,text='Password',font=('Agency FB',16),bg='white')
            c.place(x=300,y=230)
            d=Entry(t,width=80,relief="solid",show='*')
            d.place(x=400,y=235)
            e=Label(t,text='A Name',font=('Agency FB',16),bg='white')
            e.place(x=300,y=280)
            f=Entry(t,width=80,relief="solid")
            f.place(x=400,y=285)
            g=Label(t,text='Email',font=('Agency FB',16),bg='white')
            g.place(x=300,y=330)
            h=Entry(t,width=80,relief="solid")
            h.place(x=400,y=335)
            ia=Label(t,text='Phone',font=('Agency FB',16),bg='white')
            ia.place(x=300,y=380)
            j=Entry(t,width=80,relief="solid")
            j.place(x=400,y=385)
            b1=Button(t,text="Firts",font=('Bernard MT Condensed',14),command=showfirst, bg='royal blue')
            b1.place(x=400,y=450)
            b2=Button(t,text="Next",font=('Bernard MT Condensed',14),command=shownext, bg='royal blue')
            b2.place(x=500,y=450)
            b3=Button(t,text="Last",font=('Bernard MT Condensed',14),command=showlast, bg='royal blue')
            b3.place(x=600,y=450)
            b4=Button(t,text="Previous",font=('Bernard MT Condensed',14),command=previous, bg='royal blue')
            b4.place(x=700,y=450)
            b4=Button(t,text="Close",font=('Bernard MT Condensed',14),command=close, bg='royal blue')
            b4.place(x=550,y=520)
            filldata()
            showfirst()


            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        #admin show code end












        #admin find data start
        def adminf():

            

            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')
            
            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select password,name,email,phone from admin where adminid=%d"%(xb)
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    j.delete(0,100)
                    d.insert(0,str(data[0]))
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    j.insert(0,str(data[3]))
                    
            def close():
                  t.destroy()
                    
                
            
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)
            
            
            a=Label(t,text='Admin ID:-',font=('Agency FB',16),bg='white')
            a.place(x=300,y=180)
            b=Entry(t,width=80,relief="solid")
            b.place(x=380,y=180)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find,bg='royal blue')
            b1.place(x=575,y=230)
            c=Label(t,text='Password:-',font=('Agency FB',16),bg='white')
            c.place(x=300,y=270)
            d=Entry(t,width=80,relief="solid",show="*")
            d.place(x=380,y=275)
            e=Label(t,text='Name:-',font=('Agency FB',16),bg='white')
            e.place(x=300,y=320)
            f=Entry(t,width=80,relief="solid")
            f.place(x=380,y=325)
            g=Label(t,text='Email:-',font=('Agency FB',16),bg='white')
            g.place(x=300,y=370)
            h=Entry(t,width=80,relief="solid")
            h.place(x=380,y=375)
            i=Label(t,text='Phone:-',font=('Agency FB',16),bg='white')
            i.place(x=300,y=420)
            j=Entry(t,width=80,relief="solid")
            j.place(x=380,y=425)
            b3=Button(t,text="close",font=('Bernard MT Condensed',14),command=close,bg='royal blue')
            b3.place(x=550,y=475)
            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)

        #admin find code end










        # admin update code start here
        def adminu():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')

            def find():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                sql="select password,name,email,phone from admin where adminid=%d"%(xb)  
                cur.execute(sql)
                db.commit()
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo("Check","Check data")
                else:        
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    j.delete(0,100)
                    d.insert(0,data[0])
                    f.insert(0,data[1])
                    h.insert(0,str(data[2]))
                    j.insert(0,data[3])
                    
                    
            def updatedata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=int(d.get())
                xf=f.get()
                xh=h.get()
                xj=int(j.get())
                sql="update admin set password=%d, name='%s', email='%s', phone=%d where adminid=%d"%(xd,xf,xh,xj,xb)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('update','Data update')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)
                
            def close():
                    t.destroy()  
                    
                
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=20,y=550)




            a=Label(t,text='Admin ID:-',font=('Agency FB',16),bg='white')
            a.place(x=300,y=180)
            b=Entry(t,width=80,relief="solid")
            b.place(x=380,y=180)
            b1=Button(t,text="Find",font=('Bernard MT Condensed',14),command=find,bg='royal blue')
            b1.place(x=575,y=230)
            c=Label(t,text='Password:-',font=('Agency FB',16),bg='white')
            c.place(x=300,y=270)
            d=Entry(t,width=80,relief="solid",show="*")
            d.place(x=380,y=275)
            e=Label(t,text='Name:-',font=('Agency FB',16),bg='white')
            e.place(x=300,y=320)
            f=Entry(t,width=80,relief="solid")
            f.place(x=380,y=325)
            g=Label(t,text='Email:-',font=('Agency FB',16),bg='white')
            g.place(x=300,y=370)
            h=Entry(t,width=80,relief="solid")
            h.place(x=380,y=375)
            i=Label(t,text='Phone:-',font=('Agency FB',16),bg='white')
            i.place(x=300,y=420)
            j=Entry(t,width=80,relief="solid")
            j.place(x=380,y=425)
            b3=Button(t,text="Update",font=('Bernard MT Condensed',14),command=updatedata,bg='royal blue')
            b3.place(x=550,y=475)
            b3=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
            b3.place(x=650,y=475)



            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)
        #admin update code end 












        # admin isert code start here
        def admini():
            t=tkinter.Tk()
            t.geometry('1600x800')
            t.title('insert data')


            # functions
            def insertdata():
                db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
                cur=db.cursor()
                xb=int(b.get())
                xd=int(d.get())
                xf=f.get()
                xh=h.get()
                xj=int(j.get())
                sql="insert into admin values(%d,%d,'%s','%s',%d)"%(xb,xd,xf,xh,xj)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('register','Successfully register')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                j.delete(0,100)

            def close():
                  t.destroy()    
                
            # design    
            c1=Canvas(t,width=1600,height=700,bg='white',)
            c1.place(x=0,y=0)
            ca=Canvas(t,width=1600,height=60,bg='royal blue',)
            ca.place(x=0,y=0)
            cb=Canvas(t,width=1600,height=100,bg='white')
            cb.place(x=0,y=50)
            cd=Canvas(t,width=250,height=520,bg='royal blue')
            cd.place(x=0,y=150)
            sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
            sa.place(x=30,y=70)
            sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
            sb.place(x=30,y=95)
            sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
            sc.place(x=1000,y=65)
            sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
            sd.place(x=30,y=10)
            se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
            se.place(x=1100,y=5)
            sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
            sf.place(x=400,y=550)

            #form work
            a=Label(t,text='Admin id:-',font=('Agency FB',16),bg='white')
            a.place(x=400,y=180)
            b=Entry(t,width=80,relief="solid")
            b.place(x=480,y=185)
            c=Label(t,text='Password:-',font=('Agency FB',16),bg='white')
            c.place(x=400,y=230)
            d=Entry(t,width=80,relief="solid")
            d.place(x=480,y=230)
            e=Label(t,text='Name:-',font=('Agency FB',16),bg='white')
            e.place(x=400,y=270)
            f=Entry(t,width=80,relief="solid")
            f.place(x=480,y=270)
            g=Label(t,text='Email:-',font=('Agency FB',16),bg='white')
            g.place(x=400,y=320)
            h=Entry(t,width=80,relief="solid")
            h.place(x=480,y=320)
            i=Label(t,text='Phone:-',font=('Agency FB',16),bg='white')
            i.place(x=400,y=370)
            j=Entry(t,width=80,relief="solid")
            j.place(x=480,y=370)
            b1=Button(t,text="REGISTER",width=20,height=2,font=('Arial black',10),bg='white',command=insertdata)
            b1.place(x=30,y=200)
            b2=Button(t,text="CLOSE",width=20,height=2,font=('Arial black',10),bg='white',command=close)
            b2.place(x=30,y=350)

            #footer
            cd=Canvas(t,width=1600,height=150,bg='royal blue',)
            cd.place(x=0,y=600)
            sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
            sg.place(x=20,y=620)
            sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
            sh.place(x=1000,y=620)


        # admin insert code end here







        #--------------------------------------------------admin group code end-------------------------------------------------------------





        # admin pannel code start
        def close():
              t.destroy()    
            
        # design  
          
        c1=Canvas(t,width=1600,height=700,bg='white',)
        c1.place(x=0,y=0)
        ca=Canvas(t,width=1600,height=60,bg='royal blue',)
        ca.place(x=0,y=0)
        cb=Canvas(t,width=1600,height=100,bg='white')
        cb.place(x=0,y=50)
        cd=Canvas(t,width=200,height=400,bg='royal blue')
        cd.place(x=10,y=200)
        cda=Label(t,text='ADMIN',font=('Arial black',18),bg='royal blue',foreground='white')
        cda.place(x=50,y=210)
        cdbutton1=Button(t,text="INSERT",width=14,height=2,font=('Arial black',10),bg='white', command=admini)
        cdbutton1.place(x=30,y=270)
        cdbutton2=Button(t,text="UPDATE",width=14,height=2,font=('Arial black',10),bg='white',command=adminu)
        cdbutton2.place(x=30,y=330)
        cdbutton3=Button(t,text="FIND",width=14,height=2,font=('Arial black',10),bg='white',command=adminf)
        cdbutton3.place(x=30,y=390)
        cdbutton4=Button(t,text="CHECK",width=14,height=2,font=('Arial black',10),bg='white',command=admins)
        cdbutton4.place(x=30,y=450)
        cdbutton5=Button(t,text="DELETE",width=14,height=2,font=('Arial black',10),bg='white',command=admind)
        cdbutton5.place(x=30,y=510)


        ce=Canvas(t,width=200,height=400,bg='royal blue')
        ce.place(x=230,y=200)
        cea=Label(t,text='USER',font=('Arial black',18),bg='royal blue',foreground='white')
        cea.place(x=275,y=210)
        cebutton1=Button(t,text="INSERT",width=14,height=2,font=('Arial black',10),bg='white',command=useri)
        cebutton1.place(x=265,y=270)
        cebutton2=Button(t,text="UPDATE",width=14,height=2,font=('Arial black',10),bg='white',command=useru)
        cebutton2.place(x=265,y=330)
        cebutton3=Button(t,text="FIND",width=14,height=2,font=('Arial black',10),bg='white',command=userf)
        cebutton3.place(x=265,y=390)
        cebutton4=Button(t,text="CHECK",width=14,height=2,font=('Arial black',10),bg='white',command=users)
        cebutton4.place(x=265,y=450)
        cebutton5=Button(t,text="DELETE",width=14,height=2,font=('Arial black',10),bg='white',command=userd)
        cebutton5.place(x=265,y=510)





        cf=Canvas(t,width=200,height=400,bg='royal blue')
        cf.place(x=460,y=200)
        cfa=Label(t,text='WARD',font=('Arial black',18),bg='royal blue',foreground='white')
        cfa.place(x=500,y=210)
        cfbutton1=Button(t,text="INSERT",width=14,height=2,font=('Arial black',10),bg='white',command=wardi)
        cfbutton1.place(x=485,y=270)
        cfbutton2=Button(t,text="UPDATE",width=14,height=2,font=('Arial black',10),bg='white',command=wardu)
        cfbutton2.place(x=485,y=330)
        cfbutton3=Button(t,text="FIND",width=14,height=2,font=('Arial black',10),bg='white',command=wardf)
        cfbutton3.place(x=485,y=390)
        cfbutton4=Button(t,text="CHECK",width=14,height=2,font=('Arial black',10),bg='white',command=wards)
        cfbutton4.place(x=485,y=450)
        cfbutton5=Button(t,text="DELETE",width=14,height=2,font=('Arial black',10),bg='white',command=wardd)
        cfbutton5.place(x=485,y=510)






        cg=Canvas(t,width=200,height=400,bg='royal blue')
        cg.place(x=690,y=200)
        cga=Label(t,text='CANDIDATE',font=('Arial black',18),bg='royal blue',foreground='white')
        cga.place(x=715,y=210)
        cgbutton1=Button(t,text="INSERT",width=14,height=2,font=('Arial black',10),bg='white',command=cani)
        cgbutton1.place(x=725,y=270)
        cgbutton2=Button(t,text="UPDATE",width=14,height=2,font=('Arial black',10),bg='white',command=canu)
        cgbutton2.place(x=725,y=330)
        cgbutton3=Button(t,text="FIND",width=14,height=2,font=('Arial black',10),bg='white',command=canf)
        cgbutton3.place(x=725,y=390)
        cgbutton4=Button(t,text="CHECK",width=14,height=2,font=('Arial black',10),bg='white',command=cans)
        cgbutton4.place(x=725,y=450)
        cgbutton5=Button(t,text="DELETE",width=14,height=2,font=('Arial black',10),bg='white',command=cand)
        cgbutton5.place(x=725,y=510)








        ch=Canvas(t,width=200,height=400,bg='royal blue')
        ch.place(x=920,y=200)
        cha=Label(t,text='SCHEDULE',font=('Arial black',18),bg='royal blue',foreground='white')
        cha.place(x=950,y=210)
        chbutton1=Button(t,text="INSERT",width=14,height=2,font=('Arial black',10),bg='white',command=schi)
        chbutton1.place(x=960,y=270)
        chbutton2=Button(t,text="UPDATE",width=14,height=2,font=('Arial black',10),bg='white',command=schu)
        chbutton2.place(x=960,y=330)
        chbutton3=Button(t,text="FIND",width=14,height=2,font=('Arial black',10),bg='white',command=schf)
        chbutton3.place(x=960,y=390)
        chbutton4=Button(t,text="CHECK",width=14,height=2,font=('Arial black',10),bg='white',command=schs)
        chbutton4.place(x=960,y=450)
        chbutton5=Button(t,text="DELETE",width=14,height=2,font=('Arial black',10),bg='white',command=schd)
        chbutton5.place(x=960,y=510)







        ci=Canvas(t,width=200,height=400,bg='royal blue')
        ci.place(x=1140,y=200)
        cia=Label(t,text='VOTING',font=('Arial black',18),bg='royal blue',foreground='white')
        cia.place(x=1190,y=210)
        cibutton1=Button(t,text="INSERT",width=14,height=2,font=('Arial black',10),bg='white',command=votei)
        cibutton1.place(x=1170,y=270)
        cibutton2=Button(t,text="UPDATE",width=14,height=2,font=('Arial black',10),bg='white',command=voteu)
        cibutton2.place(x=1170,y=330)
        cibutton3=Button(t,text="FIND",width=14,height=2,font=('Arial black',10),bg='white',command=votef)
        cibutton3.place(x=1170,y=390)
        cibutton4=Button(t,text="CHECK",width=14,height=2,font=('Arial black',10),bg='white',command=votes)
        cibutton4.place(x=1170,y=450)
        cibutton5=Button(t,text="DELETE",width=14,height=2,font=('Arial black',10),bg='white',command=voted)
        cibutton5.place(x=1170,y=510)

        result=Button(t,text='RESULT',width=12,font=('Arial black',12),bg='royal blue',foreground='white',command=results)
        result.place(x=1180,y=157)





        sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
        sa.place(x=30,y=70)
        sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
        sb.place(x=30,y=95)
        sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
        sc.place(x=1000,y=65)
        sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
        sd.place(x=30,y=10)
        se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
        se.place(x=1100,y=5)
        sf=Label(t,text='ADMIN PANEL',font=('Arial black',18),bg='white',foreground='royal blue')
        sf.place(x=550,y=110)






        #footer
        cd=Canvas(t,width=1600,height=150,bg='royal blue',)
        cd.place(x=0,y=600)
        sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
        sg.place(x=20,y=620)
        sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
        sh.place(x=1000,y=620)

        # admin pannel code end
       
        
        
        
        
    # admin pannel code end here




























    # admin register code start here

    def adminregister():
        t=tkinter.Tk()
        t.geometry('1600x800')
        t.title('insert data')


        # functions
        def insertdata():
            db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
            cur=db.cursor()
            xb=b.get()
            xd=d.get()
            xf=f.get()
            xh=h.get()
            xj=int(j.get())
            sql="insert into admin values('%s','%s','%s','%s',%d)"%(xb,xd,xf,xh,xj)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('Save','successfully register')
            t.destroy()
            b.delete(0,100)
            d.delete(0,100)
            f.delete(0,100)
            h.delete(0,100)
            j.delete(0,100)

        def close():
              t.destroy()    
            
        # design    
        c1=Canvas(t,width=1600,height=700,bg='white',)
        c1.place(x=0,y=0)
        ca=Canvas(t,width=1600,height=60,bg='royal blue',)
        ca.place(x=0,y=0)
        cb=Canvas(t,width=1600,height=100,bg='white')
        cb.place(x=0,y=50)
        cd=Canvas(t,width=250,height=520,bg='royal blue')
        cd.place(x=0,y=150)
        sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
        sa.place(x=30,y=70)
        sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
        sb.place(x=30,y=95)
        sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
        sc.place(x=1000,y=65)
        sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
        sd.place(x=30,y=10)
        se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
        se.place(x=1100,y=5)
        sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
        sf.place(x=400,y=550)

        #form work
        a=Label(t,text='Admin id:-',font=('Agency FB',16),bg='white')
        a.place(x=400,y=180)
        b=Entry(t,width=80,relief="solid")
        b.place(x=480,y=185)
        c=Label(t,text='Password:-',font=('Agency FB',16),bg='white')
        c.place(x=400,y=230)
        d=Entry(t,width=80,relief="solid",show='*')
        d.place(x=480,y=230)
        e=Label(t,text='Name:-',font=('Agency FB',16),bg='white')
        e.place(x=400,y=270)
        f=Entry(t,width=80,relief="solid")
        f.place(x=480,y=270)
        g=Label(t,text='Email:-',font=('Agency FB',16),bg='white')
        g.place(x=400,y=320)
        h=Entry(t,width=80,relief="solid")
        h.place(x=480,y=320)
        i=Label(t,text='Phone:-',font=('Agency FB',16),bg='white')
        i.place(x=400,y=370)
        j=Entry(t,width=80,relief="solid")
        j.place(x=480,y=370)
        b1=Button(t,text="REGISTER",width=20,height=2,font=('Arial black',10),bg='white',command=insertdata)
        b1.place(x=30,y=200)
        b2=Button(t,text="CLOSE",width=20,height=2,font=('Arial black',10),bg='white',command=close)
        b2.place(x=30,y=350)

        #footer
        cd=Canvas(t,width=1600,height=150,bg='royal blue',)
        cd.place(x=0,y=600)
        sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
        sg.place(x=20,y=620)
        sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
        sh.place(x=1000,y=620)
        
        
    # admin register code end gere
        









    # forget password codet start

    def forgetb():
        
        t=tkinter.Tk()
        t.geometry('1600x800')
        t.title('insert data')
        
        def login():
            db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
            cur=db.cursor()
            uname=int(c.get())
            password=int(e.get())
            
            sql="update admin set password=%d where adminid=%d"%(password,uname)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('save','password change successfully')
            t.destroy()
            c.delete(0,100)
            e.delete(0,100)
           
          


        c1=Canvas(t,width=1600,height=700,bg='white',)
        c1.place(x=0,y=0)
        ca=Canvas(t,width=1600,height=60,bg='royal blue',)
        ca.place(x=0,y=0)
        cb=Canvas(t,width=1600,height=100,bg='white')
        cb.place(x=0,y=50)
        cd=Canvas(t,width=1600,height=800,bg='blue')
        cd.place(x=0,y=150)
        cd=Canvas(t,width=400,height=400,bg='royal blue')
        cd.place(x=480,y=250)

        a=Label(t,text='Log In',font=('Arial black',22),bg='royal blue',foreground="white")
        a.place(x=630,y=260)
        b=Label(t,text='Admin id',font=('Arial black',14),bg='royal blue',foreground="white")
        b.place(x=520,y=350)
        c=Entry(t,width=30,relief="solid")
        c.place(x=682,y=360)

        d=Label(t,text=' New Password',font=('Arial black',13),bg='royal blue',foreground="white")
        d.place(x=520,y=425)
        e=Entry(t,width=30,relief="solid",show="*")
        e.place(x=680,y=430)

        b1=Button(t,text="Save",width=30,height=1,font=('Arial black',10),bg='blue',foreground="white",command=login)
        b1.place(x=550,y=505)



        sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
        sa.place(x=30,y=70)
        sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
        sb.place(x=30,y=95)
        sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
        sc.place(x=1000,y=65)
        sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
        sd.place(x=30,y=10)
        se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
        se.place(x=1100,y=5)

    # forget passwor code end









    def login():
        
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        uname=c.get()
        password=e.get()
        sql="select * from admin where adminid=%s and password=%s"
        cur.execute(sql,[(uname),(password)])
        result=cur.fetchall()
        if result:
            messagebox.showinfo('log in','login success')
            t.destroy()
            adminpannel()
            
        else:
            messagebox.showinfo('incorrect','enter correct details')
            t.destroy()
            
            
            
            
      


    c1=Canvas(t,width=1600,height=700,bg='white',)
    c1.place(x=0,y=0)
    ca=Canvas(t,width=1600,height=60,bg='royal blue',)
    ca.place(x=0,y=0)
    cb=Canvas(t,width=1600,height=100,bg='white')
    cb.place(x=0,y=50)
    cd=Canvas(t,width=1600,height=800,bg='blue')
    cd.place(x=0,y=150)
    cd=Canvas(t,width=400,height=400,bg='royal blue')
    cd.place(x=480,y=250)

    a=Label(t,text='Log In',font=('Arial black',22),bg='royal blue',foreground="white")
    a.place(x=630,y=260)
    b=Label(t,text='Admin id',font=('Arial black',14),bg='royal blue',foreground="white")
    b.place(x=520,y=350)
    c=Entry(t,width=30,relief="solid")
    c.place(x=640,y=360)

    d=Label(t,text='Password',font=('Arial black',14),bg='royal blue',foreground="white")
    d.place(x=520,y=425)
    e=Entry(t,width=30,relief="solid",show="*")
    e.place(x=640,y=425)
    f=Button(t,text='forget password',font=('Arial black',8),bg='blue',foreground="white",command=forgetb)
    f.place(x=550,y=480)
    b1=Button(t,text="Log In",width=30,height=1,font=('Arial black',10),bg='blue',foreground="white",command=login)
    b1.place(x=550,y=505)

    b3=Button(t,text="register",width=30,height=1,font=('Arial black',10),bg='blue',foreground="white",command=adminregister)
    b3.place(x=550,y=560)


    sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
    sa.place(x=30,y=70)
    sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
    sb.place(x=30,y=95)
    sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
    sc.place(x=1000,y=65)
    sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
    sd.place(x=30,y=10)
    se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
    se.place(x=1100,y=5)




    
    






















#---------------------------------------------------ADMIN GROUP ALL SCREEN CODE END--------------------------------------------#











#-------------------------------------------------------USER  GROUP ALL SCREEN CODE START---------------------------------------------#

















t=tkinter.Tk()
t.geometry('1600x800')
t.title('Election commision of india')

def forget():
    
    t=tkinter.Tk()
    t.geometry('1600x800')
    t.title('forget password')
    
    def login():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        uname=int(c.get())
        password=int(e.get())
        
        sql="update users set password=%d where userid=%d"%(password,uname)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('save','password change successfully')
        t.destroy()
        c.delete(0,100)
        e.delete(0,100)
       
      


    c1=Canvas(t,width=1600,height=700,bg='white',)
    c1.place(x=0,y=0)
    ca=Canvas(t,width=1600,height=60,bg='royal blue',)
    ca.place(x=0,y=0)
    cb=Canvas(t,width=1600,height=100,bg='white')
    cb.place(x=0,y=50)
    cd=Canvas(t,width=1600,height=800,bg='blue')
    cd.place(x=0,y=150)
    cd=Canvas(t,width=400,height=400,bg='royal blue')
    cd.place(x=480,y=250)

    a=Label(t,text='Log In',font=('Arial black',22),bg='royal blue',foreground="white")
    a.place(x=630,y=260)
    b=Label(t,text='User id',font=('Arial black',14),bg='royal blue',foreground="white")
    b.place(x=520,y=350)
    c=Entry(t,width=30,relief="solid")
    c.place(x=682,y=360)

    d=Label(t,text=' New Password',font=('Arial black',13),bg='royal blue',foreground="white")
    d.place(x=520,y=425)
    e=Entry(t,width=30,relief="solid",show="*")
    e.place(x=680,y=430)

    b1=Button(t,text="Save",width=30,height=1,font=('Arial black',10),bg='blue',foreground="white",command=login)
    b1.place(x=550,y=505)



    sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
    sa.place(x=30,y=70)
    sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
    sb.place(x=30,y=95)
    sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
    sc.place(x=1000,y=65)
    sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
    sd.place(x=30,y=10)
    se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
    se.place(x=1100,y=5)

# forget passwor code end




















# end screen code start

def end():
    t=tkinter.Tk()
    t.geometry('1600x800')
    t.title('End screen')
    def des():
        t.destroy()

    # design    
    c1=Canvas(t,width=1600,height=700,bg='white',)
    c1.place(x=0,y=0)
    ca=Canvas(t,width=1600,height=60,bg='royal blue',)
    ca.place(x=0,y=0)
    cb=Canvas(t,width=1600,height=100,bg='white')
    cb.place(x=0,y=50)
    sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
    sa.place(x=30,y=70)
    sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
    sb.place(x=30,y=95)
    sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
    sc.place(x=1000,y=65)
    sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
    sd.place(x=30,y=10)
    se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
    se.place(x=1100,y=5)
    sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
    sf.place(x=20,y=550)

    a=Label(t,text='Thank you for your vote',font=('arial black',30),bg='white',foreground='royal blue')
    a.place(x=400,y=250)
    b1=Button(t,text="Exit",width=15,height=2,font=('Bernard MT Condensed',14),bg='royal blue',foreground="white",command=des)
    b1.place(x=600,y=350)
    


# end screen code end





    #footer
    cd=Canvas(t,width=1600,height=150,bg='royal blue',)
    cd.place(x=0,y=600)
    sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
    sg.place(x=20,y=620)
    sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
    sh.place(x=1000,y=620)












# voting screen code start

def give():
    
    t=tkinter.Tk()
    t.geometry('1600x800')
    t.title('Election commision of india')
    
    
    
    



    i=0
    xa=[]
    count=0

    def filldata():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        sql="select userid from userlogin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[-1])
           
            global count
            count=count+1
        db.close()
    def showfirst():
        global i
        i=0
        f.delete(0,100)
        f.insert(0,xa[-1])
        
    def check():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        uname=f.get()
        sql="select userid from votings where userid=%s"
        cur.execute(sql,[(uname)])
        result=cur.fetchall()
        if result:
            messagebox.showerror('sorry','you are already give the vote')
            t.destroy()
        else:
            messagebox.showin('sorry','you are already give the vote')
            
            
            


    
        




    elist=[]
    def fill():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        sql="select canid from candidates"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            elist.append(res[0])
        db.close
        
    elistb=[]
    def fillb():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        sql="select wardno from wards"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            elistb.append(res[0])
        db.close
        
        
        
        

        
            

    def insertdata():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
       
        xd=int(d.get())
        xf=int(f.get())
        xh=int(h.get())
        sql="insert into votings (canid,userid,wardno) values(%d,%d,%d)"%(xd,xf,xh)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('successfully','vote save successfully')
        t.destroy()
        end()
        b.delete(0,100)
        d.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)
        j.delete(0,100)
        l.delete(0,100)
        


            
    def close():
          t.destroy()
            
        
    def dis():
        f.config(state='disabled')
    # design    
    c1=Canvas(t,width=1600,height=700,bg='white',)
    c1.place(x=0,y=0)
    ca=Canvas(t,width=1600,height=60,bg='royal blue',)
    ca.place(x=0,y=0)
    cb=Canvas(t,width=1600,height=100,bg='white')
    cb.place(x=0,y=50)
    sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
    sa.place(x=30,y=70)
    sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
    sb.place(x=30,y=95)
    sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
    sc.place(x=1000,y=65)
    sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
    sd.place(x=30,y=10)
    se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
    se.place(x=1100,y=5)
    sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
    sf.place(x=20,y=550)


    heading=Label(t,text='Give your important vote',font=('Agency FB',25),bg='white',fg='royal blue')
    heading.place(x=450,y=100)
    c=Label(t,text='Cand Id',font=('Agency FB',16),bg='white')
    c.place(x=300,y=215)
    d=ttk.Combobox(t,width=77)
    fill()
    d['values']=elist
    d.place(x=400,y=220)
    e=Label(t,text='User Id',font=('Agency FB',16),bg='white')
    e.place(x=300,y=265)
    f=Entry(t,width=80,relief="solid")
    f.place(x=400,y=270)
    g=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
    g.place(x=300,y=315)
    h=ttk.Combobox(t,width=77)
    fillb()
    h['values']=elistb
    h.place(x=400,y=320)

    b1=Button(t,text="Save",font=('Bernard MT Condensed',14),command=insertdata,bg='royal blue')
    b1.place(x=500,y=370)
    b2=Button(t,text="Close",font=('Bernard MT Condensed',14),bg='royal blue',command=close)
    b2.place(x=600,y=370)


    #footer
    cd=Canvas(t,width=1600,height=150,bg='royal blue',)
    cd.place(x=0,y=600)
    sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
    sg.place(x=20,y=620)
    sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
    sh.place(x=1000,y=620)
    filldata()
    showfirst()
    dis()
    check()
    


# voting screen code end







# user register screen code start

def raj():
    t=tkinter.Tk()
    t.geometry('1600x800')
    t.title('registration')


    xa=[]
    i=0
    count=0


        
        
    def insertdata():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        xb=int(b.get())
        xbd=int(bd.get())
        xd=d.get()
        xf=f.get()
        xh=int(h.get())
        xj=j.get()
        xl=int(l.get())
        sql="insert into users values(%d,%d,'%s','%s',%d,'%s',%d)"%(xb,xbd,xd,xf,xh,xj,xl)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('register','register successfully')
        t.destroy()
        b.delete(0,100)
        bd.delete(0,100)
        d.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)
        j.delete(0,100)
        l.delete(0,100)
    
        
        
          

    def filldata():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        sql="select userid from users"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            global count
            count=count+1
        db.close()
        
    def showfirst():
        global i
        i=0
        b.delete(0,100)
        b.insert(0,xa[-1]+1)
        
       


            
    def close():
          t.destroy()

            
    def dis():
        b.config(state='disabled')    

    # design    
    c1=Canvas(t,width=1600,height=700,bg='white',)
    c1.place(x=0,y=0)
    ca=Canvas(t,width=1600,height=60,bg='royal blue',)
    ca.place(x=0,y=0)
    cb=Canvas(t,width=1600,height=100,bg='white')
    cb.place(x=0,y=50)
    cd=Canvas(t,width=250,height=520,bg='royal blue')
    cd.place(x=0,y=150)
    sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
    sa.place(x=30,y=70)
    sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
    sb.place(x=30,y=95)
    sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
    sc.place(x=1000,y=65)
    sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
    sd.place(x=30,y=10)
    se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
    se.place(x=1100,y=5)
    sf=Label(t,text="Note:-   Please Enter Detail Carefully",font=('Arial Unicode MS',10),bg='white')
    sf.place(x=300,y=550)


    a=Label(t,text='User id',font=('Agency FB',16),bg='white')
    a.place(x=400,y=160)
    b=Entry(t,width=80,relief="solid")
    b.place(x=500,y=165)
    
    bc=Label(t,text='Password',font=('Agency FB',16),bg='white')
    bc.place(x=400,y=215)
    bd=Entry(t,width=80,relief="solid")
    bd.place(x=500,y=220)
    c=Label(t,text='Name',font=('Agency FB',16),bg='white')
    c.place(x=400,y=260)
    d=Entry(t,width=80,relief="solid")
    d.place(x=500,y=265)
    e=Label(t,text='Address',font=('Agency FB',16),bg='white')
    e.place(x=400,y=310)
    f=Entry(t,width=80,relief="solid")
    f.place(x=500,y=315)
    g=Label(t,text='Phone',font=('Agency FB',16),bg='white')
    g.place(x=400,y=360)
    h=Entry(t,width=80,relief="solid")
    h.place(x=500,y=365)
    i=Label(t,text='Email',font=('Agency FB',16),bg='white')
    i.place(x=400,y=410)
    j=Entry(t,width=80,relief="solid")
    j.place(x=500,y=415)
    k=Label(t,text='Ward No',font=('Agency FB',16),bg='white')
    k.place(x=400,y=460)
    l=Entry(t,width=80,relief="solid")
    l.place(x=500,y=465)
    b1=Button(t,text="REGISTER",width=20,height=2,font=('Arial black',10),bg='white',command=insertdata)
    b1.place(x=30,y=200)
    b2=Button(t,text="CLOSE",width=20,height=2,font=('Arial black',10),bg='white',command=close)
    b2.place(x=30,y=350)
    filldata()
    showfirst()
    dis()

    #footer
    cd=Canvas(t,width=1600,height=150,bg='royal blue',)
    cd.place(x=0,y=600)
    sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
    sg.place(x=20,y=620)
    sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
    sh.place(x=1000,y=620)

# user register screen code End





# login  screen code start


def loginaccess():
    
    t=tkinter.Tk()
    t.geometry('1600x800')
    t.title('registration')
    
    
    def insertid():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        xb=int(c.get())
        sql="insert into userlogin(userid) values(%s)"
        cur.execute(sql,[(xb)])
        db.commit()
       
    
    
        
      
    
    
    
    
    def message():
        messagebox.showinfo('incorrect','enter correct details')

    def login():
        db=pymysql.connect(host="localhost",user="root",password="root",database="testdb")
        cur=db.cursor()
        uname=c.get()
        password=e.get()
        sql="select * from users where userid=%s and password=%s"
        cur.execute(sql,[(uname),(password)])
        result=cur.fetchall()
        insertid()
        if result:
            messagebox.showinfo('log in','login success')
            t.destroy()
            give()
            
            
        else:
            message()
            t.destroy()
            loginaccess()
        
            
            
            
      
    
    
    
    c1=Canvas(t,width=1600,height=700,bg='white',)
    c1.place(x=0,y=0)
    ca=Canvas(t,width=1600,height=60,bg='royal blue',)
    ca.place(x=0,y=0)
    cb=Canvas(t,width=1600,height=100,bg='white')
    cb.place(x=0,y=50)
    cd=Canvas(t,width=1600,height=800,bg='blue')
    cd.place(x=0,y=150)
    cd=Canvas(t,width=400,height=400,bg='royal blue')
    cd.place(x=480,y=250)
    
    a=Label(t,text='Log In',font=('Arial black',22),bg='royal blue',foreground="white")
    a.place(x=630,y=260)
    b=Label(t,text='User id',font=('Arial black',14),bg='royal blue',foreground="white")
    b.place(x=520,y=350)
    c=Entry(t,width=30,relief="solid")
    c.place(x=640,y=360)
    
    d=Label(t,text='Password',font=('Arial black',14),bg='royal blue',foreground="white")
    d.place(x=520,y=425)
    e=Entry(t,width=30,relief="solid",show="*")
    e.place(x=640,y=430)
    f=Button(t,text="forget password",width=13,height=0,font=('Arial black',8),bd=0,bg='royal blue',foreground="white",command=forg)
    f.place(x=555,y=475)
    b1=Button(t,text="Log In",width=30,height=1,font=('Arial black',10),bg='blue',foreground="white",command=login)
    b1.place(x=550,y=505)
    b2=Button(t,text="register",width=30,height=1,font=('Arial black',10),bg='blue',foreground="white",command=raj)
    b2.place(x=550,y=560)
    
    
    sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
    sa.place(x=30,y=70)
    sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
    sb.place(x=30,y=95)
    sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
    sc.place(x=1000,y=65)
    sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
    sd.place(x=30,y=10)
    se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
    se.place(x=1100,y=5)
    

# login  screen code End















# main pannel code start

# design    
c1=Canvas(t,width=1600,height=700,bg='white',)
c1.place(x=0,y=0)
ca=Canvas(t,width=1600,height=60,bg='royal blue',)
ca.place(x=0,y=0)
cb=Canvas(t,width=1600,height=100,bg='white')
cb.place(x=0,y=50)
sa=Label(t,text='भारत निर्वाचन आयोग' ,font=('Agency FB',14) ,bg='white')
sa.place(x=30,y=70)
sb=Label(t,text='Election Commision of india' ,font=('Arial Unicode MS',14) ,bg='white')
sb.place(x=30,y=95)
sc=Label(t,text='वन्दे मातरम्' ,font=('Arial Unicode MS',35) ,bg='white')
sc.place(x=1000,y=65)
sd=Label(t,text="WELCOME TO INDIA VOTING PORTAL",foreground="white", bg='royal blue',font=('Arial Unicode MS',14))
sd.place(x=30,y=10)
se=Label(t,text="INDIA",foreground="white", bg='royal blue',font=('Bodoni MT Black',25))
se.place(x=1100,y=5)


a=Canvas(t,width=300,height=400,bg='royal blue',)
a.place(x=250,y=180)
al=Label(t,text='ADMIN',font=('Arial Black',25),bg='royal blue',foreground="white")
al.place(x=330,y=220)
buttona=Button(t,text='ADMIN',width=15,height=5,font=('Arial Black',14),bg='white',foreground="royal blue",command=adminscreen)
buttona.place(x=300,y=320)
b=Canvas(t,width=300,height=400,bg='royal blue',)
b.place(x=800,y=180)
bl=Label(t,text='USER',font=('Arial Black',25),bg='royal blue',foreground="white")
bl.place(x=890,y=220)
buttonb=Button(t,text='USER',width=15,height=5,font=('Arial Black',14),bg='white',foreground="royal blue",command=loginaccess)
buttonb.place(x=850,y=320)

    



#footer
cd=Canvas(t,width=1600,height=150,bg='royal blue',)
cd.place(x=0,y=600)
sg=Label(t,text="PROUD TO BE INDIAN",foreground="white", bg='royal blue',font=('Bodoni MT Black',20))
sg.place(x=20,y=620)
sh=Label(t,text="© Copyright Election Commission of India",foreground="white", bg='royal blue',font=('Arial',10))
sh.place(x=1000,y=620)

# main pannel code end






t.mainloop()
   
