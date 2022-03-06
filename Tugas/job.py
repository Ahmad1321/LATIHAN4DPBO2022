class job():
    __NIP = 0
    __company = ""
    __posisition = ""

    # construct
    def __init__(self, NIP = 0, company = "", posisition = ""):
        self.__NIP = NIP
        self.__company = company
        self.__posisition = posisition

    # set dan get
    def setNIP(self, NIP):
        self.__NIP = NIP

    def getNIP(self):
        return self.__NIP
    
    def setcompany(self, company):
        self.__company = company
    
    def getcompany(self):
        return self.__company

    def setposisition(self, posisition):
        self.__posisition = posisition
    
    def getposisition(self):
        return self.__posisition

    # output
    def printjob(self):
        print("-------------------------------")
        print("Pekerjaan")
        print("NIP : " + str(self.__NIP))
        print("company : " + str(self.__company))
        print("posisition : " + str(self.__posisition))