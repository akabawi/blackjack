import time

class Account:

	def __init__(self,name,balance):
		self.name = name
		self.balance = balance

	def withdraw(self,w):

		self.balance = self.balance - w

	def deposit(self,d):

		self.balance = self.balance + d

	def check_withdrawal(self,c):

		if c > self.balance:
			return 0
		return 1


def check_input(inpt):

	valid_input = ("v","w","d","q")

	if inpt in valid_input:
		return True
	return False

print("\nPlease enter account holder name: ")
acc_n = input()
print("\nPlease enter initial account balance: ")
bal = int(input())

acc = Account(acc_n,bal)

print("\n---------------------------------")
print("Please select action: ")
print("v-> view account details")
print("d-> deposit")
print("w-> withdraw")
print("q-> quit")
print("---------------------------------\n")

sel = input()

while sel != "q":

	while check_input(sel) == False :
		print("Invalid input! Please enter a valid selection")
		sel = input()

	if sel == "v":
		print("\nAccount Holder Name: " + acc.name)
		print("Account Balance    : " + str(acc.balance) + "\n")
		time.sleep(2)

	if sel == "d":
		print("\nPlease enter deposit amount:")
		dip = int(input())
		acc.deposit(dip)
		print("\nDeposit successful\n")
		time.sleep(2)
	if sel == "w":
		print("\nPlease enter withdrawal amount:")
		wit = int(input())
		if acc.check_withdrawal(wit) == 0:
			print("\nNot enough balance for withdrawal\n")
			time.sleep(2)
		else:
			acc.withdraw(wit)
			print("\nWithdrawal successful\n")
			time.sleep(2)

	print("\n---------------------------------")
	print("Please select action: ")
	print("v-> view account details")
	print("d-> deposit")
	print("w-> withdraw")
	print("q-> quit")
	print("---------------------------------\n")

	sel = input()
time.sleep(2)
print("Thank you, Goodbye!")
time.sleep(2)



