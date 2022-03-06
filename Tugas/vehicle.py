class vehicle():
    __ftype = ""
    __max = ""

    # construct
    def __init__(self, ftype = "", max = ""):
        self.__ftype = ftype
        self.__max = max

    # set dan get
    def setftype(self, ftype):
        self.__ftype = ftype

    def getftype(self):
        return self.__ftype
    
    def setmax(self, max):
        self.__max = max
    
    def getmax(self):
        return self.__max

    def move(self):
        print("Mesin Bergerak")

    # output
    def printvehicle(self):
        print("-------------------------------")
        print("Mesin")
        print("fueltype : " + str(self.__ftype))
        print("max : " + str(self.__max))