import os ,shutil ,time
from time import sleep
os.system ("clear")
print("""
██████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
██████╦╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
██╔══██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
██████╦╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝""")

print("""\t
		
		██████╗░██████╗░░█████╗░
		██╔══██╗██╔══██╗██╔══██╗
		██████╔╝██████╔╝██║░░██║
		██╔═══╝░██╔══██╗██║░░██║
		██║░░░░░██║░░██║╚█████╔╝
 		╚═╝░░░░░╚═╝░░╚═╝░╚════╝░""")
print()
print()

print("\t			[1] Evil Eye Banner ")
print("\t			[2] Neofetch")
print()
print()

def evil():
	name = str(input("Enter Your Name :- "))
	cs = str(input("Enter Cowsay text :- "))
	speed = str(input("speed :- "))
	
	text1 = ("cowthink -f eyes "+cs+"|lolcat -a --speed="+speed)
	text2 = ("\ntoilet"+name+"|lolcat -a --speed"+speed)
	
	
	with open("zshrc","w") as zsh : 
		zsh.write(text1)
		zsh.write(text2)
	
def neo():
	name = str(input(Enter name :- ))
	text1 = "neofetch"
	text2 = ("\nfiglet"+name+"|lolcat -a --speed=80")
		with open("zshrc","w") as zsh : 
		zsh.write(text1)
		zsh.write(text2)
		
def move_f():
		if os.path.exists("/data/data/com.termux/files/usr/etc/zshrc"):
			os.remove("/data/data/com.termux/files/usr/etc/zshrc")
			
		shutil.move("zshrc" , "/data/data/com.termux/files/usr/etc")
		print("033[32m DONE....\033[0m]")
			
cho = int(input("➣ Choice :-  "))
print()
print()

if cho == 1 : 
	evil()
	move_f()
	
elif cho == 2:
	neo()
	move_f()
else : 
	exit()