from GymManager import GymManager
from Customer import Customer
from Package import Package

gymManager = GymManager()
print ("\n")
print ("   *****Gym Management System*****")
print ("Hello Admin, please select a choice from the menu")


def menu():
    print ("1. Add Member")
    print ("2. Add Regimes")
    print ("3. Show all Regimes")
    print ("4. Show all Members")
    print ("5. View Member")
    print ("6. Remove Member")
    print ("7. Remove Regime")
    print ("8. Show this menu again")
    print ("\nEnter You Choice: ")

menu()

while(True):
    input = int(input())
    if input == 1:
        name = str(input("Enter Member's name - "))
        phoneNo = str(input("Enter Member's Phone No. - "))
        age = int(input("Enter Age -  "))
        gender = str(input("Enter Member's Gender - "))
        email = str(input("Enter Member's Email - "))
        bmi = float(input("Enter Member's BMI - "))
        duration = int(input("Enter Member's Duration - "))
        customer = Customer(name, phoneNo, age, gender, email, bmi, duration)
        gymManager.addCustomer(customer)

    elif input == 2:
        bmi = str(input("Enter BMI - "))
        facilities = str(input("Enter facilities - "))
        package = Package(type, facilities)
        gymManager.addPackage(package)

    elif input == 3:
        print ("PackageID\tType\tFacilities")
        for pkgId in gymManager.packages.keys():
            package = gymManager.packages[pkgId]
            packageId = pkgId
            bmi = package.getBMI()
            facilities = package.getFacilities()
            print (str(packageId) + "\t" + bmi + "\t" + facilities)

    elif input == 4:
        print ("CustomerID\tName\tPhone\tAge\tGender\tEmail\tBMI\tDuration")
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            customerId = cusId
            name = customer.getName()
            phoneNo = customer.getPhoneNo()
            age = customer.getAge()
            gender = customer.getGender()
            email = customer.getEMail()
            bmi = customer.getBMI()
            duration = customer.getDuration()
            print ((str(customerId) + "\t" + name + "\t" + phoneNo + "\t" + age + "\t" + gender + "\t" + email + "\t" + bmi + "\t" + duration))
   
    elif input == 5:
        phoneNo = str(input("Enter Member's Phone No. - "))
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getPhoneNo() == phoneNo:
                print (customer)
                customerId = cusId
                break
        if customerId == -1:
            print ("Customer with phoneNo - {0} not found".format(phoneNo))
        else:
            packageDict = gymManager.subscriptions.get(customerId)
            print ("Customer found", gymManager.customers[customerId])

    elif input == 6:
        name = str(input("Enter customer name - "))
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                gymManager.delCustomer()

    elif input == 7:
        bmi = str(input("Enter BMI - "))
        customerId = -1
        for cusId in gymManager.packages.keys():
            package = gymManager.packages[pkgId]
            if package.getBMI() == bmi:
                gymManager.delPackage()
    elif input == 8:
        menu()
    elif input == 9:
        gymManager.save()
        exit(0)
    else:
        print ("Please enter a valid number")
    menu()
