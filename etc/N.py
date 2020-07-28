from random import seed
from random import randint

exec(open('etc/clear.py').read())#clear
PassowrdLenght=int(input("Please enter password lenght:\nUSER>>"))
if(PassowrdLenght>300):
	print("Is the American president getting the password? This long password is unreasonable and exceeds the limit.")
	pause=input("Press any key to continue...")
	exec(open('Password Generator.py').read())
	
seed(1)
list=[]
for i in range(PassowrdLenght):
	for _ in range(10):
		data = randint(0, 10)
		list.append(data)
exec(open('etc/clear.py').read())#clear
print("Your password:\n")
print(*list, sep = "")#print password
pause=input("Press any key to continue...")
exec(open('Password Generator.py').read())