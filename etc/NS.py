import string
import random

exec(open('etc/clear.py').read())#clear
PassowrdLenght=int(input("Please enter password lenght:\nUSER>>"))
if(PassowrdLenght>300):
	print("Is the American president getting the password? This long password is unreasonable and exceeds the limit.")
	pause=input("Press any key to continue...")
	exec(open('Password Generator.py').read())

def id_generator(size=6, chars=string.punctuation+string.digits):
	return ''.join(random.choice(chars) for _ in range(size))





exec(open('etc/clear.py').read())#clear
print("Your password:\n")
print(id_generator(PassowrdLenght))#print password
pause=input("Press any key to continue...")
exec(open('Password Generator.py').read())


