class Account:#class
    def __init__(self,name,account_no,balance):#constructor
        self.name=name
        self.account_no= account_no
        self.balance= balance
    def deposite(self,ammount):#construtor method
        self.balance +=ammount
        print(f"Rs.{ammount}")
        print(f"\n{ammount} deposite in your account-{self.account_no}")
        print(f"\nNew Balance = {self.balance}")
    def withdraw(self,ammount):
        if ammount>self.balance:
            print("Insaficient balance!")
        else:
           self.balance -=ammount
           print(f"Rs.{ammount}")
           print(f"\n withdraw ammount is {ammount} ")
        print(f"\nNew Balance = {self.balance}")
    def display_balance(self):
        # print("....Finaal Reciept...")
        print(f"Account Holder name: {self.name}")
        print(f"Account No.: {self.account_no}")
        print(f"Current Balance: {self.balance}")      

obj1=Account("jayanta",7865042543,20000) #object
obj1.display_balance()
deposite_ammount=float(input("Enter the deposite ammount:"))
obj1.deposite(deposite_ammount)
withdraw_ammount=float(input("Enter the withdraw ammount ammount:"))
obj1.withdraw(withdraw_ammount)
print(f"\n------ Final Account Details ------")
obj1.display_balance()
obj2=Account("kumar",9641870273,300000) #object2
deposite_ammount=float(input("Enter the deposite ammount:"))
obj2.deposite(deposite_ammount)
withdraw_ammount=float(input("Enter the withdraw ammount ammount:"))
obj2.withdraw(withdraw_ammount)
obj2.display_balance()