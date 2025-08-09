class Bankaccount:
    a= "Welcome Jayanta's Bank"
    print("\n",a.center(100))
    

    def __init__(self,account_holder,account_number,balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def deposit(self,ammount):
        self.balance +=ammount
        print(f"\n{ammount} deposite in your account-{self.account_number}")
        print(f"\nNew Balance = {self.balance}")
    def withdraw(self,ammount):
        if ammount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= ammount
            print(f"\n withdraw ammount is {ammount}")
            print(f"\nNew balance = {self.balance}")
    def display_balance(self):
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Account No.: {self.account_number}")
        print(f"Current Balance: {self.balance}")
acc = Bankaccount("Jayanta Samanta", 987634561000,20000)
acc.display_balance()
deposit_amount = float(input("\nEnter amount to deposit: "))
acc.deposit(deposit_amount)
withdraw_amount = float(input(f"\nEnter amount to withdraw: ₹"))
acc.withdraw(withdraw_amount)
print(f"\n------ Final Account Details ------")
acc.display_balance()
print(f"\nTHANK YOU!" \
"Visit Again")

# acc2 = Bankaccount("Nitin Das",531655561000,1000000)
# acc2.display_balance()
# deposit_amount = float(input("\nEnter amount to deposit: "))
# acc2.deposit(deposit_amount)
# withdraw_amount = float(input(f"\nEnter amount to withdraw: ₹"))
# acc2.withdraw(withdraw_amount)
# print(f"\n------ Final Account Details ------")
# acc2.display_balance()
# print(f"\nTHANK YOU!" \
# "Visit Again")


        
