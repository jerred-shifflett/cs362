#simple 4 funciton calculator
#user enters 5 to exit
#Jerred Shifflett
#####################
def addition(x,y):
	return x+y

def substraction(x,y):
	return x-y

def multiplication(x,y):
	return x*y
def division(x,y):
	return x/y

def userPrompt():
	print("1. addition")
	print("2. substraction")
	print("3. multiplication")
	print("4. division")
	print("5. to exit program")

def getFirstNumber():
	firstNumber = float(input("Enter the firstNumber."))
	return firstNumber

def getSecondNumber():
	secondNumber = float(input("Enter the firstNumber."))
	return secondNumber



def main():
	userChoice =0

	while userChoice!=5:
		userPrompt()
		userChoice = int(input("Enter one of the choices above."))
		if userChoice==1:
			num1= getFirstNumber()
			num2= getSecondNumber()
			print(num1, " + ", num2, "=", addition(num1,num2))
		elif userChoice == 2:
			num1=getFirstNumber()
			num2= getSecondNumber()
			print(num1, " - ", num2, "=", substraction(num1,num2))
		elif userChoice ==  3:
			num1=getFirstNumber()
			num2= getSecondNumber()
			print(num1, " * ", num2, "=", multiplication(num1,num2))
		elif userChoice == 4:
			num1=getFirstNumber()
			num2= getSecondNumber()
			if num2 ==0:
				print("Undefined")
			else:
				print(num1, " / ", num2, "=", division(num1,num2))
		elif userChoice == 5:
			userChoice = 5
		else:
			print("Please follow to the instructions.")
main()