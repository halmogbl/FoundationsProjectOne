####################### DO NOT MODIFY THIS CODE ########################
menu = {
	"original cupcake": 2,
	"signature cupcake": 2.750,
	"coffee": 1,
	"tea": 0.900,
	"bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Almogbl"
signature_flavors = ["tuna","salmon","red herring"]
order_list = []


def print_menu():
	"""
	Print the items in the menu dictionary.
	"""
	for item in menu:
		print ( "- '%s'   (KD %s)"  % (item, menu[item]) )
	# your code goes here!


def print_originals():
	"""
	Print the original flavor cupcakes.
	"""

	print("Our original flavor cupcakes (KD %s each):" % original_price)
	# your code goes here!
	for flavor in original_flavors:
		print ("- '%s' "% (flavor))

def print_signatures():
	"""
	Print the signature flavor cupcakes.
	"""
	print("Our signature flavor cupcake (KD %s each):" % signature_price)
	# your code goes here!
	for signature in signature_flavors:
		print ("- '%s' "% (signature))

def is_valid_order(order):
	"""
	Check if an order exists in the shop.
	"""
	# your code goes here!
	if order in menu or order in original_flavors or order in signature_flavors :
		return True
	else:
		return False
	if False:
		print ("Your Order Is Not Avalible In Our Menus")

def get_order():
	"""
	Repeatedly ask customer for order until they end their order by typing "Exit".
	"""
	order_list = []
	# your code goes here!

	the_order = input("What is your order? ( Enter the exact spelling of the item you want. Type 'Exit' to end your order) \n")

	while the_order != "Exit":
		if is_valid_order(the_order) == True:
			order_list.append(the_order)
			the_order = input()
		else:
			the_order = input("Item is not avalible . Please try another again: ")

	return order_list


def accept_credit_card(total):
	"""
	Return whether an order is eligible for credit card payment.
	"""
	# your code goes here!
	if total < 5:
		return False
	else:
		return True

def get_total_price(order_list):
	"""
	Calculate and return total price of the order.
	"""
	total = 0
	# your code goes here!
	for order in menu:
		if order in menu:
			total += menu[order]
		elif order in original_flavors:
			total += 2
		else:
			total += 2.750
	return total


def print_order(order_list):
	"""
	Print the order of the customer.
	"""
	print()
	print("Your order is: ")
	# your code goes here!
	for ss in order_list:
		print ('- %s' % ss)
	total_price = get_total_price(order_list)
	print ("That will be KD %s " %total_price)
	if accept_credit_card(total_price) == True:
		print("This order is eligible for credit card payment. ")
	else:
		print("Only Cash Please")
	print("Thank you for shopping at Get Baked")
