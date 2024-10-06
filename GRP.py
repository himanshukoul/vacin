import random
import os
import sys
import pickle
import mysql.connector as s1
from kivy.app import App

from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

path = os.path.abspath("GRP.py")
direc = os.path.dirname(path)


t1 = open(r"{}\passw.txt".format(direc),"ab+")

try:
    t1.seek(0)
    data = pickle.load(t1)
    con = s1.connect(host="localhost", user="root", passwd="{}".format(data), charset="utf8")
    cur = con.cursor()
except:
    con = ""
    cur = ""
print(con)
pindc = {"201010": ("CHANDRA LAXMI HOSP.",), "201012": ("MAX HOSP.",), "201014": ("APOLLO CLINIC", "CHANDRA LAXMI"),
         "201016": ("DIVOC HEALTH", "SUBASH HOSP.")}

anum = 0


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
                cur.execute("create database nikola369;")

                cur.execute(
                "create table covitab (aadhar_no char(12) primary key,name char(50) not null,gender char(10) not null,pin char(6) not null,dose_no int default 1,reg_date datetime,vacindate datetime,centre char(80),vacin_type char(15));")
                cur.execute(
                "create table aadhar (name char(50) not null,DOB date not null,gender char(10) not null,aadhar_no char(12) primary key,phone char(10) not null,address char(50) not null);")
                cur.execute("create table userlogin (username char(50) not null,password char(50) not null);")
            except:
                pass
            cur.execute("use nikola369;")
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
                x = "beta"
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
class FourthWindow(Screen):
    pass


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
        self.ids.lab1.text = "ur centre is '{}' and time '{}'".format(b,a)


class EighthWindow(Screen):
    def pinchk(self,pin,name,gender):
        global a,b,c
        for k in list(pindc.keys()):
            if k != pin:
                omega = -1
            else:
                omega = 1
                break
        if omega == -1:
            a,b,c = 0,0,0
        else:
            cur.execute(
                "insert into covitab(aadhar_no,name,gender,pin) values('{}','{}','{}','{}');".format(anum, name,
                                                                                                     gender, pin))
            i = 0
            while i != -1:
                cur.execute("select DATE_ADD(CURRENT_TIMESTAMP,INTERVAL 2 DAY) + INTERVAL FLOOR(RAND() * 14 * 24 * 60 * 60)"
                " SECOND;")
                dat = cur.fetchall()
                date = dat[0][0]
                cur.execute("select HOUR('{}');".format(date))
                time = cur.fetchall()                       #HOUR() WILL GIVE INT TYPE
                if time[0][0] in [8,9,10,11,12,13,14,15,16,17,18,19]:
                    i = -1

            cur.execute(
                "update covitab set vacindate = '{}' where aadhar_no = '{}';".format(date,anum))
            cur.execute("update covitab set reg_date = CURRENT_TIMESTAMP;")
            rndm = random.randrange(len(pindc[pin]))
            cur.execute("update covitab set centre = '{}' where aadhar_no = '{}';".format(pindc[pin][rndm],anum))
            con.commit()
            cur.execute("select name,vacindate,centre from covitab where aadhar_no = '{}';".format(anum))
            tim = cur.fetchall()
            a = tim[0][0]
            b = tim[0][1]
            c = tim[0][2]
        return omega

    a1 = StringProperty()
    b1 = StringProperty()
    c1 = StringProperty()
    def f5(self):
        self.a1 = str(a)
        self.b1 = str(b)
        self.c1 = str(c)


class NinthWindow(Screen):
    tiger = StringProperty()
    lynx = StringProperty()
    jaguar = StringProperty()

class TenthWindow(Screen):
    pass
adtext=0
dn=0
class AadharWindow(Screen):
    def aadharinput(self,aadhartext):
        global adtext
        global dn
        adtext = aadhartext
        cur.execute("select aadhar_no from covitab;")
        ac=cur.fetchall()
        if (aadhartext,) in ac:
            doaadhar="aadhar_present"
        elif (aadhartext,) not in ac:
            doaadhar="aadhar_notpresent"
        return doaadhar
    def dosecheck(self):
        cur.execute("select dose_no from covitab where aadhar_no = '{}';".format(adtext))
        d=cur.fetchall()
        try:
            dn=d[0][0]
            return dn
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

class Dose1Window(Screen):
    name_vac = StringProperty()
    type_vac = StringProperty()
    dose_vac = StringProperty()
    date_vac = StringProperty()
    centre_vac = StringProperty()

class Dose1stringWindow(Screen):
    def names(self,vaccine):
        global n,t,do,da,c
        for i in ["1","2"]:
            if i != vaccine:
                allow = -1
            else:
                allow = 1
                if i == 1:
                    vaccine = "covishield"
                else:
                    vaccine = "covaxin"
                break
        if allow == -1:
            pass
        else:
            cur.execute("update covitab set vacin_type = '{}' where aadhar_no = '{}';".format(vaccine,adtext))
            con.commit()
        cur.execute("select name,vacin_type,dose_no,vacindate,centre from covitab where aadhar_no = '{}';".format(adtext))
        try:
            dose=cur.fetchall()
            n = dose[0][0]
            t = dose[0][1]
            do = dose[0][2]
            da = dose[0][3]
            c = dose[0][4]
        except:
            pass
        cur.execute("update covitab set vacindate = DATE_ADD(vacindate, INTERVAL 30 DAY) where aadhar_no = '{}';".format(adtext))
        cur.execute("update covitab set dose_no = 2 where aadhar_no = '{}';".format(adtext))
        con.commit()
        
        return allow 
    n1 = StringProperty()
    t1 = StringProperty()
    do1 = StringProperty()
    da1 = StringProperty()
    c1 = StringProperty()
    def link(self):
        self.n1 = str(n)
        self.t1 = str(t)
        self.do1 = str(do)
        self.da1 = str(da)
        self.c1 = str(c)

class Dose2Window(Screen):
    def abcd(self):
        global ndo,nda,nc
        cur.execute("select dose_no,vacindate,centre from covitab where aadhar_no = '{}';".format(adtext))
        try:
            dose2=cur.fetchall()
            ndo = dose2[0][0]
            nda = dose2[0][1]
            nc = dose2[0][2]
        except:
            pass
        return ndo,nda,nc
    do2 = StringProperty()
    da2 = StringProperty()
    c2 = StringProperty()
    def link2(self):
        self.do2 = str(ndo)
        self.da2 = str(nda)
        self.c2 = str(nc)
        
class Dose2stringWindow(Screen):
    dose2_vac = StringProperty()
    date2_vac = StringProperty()
    centre2_vac = StringProperty()

    
class ErrorvacnameWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('vacin.kv')


class vacin(App):
    def build(self):
        return kv

if __name__ == "__main__":
    vacin().run()


