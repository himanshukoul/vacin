import random        
import datetime
import os
import sys
import threading
import pickle
import sendingsms.send as ss
import mysql.connector as s1
from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
path = os.path.abspath("GRP.py")
direc = os.path.dirname(path)
#after backend created
t1 = open(r"{}\passw.dat".format(direc),"ab+")

try:
    t1.seek(0)
    data = pickle.load(t1)
    con = s1.connect(host="localhost", user="root", passwd="{}".format(data), charset="utf8")
    cur = con.cursor()
    cur.execute("use project;")
except:
    con = ""
    cur = ""

key = "369"
anum = 0
pnum = ""
glob_pin = 0
glob_otp = 0
glob_centre = ""
glob_id = ""
glob_date = ""
glob_time = ""

#refreshing data
try:
    cur.execute("select aadhar_no,vacindate from covitab;")
    data4 = cur.fetchall()
    for i in data4:
        format = '%Y-%m-%d'
        date1 = (datetime.datetime.strptime(i[1], format)).date()
        date2 = datetime.date.today()
        if date1 < date2:
            print("hello")
    cur.execute("update covitab set dose_confirm = 'v' where aadhar_no = '{}';".format(i[0]))
    cur.execute("update pindc set qnt = qnt + 1 where id = '{}';".format(glob_id))
            # add vaccine back to hosp.
    con.commit()

except:
    pass

class LegendWindow(Screen):
    pass

class ZerowthWindow(Screen):
    def backe(self,eye):
        global con
        global cur

        try:
            con = s1.connect(host="localhost", user="root", passwd="{}".format(eye), charset="utf8")
            cur = con.cursor()
            pickle.dump("{}".format(eye),t1)
            t1.flush()
            kappa = 1
        except:
            kappa = -1
        if kappa == 1:
            try:
                cur.execute("create database project;")
                cur.execute("use project;")                                                                                                                   #^ y or n
                cur.execute(
                "create table covitab (aadhar_nochar(12) not null,namechar(50) not null,genderchar(10) not null,pinchar(6) not null,pnochar(10) primary key,dose_no int default 1,dose_confirm char(1), vacindatechar(10),vactimechar(10),centrechar(80),cen_idchar(3),vacin_typechar(15));")
                cur.execute(
                                "create table aadhar (name char(50) not null,DOB date not null,genderchar(10) not null,aadhar_nochar(12) primary key,phonechar(10) not null,addresschar(50) not null);")
                cur.execute("create table userlogin (username char(50) not null,passwordchar(50) not null);")
                cur.execute(
                                    "create table pindc (id char(3) primary key ,pincodechar(10) ,namechar(50), qnt int default 100);")
                cur.execute(
                                    "insert into pindc(id,pincode,name) values ('001','201010','CHANDRA LAXMI HOSP.'),('002','201012','MAX HOSP.'),('003','201014','APOLLO CLINIC'),('004','201014','CHANDRA LAXMI'),('005','201016','DIVOC HEALTH'),('006','201016','SUBASH HOSP.');")

                cur.execute(
                                    "insert into aadhar values ('Ajay','2004-04-27','male','112233445566','8076797696','236B Laxman Society Indirapuram'),('Anjali','1996-08-05','female','123456789012','8802087074','12-A Freedom Society Indirapuram');")
                con.commit()
            except:
                pass

        return kappa

class FirstWindow(Screen):
    def strt(self):
        if con == "":
            bob = 0
        else:
            bob = 13
        return bob

class SecondWindow(Screen):
    def adar(self,anu):
        global anum
        anum = anu
        cur.execute("select aadhar_no from aadhar;")
        data = cur.fetchall()
        cur.execute("select aadhar_no from covitab;")
        data1 = cur.fetchall()
        if (anum,) not in data:
            x = "alpha"
        else:
            if (anum,) in data1:
                cur.execute("select dose_no,dose_confirm from covitab where aadhar_no = '{}';".format(anum))
                d = cur.fetchall()                                                            #((1,"n"))
                if d[0][0] <= 3:
                    if d[0][1] == "n":
                        x = "beta"
                    else:
                        x = "gamma"
                else:
                    x = "delta"
            else:
                x = "gamma"
        return x

class ThirdWindow(Screen):
     def do_login_user(self,logintext):
        cur.execute("select username from userlogin;")
        ua=cur.fetchall()
        if (logintext,) in ua:
            douser="loguser"
        elif (logintext,) not in ua:
            douser="notuser"
        return douser

     def do_login_pass(self,passwtext):
        cur.execute("select password from userlogin;")
        ub=cur.fetchall()
        if (passwtext,) in ub:
            dopass="logpass"
        elif (passwtext,) not in ub :
            dopass="notpass"
        return dopass

class FifthWindow(Screen):
    def pegasus(self):
        t1.close()
        sys.exit()

class SixthWindow(Screen):
    pass

class SeventhWindow(Screen):
    def arceus(self):
        cur.execute("select vacindate,centre from covitab where aadhar_no = '{}';".format(anum))
        m = cur.fetchall()
        a, b = m[0][0], m[0][1]
        self.ids.lab1.text = "urcentre is '{}' and date '{}'".format(b,a)

class SeventhdashWindow(Screen):
    pass
class EighthWindow(Screen):
    def pinchk(self,pin):
        global glob_pin
        global glob_centre
        global glob_id
        cur.execute("select * from pindc")
        data3 = cur.fetchall()
        for k in data3:
            if k[1] != pin:
                omega = -1
            else:
                omega = 1
                if k[3] == 0:                #qntatity of vac
                    omega = -1
                else:
                    glob_pin = pin
                    glob_centre = k[2]
                    glob_id = k[0]
                    break
        return omega

class AdninthWindow(Screen):
    p = StringProperty()
    q = StringProperty()
    r = StringProperty()
    s = StringProperty()
    t = StringProperty()
    u = StringProperty()
    v = StringProperty()
    def f13(self,mnum):
        global pnum
        global glob_otp
        pnum = mnum
        o = ss.sms(mnum)
        glob_otp = o
    def f15(self,otp):
        if glob_otp == int(otp):
            eta = 1
        else:
            eta = -1
        return eta
    def f45(self):
        a,b,c,d,e,f,g = datetime.datetime.now() + datetime.timedelta(days=1),datetime.datetime.now() + datetime.timedelta(days=2),datetime.datetime.now() + datetime.timedelta(days=3),datetime.datetime.now() + datetime.timedelta(days=4),datetime.datetime.now() + datetime.timedelta(days=5),datetime.datetime.now() + datetime.timedelta(days=6),datetime.datetime.now() + datetime.timedelta(days=7)
        self.p = str(a)[0:10]
        self.q = str(b)[0:10]
        self.r = str(c)[0:10]
        self.s = str(d)[0:10]
        self.t = str(e)[0:10]
        self.u = str(f)[0:10]
        self.v = str(g)[0:10]
class New1Window(Screen):
    a = StringProperty()
    b = StringProperty()
    c = StringProperty()
    d = StringProperty()
    e = StringProperty()
    f = StringProperty()
    g = StringProperty()

    def f1(self,a):
        global glob_date
        glob_date = a

class New2Window(Screen):
    pass

class New3Window(Screen):
    def f1(self,a):
        global glob_time
        glob_time = a

class New4Window(Screen):
    parrot = StringProperty()
    crow = StringProperty()
    def f7(self,q,w):
        cur.execute(
            "insert into covitab(aadhar_no,name,gender,pin,vacindate,vactime,centre,dose_confirm,cen_id,pno) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(anum,q,                                                                w,glob_pin,glob_date,glob_time,glob_centre,"n",glob_id,pnum))
        cur.execute("update pindc set qnt = qnt - 1 where id = '{}';".format(glob_id))
        #reduce vaccine from hosp.
        con.commit()

        self.parrot = q
        self.crow = glob_centre

class NinthWindow(Screen):
    tiger = StringProperty()
    lynx = StringProperty()

class TenthWindow(Screen):
    pass
phtext=0
dn=0
class CheckWindow(Screen):
    def phnoinput(self,phnotext):
        global phtext
        global dn
        phtext = phnotext
        cur.execute("select pno from covitab;")
        ac=cur.fetchall()
        if (phnotext,) in ac:
            dophno="phno_present"
        elif (phnotext,) not in ac:
            dophno="phno_notpresent"
        return dophno




def dosecheck(self):
    cur.execute("select dose_no,vacin_type from covitab where pno = '{}';".format(phtext))
    d=cur.fetchall()
    try:
        dn=d[0][0]
        dvt=d[0][1]
        if dvt==None and dn==1:
            go=1
        elif dvt!=None and dn==1:
            go=2
            return go
    except:
        pass
class EleventhWindow(Screen):
    pass
class TwelfthWindow(Screen):
    pass
class ThirteenthWindow(Screen):
    pass
class Error1Window(Screen):
    pass
class Error2Window(Screen):
    pass




class Dose1stringWindow(Screen):
    def names(self,vaccine):
        for i in ["1","2"]:
            if i != vaccine:
                allow = -1
            else:
                allow = 1
                if i == "1":
                    vaccine = "covishield"
                elif i == "2":
                    vaccine = "covaxin"
                else:
                    pass
                break
        if allow == -1:
            pass
        else:
            cur.execute("update covitab set vacin_type = '{}' where pno = '{}';".format(vaccine,phtext))
            con.commit()
        return allow

class ErrorvacnameWindow(Screen):
    pass



class MasterWindow(Screen):
    def f67(self,m):
        if m == key:
            s = +1
        else:
            s = -1
        return s

class FourteenWindow(Screen):
    def f100(self,u,p):
        cur.execute("select username from userlogin;")
        cobra = cur.fetchall()
        if len(cobra) == 0:
            air = 1
        else:
            for i in cobra:
                if i[0] == u:
                    air = -1
                    break
                else:
                    air = 1
        if not u.isalnum():
            self.ids.us.text = "enter valid username(alphanumeric only)"
        elif not p.isalnum():
            self.ids.us.text = "enter valid passwd(alphanumeric only)"
        else:
            if air == 1:
               cur.execute("insert into userlogin values ('{}','{}');".format(u,p))
               con.commit()
               self.ids.us.text = "username has been added"     
            else:
                self.ids.us.text = "already registered username"

def f101(self,u,p):
        cur.execute("select username,password from userlogin;")
        cobra = cur.fetchall()
        if len(cobra) == 0:
            gale = -1
        else:
            for i in cobra:
                if i[0] == u:
                    if i[1] == p:
                        gale = 1
                    else:
                        gale = 0                  #wrong passwd
                    break
                else:
                    gale = -1
        if gale == 1:
            cur.execute("delete from userlogin where username = '{}';".format(u))
            con.commit()
            self.ids.us.text = "username has been deleted"
        elif gale == 0:
            self.ids.us.text = "wrong passwd."
        else:
            self.ids.us.text = "no such username found"

class New5Window(Screen):
    def f99(self,a,b):
        c = int(b)
        cur.execute("update pindc set qnt = qnt + {} where id = '{}';".format(c,a))
        con.commit()
class FifteenWindow(Screen):
    pass
class CreditsWindow(Screen):
    def f109(self):
        def g1():
            self.ids.n1.text = "Himanshu Koul"
            self.ids.anchr.anchor_x = "center"
            self.ids.anchr.anchor_y = "top"
            threading.Timer(1, g2).start()
        def g2():
            self.ids.n2.text = "Varad Pandey"
            self.ids.anchr.anchor_y = "center"
            self.ids.anchr.anchor_x = "right"
            threading.Timer(1, g3).start()


        def g3():
            self.ids.n3.text = "Ayush Gupta"
            self.ids.ex.height = 0
            self.ids.ex.width = 0
            self.ids.anchr.anchor_y = "bottom"
            self.ids.anchr.anchor_x = "center"
            threading.Timer(1, g4).start()
        def g4():
            self.ids.n4.text = "Sajid Ali"
            self.ids.anchr.anchor_y = "center"
            self.ids.anchr.anchor_x = "left"
            self.ids.ex.height = 50
            self.ids.ex.width = 50
            threading.Timer(1, g5).start()
        def g5():
            self.ids.anchr.anchor_y = "center"
            self.ids.anchr.anchor_x = "center"
            self.ids.anchr.anchor_x = "left"
            threading.Timer(1,g1).start()

        def g5(self):
            print(glob_date,glob_time)
            t1.close()
            sys.exit() 




class MatchWindow(Screen):
    def gethospdetails(self):
        global hid,hcentre
        cur.execute("select cen_id,centre from covitab where pno ='{}';".format(phtext))
        try:
            hcode=cur.fetchall()
            hid=hcode[0][0]
            hcentre=hcode[0][1]
        except:
            pass
        return hid,hcentre
    hi = StringProperty()
    hc = StringProperty()
    def linkh(self):
        self.hi = str(hid)
        self.hc = str(hcentre)
    def getpindetails(self):
        global pid,pcentre
        cur.execute("select id from pindc where name ='{}';".format(hcentre))
        try:
            pcode=cur.fetchall()
            pid=pcode[0][0]
        except:
            pass
        return pid
    pi = StringProperty()
    def linkp(self):
        self.pi = str(pid)
    def doseconfirm(self):
        global dc
        cur.execute("select dose_confirm from covitab where pno = '{}';".format(phtext))
        try:
            dci=cur.fetchall()
            dc = dci[0][0]
        except:
            pass
        return dc
    dc2 = StringProperty()
    def doselink(self):
        self.dc2 = str(dc)
    def dosedeails(self):
        global t,do,da
        cur.execute("select vacin_type,dose_no,vacindate from covitab where pno = '{}';".format(phtext))
        try:
            dose=cur.fetchall()
            t = dose[0][0]
            do = dose[0][1]
            da = dose[0][2]
        except:
            pass
        return t,do,da
    t1 = StringProperty()
    do1 = StringProperty()
    da1 = StringProperty()


    def link(self):
        self.t1 = str(t)
        self.do1 = str(do)
        self.da1 = str(da)
    def dateget(self):
        cur.execute("select vacindate from covitab where pno = '{}';".format(phtext))
        dtake=cur.fetchall()
        for i in dtake:
            format = '%Y-%m-%d'
            dtable = (datetime.datetime.strptime(i[0],format)).date()
            dtoday = datetime.date.today()
            print(dtable,dtoday)
            if dtoday<dtable:
                forward=2
            elif dtoday>dtable:
                forward=3
            else:
                forward=1
        return forward
class ConfirmWindow(Screen):
    pass



class OkWindow(Screen):
    def up(self):
        cur.execute("update covitab set dose_confirm = 'y' where pno ='{}';".format(phtext))
        con.commit()
        return
class NotokWindow(Screen):
    pass
class MessageWindow(Screen):
    type_vac = StringProperty()
    dose_vac = StringProperty()
    date_vac = StringProperty()
    hcentre_vac = StringProperty()
    pid_vac = StringProperty()

class PastWindow(Screen):
    date_vac = StringProperty()
class FutureWindow(Screen):
    date_vac = StringProperty()
    def delrecord(self):
        cur.execute("delete from covitab where pno ='{}';".format(phtext))
        con.commit()
        return
class WindowManager(ScreenManager):
    pass



kv = Builder.load_file('vacin3.kv')

class vacin(App):
    def build(self):
        return kv
if __name__ == "__main__":
    vacin().run()
