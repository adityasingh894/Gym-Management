from IDGenerator import IDGenerator


class Customer:
    """
    Customer entity class.
    Private Attributes:
        customerID String
        name String
        phoneNo String
        Age     String
        Gender  String
        Email   String
        BMI     Float
        Duration    Int

    Public methods:
        Getters and setters
    """

    def __init__(self, name='', phoneNo='', age='', gender='', email='', bmi='', duration=''):
        self.__name = name
        self.__phoneNo = phoneNo
        self.__age = age
        self.__gender = gender
        self.__email = email
        self.__bmi = bmi
        self.__duration = duration
        self.__customerId = IDGenerator.generateCustomerID()

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPhoneNo(self, phoneNo):
        self.__phoneNo = phoneNo

    def getPhoneNo(self):
        return self.__phoneNo

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setEmail(self, email):
        self.__email = email

    def getEMail(self):
        return self.__email

    def setBMI(self, bmi):
        self.__bmi = bmi

    def getBMI(self):
        return self.__bmi

    def setDuration(self, duration):
        self.__duration = duration

    def getDuration(self):
        return self.__duration


    def getCustomerId(self):
        return self.__customerId

    def __str__(self):
        return self.getName()+"\n"+self.getPhoneNo()+"\n"+self.getAge()+"\n"+self.getGender()+"\n"+self.getEMail()+"\n"+self.getBMI()+"\n"+self.getDuration+"\n"+str(self.getCustomerId())