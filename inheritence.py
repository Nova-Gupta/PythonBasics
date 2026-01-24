#inheritence 
class User:
    def __init__(self, email):
        self.email = email
    def login(self):
        return "User logged in"
class Admin(User):
    def __init__(self, email, level):
        super().__init__(email)
        self.level = level
    def delete_user(self):
        return "User deleted"
    def login(self):
        return "Admin logged in with 2FA"
admin = Admin("admin@example.com", "superuser")
print(admin.login())  # Output: Admin logged in with 2FA
print(admin.delete_user())  # Output: User deleted 
print(admin.email)  # Output: admin@example.com
print(admin.level)  # Output: superuser
user = User("user@example.com")
print(user.login())  # Output: User logged in
print(user.email)  # Output: user@example.com

#ClassName.__mro__
print(Admin.__mro__)  # Output: (<class '__main__.Admin'>, <class '__main__.User'>, <class 'object'>)   
# Method Resolution Order (MRO) shows the order in which base classes are searched when executing a method.
