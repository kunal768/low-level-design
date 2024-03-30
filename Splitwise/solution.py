from enum import Enum
import sys 

# Enums 
class PaymentStatus(Enum):
	HAS_PAID, HAS_TOPAY = 0, 1 

class SplitType(Enum):
	EQUAL, EXACT, PERCENT = 0, 1, 2

class SplitStatus(Enum):
	INIT, FAILED, COMPLETED = 0, 1, 2


# Implementation for above thinking
class User:
	def __init__(self, userId, name, email, mobile):
		self.name = name 
		self.userId = userId
		self.email = email
		self.mobile = mobile 
		self.balance = 0 


class Payee(User):
	def __init__(self, userId, amount = 0, status = PaymentStatus.HAS_TOPAY):
		self.userId = userId 
		self.amount = amount
		self.status = status 


class Expense:
	def __init__(self, expenseId, payee, split_among, split_type = SplitType.EQUAL, split_status = SplitStatus.INIT, exact_split_amounts = [], percent_split_amounts = []):
		self.id = expenseId
		self.payee = payee 
		self.split_among = split_among
		self.split_type = split_type
		self.split_status = split_status
		self.exact_split_amounts = exact_split_amounts
		self.percent_split_amounts = percent_split_amounts

	def __str__(self):
		summary  = {
			"expense_id" : self.id,
			"payee_Id" : self.payee.userId,
			"payee_amt" : self.payee.amount,
			"split_among" : [(people.userId, people.amount) for people in self.split_among],
			"split_type" : self.split_type.name,
			"split_status" : self.split_status.name,
			"exact_split_amounts" : self.exact_split_amounts,
			"percent_split_amounts" : self.percent_split_amounts
		}

		return str(summary)


def panic(err):
	print(err)
	sys.exit()


class Calculate(SplitWise):
	def __init__(self, splitwise, expense):
		self.expense = expense 
		self.splitwise = splitwise

	def update_overall_balance(self, latest_expense, status):
		# logic to change overall balance 
		if latest_expense.split_status != SplitStatus.COMPLETED :
			panic("expense not yet completed")

		# now update overall expense





	def calculate_and_update_expense(self):
		print("Initial Status")
		print(self.expense)
		split_type = self.expense.split_type 
		amount_paid = self.expense.payee.amount
		if split_type == SplitType.EQUAL :
			calc_split_amount = amount_paid/len(self.expense.split_among)
			print(calc_split_amount)
			for people in self.expense.split_among :
				if people.status == PaymentStatus.HAS_TOPAY :
					print(people.userId, people.amount)
					people.amount = calc_split_amount

		elif split_type == SplitType.EXACT :
			for owed_personId, owed_amount in self.expense.exact_split_amounts :
				for people in self.expense.split_among :
					if people.userId == owed_personId and people.status != people.HAS_PAID :
						people.amount = owed_amount

		elif split_type == SplitType.PERCENT:
			for owed_personId, owed_percent in self.expense.percent_split_amounts :
				for people in self.expense.split_among :
					if people.userId == owed_personId and people.status != people.HAS_PAID :
						people.amount = amount*owed_percent/100

		print("Final Status")
		print(self.expense)

		return self.update_overall_balance(self.expense)

	
	def update_expense_status(self, status):
		self.expense.split_status = status
		return 



class SplitWise:
	def __init__(self, users = []):
		self.users = users
		self.groups = []
		self.logs = []
		self.lending_tracker = {}

	def add_user(self, user):
		self.user.append(user)

	def remove_user(self, username):
		self.users.remove(username)

	def __str__(self):
		return ' '.join([user.name for user in self.users])




user1 = User(1, "Alice", "alice@example.com", "12345")
user2 = User(2, "Bob", "bob@example.com", "67890")
user3 = User(3, "Jack", "jack@example.com", "231234")


payee = Payee(1, 50, PaymentStatus.HAS_PAID)
expense1 = Expense(1, payee, [payee, Payee(2)])
calculator = Calculate(expense1)
calculator.calculate_and_update_expense()

payee = Payee(1, 50, PaymentStatus.HAS_PAID)
expense2 = Expense(2, payee, [Payee(2), Payee(3)])
calculator2 = Calculate(expense2)
calculator2.calculate_and_update_expense()




payee = Payee(1, 100, PaymentStatus.HAS_PAID)
expense3 = Expense(3, payee, [payee, Payee(2), Payee(3)])
calculator3 = Calculate(expense3)
calculator3.calculate_and_update_expense()




