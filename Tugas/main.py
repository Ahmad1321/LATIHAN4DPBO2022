from time import sleep
from person import person
from ship import ship
from airplane import airplane
import array as arr

#List data manusia
data = person()
data.setname("Ali")
data.setgender(1)
data.setNIK(10001) 
data.setNIP(20001)
data.setcompany("UPI")
data.setposisition("Mahasiswa")
data.setid(30001)
data.setactive("20 Desember 2022")
data.settype("Kapal01")

data1 = person()
data1.setname("Adi")
data1.setgender(1)
data1.setNIK(10002)
data1.setNIP(20002)
data1.setcompany("UPI")
data1.setposisition("Mahasiswa")
data1.setid(30002)
data1.setactive("21 Desember 2022")
data1.settype("Kapal02")

data2 = person()
data2.setname("Dina")
data2.setgender(2)
data2.setNIK(10003)
data2.setNIP(20003)
data2.setcompany("UPI")
data2.setposisition("Mahasiswa")
data2.setid(30003)
data2.setactive("23 Desember 2022")
data2.settype("Pesawat01")

data3 = person()
data3.setname("Diah")
data3.setgender(2)
data3.setNIK(10004)
data3.setNIP(20004)
data3.setcompany("UPI")
data3.setposisition("Mahasiswa")
data3.setid(30004)
data3.setactive("20 Desember 2022")
data3.settype("Pesawat04")

data4 = person()
data4.setname("Aman")
data4.setgender(1)
data4.setNIK(10005)
data4.setNIP(20005)
data4.setcompany("UPI")
data4.setposisition("Mahasiswa")
data4.setid(30005)
data4.setactive("20 Desember 2022")
data4.settype("Kapal05")

listperson = [data,data1,data2,data3,data4]

#List data kapal
kapal1 = ship()
kapal1.settype("Kapal01")
kapal1.setage(5)
kapal1.setcountry("Indonesia")
kapal1.setftype("Fuel01")
kapal1.setmax(250)

kapal2 = ship()
kapal2.settype("Kapal02")
kapal2.setage(3)
kapal2.setcountry("Indonesia")
kapal2.setftype("Fuel01")
kapal2.setmax(200)

kapal3 = ship()
kapal3.settype("Kapal03")
kapal3.setage(7)
kapal3.setcountry("Inggris")
kapal3.setftype("Fuel01")
kapal3.setmax(300)

kapal4 = ship()
kapal4.settype("Kapal04")
kapal4.setage(6)
kapal4.setcountry("Indonesia")
kapal4.setftype("Fuel02")
kapal4.setmax(275)

kapal5 = ship()
kapal5.settype("Kapal05")
kapal5.setage(3)
kapal5.setcountry("Jerman")
kapal5.setftype("Fuel02")
kapal5.setmax(200)

listship = [kapal1,kapal2,kapal3,kapal4,kapal5]

#List Pesawat
air1 = airplane()
air1.settype("Pesawat01")
air1.setage(20)
air1.setlen(500)
air1.setftype("Fuel03")
air1.setmax(150)

air2 = airplane()
air2.settype("Pesawat02")
air2.setage(21)
air2.setlen(550)
air2.setftype("Fuel03")
air2.setmax(155)

air3 = airplane()
air3.settype("Pesawat03")
air3.setage(10)
air3.setlen(700)
air3.setftype("Fuel04")
air3.setmax(180)

air4 = airplane()
air4.settype("Pesawat04")
air4.setage(5)
air4.setlen(850)
air4.setftype("Fuel04")
air4.setmax(195)

air5 = airplane()
air5.settype("Pesawat05")
air5.setage(20)
air5.setlen(500)
air5.setftype("Fuel03")
air5.setmax(100)

listairplane = [air1,air2,air3,air4,air5]

#Looping untuk print
x=1
for i in range(5):
    print()
    print("======================")
    print("Data ke-" + str(x))
    listperson[i].printperson()
    if(i%2==0):
        listperson[i].sleep()
    x = x + 1
    for j in range(5):
        #Kondisi jika tipe kendaraan person sama dengan tipe vehicle
        #Maka akan diprint vehiclenya
        if(listperson[i].gettype() == listairplane[j].gettype()):
            listairplane[j].printairplane()
        elif(listperson[i].gettype() == listship[j].gettype()):
            listship[j].printship()    





