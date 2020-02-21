from os import system
system('clear')
logp = '''
	\033[0m| \033[0;33m3 \033[0m|         | \033[0;33m7 \033[0m|
	\033[0m| \033[0;33m4 \033[0;32m=~=~> \033[0;33m4   \033[0m| \033[0;33m9 \033[0;32m=~=~> \033[0;33m9
	\033[0m| \033[0;33m5 \033[0m|         | \033[0;33m11 \033[0m|

    \033[0;95m { \033[0;92mif \033[0;91mG P A         \033[0;33m    V \033[0;95m}
    \033[0;95m { \033[4;34mwww\033[4;33m.\033[4;34mifcompany\033[4;33m.\033[4;34mir\033[0;33m     1 \033[0;95m}
    \033[0;95m { \033[4;34mgithub\033[4;33m.\033[4;34mcom\033[4;33m/\033[4;34mifcompany\033[0;33m 0 \033[0;95m}
    \033[0;95m { \033[4;34mT\033[4;33m.\033[4;34mme\033[4;33m/\033[4;34mThe\033[4;32mlink\033[4;33mif\033[0;33m       0 \033[0;95m}
    \033[0;95m [ \033[4;33mProgrammer\033[0;36m : \033[0;101m007\033[0m      \033[0;95m ]\033[0m

	  \033[0;34mTo Calculate \033[0;33m( \033[0;31m= \033[0;33m) \033[0;34msend
'''
db = []

def cac():
	while(True):
		num = input("\033[0;36m[\033[0;33m$\033[0;36m]\033[0;32m Enter Score\033[0;34m \> \033[0m")
		if num.isnumeric():
			num = int(num)
			if 21 > num > 0:
				db.append(num)
			else:
				print("\033[0;36m[\033[0;31mError\033[0;36m]\033[0;32m The Score must be between 0 and 20\033[0m")
		elif num == "=":
			break
		else:
			print("\033[0;36m[\033[0;31mError\033[0;36m]\033[0;32m The Score Should Only be a Number\033[0m")
def clcl():
	y = 0
	total = 0
	for p in db:
		y += 1
		total += p
	endwork = total/y
	print("\033[0;36m[\033[0;32m#\033[0;36m]\033[0;32m Your GPA \033[0;33m= \033[0;32m"+str(endwork)+"\033[0m")

if __name__ == '__main__':
	print(logp)
	cac()
	if db == []:
		print("\033[0;36m[\033[0;31mError\033[0;36m]\033[0;32m You didn't enter anything\033[0m")
	else:
		clcl()