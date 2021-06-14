from IDGenerator import IDGenerator


class Package:
    def __init__(self, bmi, facilities):
        self.__bmi = bmi
        self.__facilities = facilities
        self.__packageId = IDGenerator.generateCustomerID()

    def setBMI(self, bmi):
        self.__bmi = bmi

    def getBMI(self):
        return self.__bmi

    def setFacilities(self, facilities):
        self.__facilities = facilities

    def getFacilities(self):
        return self.__facilities

    def getPackageId(self):
        return self.__packageId

    def __str__(self):
        return self.getType()+"\n"+self.getFacilities()+"\n"+str(self.getPackageId())