#Jerred Shifflett
#creates random password to the desired length 
#specified by the user


import string
import random

#going to gather all the components of the password
alphabet = string.ascii_letters
tendigits = string.digits
symbols = string.punctuation

def getLength():
	userlength = int(input("Enter the length of the password."))
	return userlength

def generator(userlength):
	#place them into one string
	passOptions = f' {alphabet}{tendigits}{symbols} '
	#type casting into a more functional list
	passOptions = list(passOptions)
	random.shuffle(passOptions)
	#now we are selecting random compents of the password
	#to length wanted by the user.
	#then we join it to a single list.
	password = random.choices(passOptions, k= userlength)
	password = ''.join(password)
	return password

def main():
	passLength = getLength()
	password = generator(passLength)
	print("your password is: "+ password)
main()