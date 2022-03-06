from vehicle import vehicle

class ship(vehicle):
    __age = 0
    __type = ""
    __country = ""

    # construct
    def __init__(self, age = 0, type = "", country = ""):
        self.__age = age
        self.__type = type
        self.__country = country

    # set dan get
    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age
    
    def settype(self, type):
        self.__type = type
    
    def gettype(self):
        return self.__type

    def setcountry(self, country):
        self.__country = country
    
    def getcountry(self):
        return self.__country

    # output
    def printship(self):
        print("-------------------------------")
        print("Kapal", end=" ") 
        vehicle.move(self)
        print("age : " + str(self.__age))
        print("type : " + str(self.__type))
        print("country : " + str(self.__country))
        vehicle.printvehicle(self)