class driver():
    __id = 0
    __active = ""
    __type = ""

    # construct
    def __init__(self, id = 0, active = "", type = ""):
        self.__id = id
        self.__active = active
        self.__type = type

    # set dan get
    def setid(self, id):
        self.__id = id

    def getid(self):
        return self.__id
    
    def setactive(self, active):
        self.__active = active
    
    def getactive(self):
        return self.__active

    def settype(self, type):
        self.__type = type
    
    def gettype(self):
        return self.__type

    # output
    def printdriver(self):
        print("-------------------------------")
        print("Driver")
        print("id : " + str(self.__id))
        print("active : " + str(self.__active))
        print("type : " + str(self.__type))