class MyClass:
    def __init__(self):
        self.str1 =input("Enter a string:") 
        self.n1 = int(input("Enter a integer:"))
        self.n2 = int(input("Enter a integer:"))
    def show(self):
        print("reverse:",self.str1[::-1])#string is reversed
        print("Squares of integers:",self.n1**2,self.n2**2)#printing square of the numbers
        return 
    def display(self):
        print("Length:",len(self.str1))#length of the is getting print
        print("Modulus:",self.n1%self.n2)#n1%n2
        return
obj = MyClass()
obj.show()
obj.display()
