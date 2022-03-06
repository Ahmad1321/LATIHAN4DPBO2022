from job import job
from driver import driver

class person(job,driver):
    __NIK = ""
    __name = ""
    __gender = True

    # construct
    def __init__(self, NIK = "", name = "", gender = True):
        self.__NIK = NIK
        self.__name = name
        self.__gender = gender

    # set dan get
    def setNIK(self, NIK):
        self.__NIK = NIK

    def getNIK(self):
        return self.__NIK
    
    def setname(self, name):
        self.__name = name
    
    def getname(self):
        return self.__name

    def setgender(self, gender):
        self.__gender = gender
    
    def getgender(self):
        return self.__gender
    
    def sleep(self):
        print()
        print("!-------------------------------!")
        print(" " + str(self.__name) + " sedang tidur")
        print("!-------------------------------!")
        print()

    # output
    def printperson(self):
        print("-------------------------------")
        print("NIK : " + str(self.__NIK))
        print("name : " + str(self.__name))
        if(self.__gender == True):
            print("Laki-laki")
        else:
            print("Perempuan")
        job.printjob(self)
        driver.printdriver(self)
        