#class vs object
class Server:
    def __init__(self, ip, region):
        self.ip = ip
        self.region = region
        self.status = "STOPPED"

    def start(self):
        self.status = "RUNNING"

    def stop(self):
        self.status = "STOPPED"
s1 = Server("10.0.0.1", "Mumbai")
s2 = Server("10.0.0.2", "Delhi")

s1.start() # calling instance method using class name
Server.start(s1) 
print(s1.status)

# Demonstration of class vs. instance variables in Python
class CloudServer:
    provider = "AWS"
    def __init__(self, name):
        self.name = name
a = CloudServer("api-server")
b = CloudServer("db-server")
print(a.provider)
print(b.provider)
CloudServer.provider = "Azure"
print(CloudServer.provider)
print(a.provider)
print(b.provider)

# Demonstration of private variables using name mangling in Python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # This will raise an AttributeError
#__balance → _BankAccount__balance
print(account._BankAccount__balance)  # Accessing the mangled name directly (not recommended)