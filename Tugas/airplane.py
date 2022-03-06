from vehicle import vehicle

class airplane(vehicle):
    __type = ""
    __age = 0
    __len = 0

    # construct
    def __init__(self, type = "", age = 0, len = 0):
        self.__age = age
        self.__type = type
        self.__len = len

    # set dan get
    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age
    
    def settype(self, type):
        self.__type = type
    
    def gettype(self):
        return self.__type

    def setlen(self, len):
        self.__len = len
    
    def getlen(self):
        return self.__len

    # output
    def printairplane(self):
        print("-------------------------------")
        print("Pesawat", end=" ")
        vehicle.move(self)
        print("age : " + str(self.__age))
        print("type : " + str(self.__type))
        print("length : " + str(self.__len))
        vehicle.printvehicle(self)