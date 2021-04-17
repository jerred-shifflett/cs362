#prompts the user to enter a number
#the program will print the divisors of that number
#user enters 2 to exit
def showDivsors(userNum):
	
	for divisor in range(1,userNum+1):
		if(userNum%divisor==0):
			print(divisor)

def main():
	userChoice=0

	while userChoice!=2:
		userChoice=(int(input("Enter 1 to find a divisor or Enter 2 to exit\n")))
		if userChoice==1:
			userNum = (int(input("Enter A Number.")))
			showDivsors(userNum)
		else:
			print("goodbye")
main()