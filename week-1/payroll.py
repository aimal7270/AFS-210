class Employee:
    def __init__(self, first=None, last=None, id=None, pay=0.00):
        self.firstName = first
        self.lastName = last
        self.employeeID = id
        self.hourlyPay = pay


    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, last):
        self.lastName = last

    def getLastName(self):
        return self.lastName

    def setID(self):
        self.employeeID = id

    def getID(self, id):
        return self.employeeID 

    def setHourlyPay(self, pay):
        self.hourlyPay = pay

    def getHourlyPay(self):
        return self.hourlyPay 

    def pays(self, hoursWorked):
        if hoursWorked <= 40.0:
            return self.hourlyPay * hoursWorked
        else:
            weeklyPay = self.hourlyPay * 40
            weeklyPay += (self.hourlyPay * 1.5) * (hoursWorked - 40)
            return weeklyPay
id = int(input("Please enter your employee ID:"))
fName = input("Please enter employees first name: ")
lName = input("Please enter employees last name: ")
pay = float(input("Please enter employees hourly pay rate: "))
newEmployee = Employee(fName, lName, id, pay)
hours = float(input("How many hours did "+newEmployee.getFirstName()+"work this week? "))
print("{0} {1}'s paycheck amount is ${2:.2f}".format(newEmployee.getFirstName(),newEmployee.getLastName(),newEmployee.pays(hours)))