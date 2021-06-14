import _pickle as cPickles

class GymManager:
    def __init__(self):
        self.customers = dict()
        self.packages = dict()
        self.subscriptions = dict()

    def addCustomer(self, customer):
        self.customers[customer.getCustomerId()] = customer
        self.subscriptions[customer.getCustomerId()] = dict()

    def addPackage(self, package):
        self.packages[package.getPackageId()] = package

    def addSubscription(self, customer, package, months):
        packageId = package.getPackageId()
        customerId = customer.getCustomerId()
        self.subscriptions[customerId][packageId] = months

    def delCustomer(self, customer):
        del self.customers[customer.getCustomerId()]

    def delPackage(self, package):
        del self.packages[package.getPackageId()]

    def save(self):
        cPickle.dump(self, open("gym_manager.bin", "wb"))
