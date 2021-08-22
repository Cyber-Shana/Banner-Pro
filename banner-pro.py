import os  ,shutil ,time
import sys
from time import sleep
import time
os.system("clear")
time.sleep(0.23)
print()
time.sleep(1.03)
print("""\033[32m██████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
██████╦╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
██╔══██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
██████╦╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝""")
print()
time.sleep(0.23)
print()
time.sleep(0.23)
print("""\t\033[31m	
		██████╗░██████╗░░█████╗░
		██╔══██╗██╔══██╗██╔══██╗
		██████╔╝██████╔╝██║░░██║
		██╔═══╝░██╔══██╗██║░░██║
		██║░░░░░██║░░██║╚█████╔╝
		╚═╝░░░░░╚═╝░░╚═╝░╚════╝░""")
		
time.sleep(0.13)
print()
time.sleep(0.08)
print()
time.sleep(0.13)
print("\t\033[35m		❮❮⚞ Coded By Cyber SHANA ⚟❯❯")
print()
time.sleep(0.10)
print("\t \033[93m		    [+]Owner Of Cyber Back Shot")
time.sleep(0.10)
print("\t \033[93m		    [+]Member Of SLCW")
time.sleep(0.10)
print("\t \033[93m		    [+]Member Of CEO")
time.sleep(0.13)
print()
time.sleep(0.08)
print(" \033[37m___________________________________________________________________")
print()
time.sleep(0.03)
time.sleep(0.03)
time.sleep(0.08)
print()
time.sleep(0.08)
print()
time.sleep(0.08)
print ("\t \033[34m	 [1]\033[01m Evil Eye Banner \033[0m")
time.sleep(0.5)
print()
time.sleep(0.03)
print ("\t\033[34m 	 [2] \033[0m\033[94mNeofetch Banner\033[0m")
time.sleep(0.5)
print()
time.sleep(0.3)
print("\t\033[34m 	[3]\033[0m \033[94m  Exit  ")
time.sleep(0.05)
print ()
time.sleep(0.03)
print()
print("\033[0m______________________________________________________________________")
time.sleep(0.13)
print ()
print()
time.sleep(0.13)
def evil():
	name = str(input(" ➢ Enter Your banner  Name :-  "))
	cs = str(input("  ➢ Enter Cowsay Text :-  "))
	speed = str(input(" ➢ Enter Required Speed [50 - 150] :- "))
	
	text1 = ("cowthink -f eyes "+cs+" |lolcat -a --speed="+speed)
	text2 = ("\nfiglet "+name+" |lolcat -a --speed="+speed)
	
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
def neo():
	name = str(input("  ☞  Enter Banner  Name : "))
	text1 = "neofetch"
	text2 = ("\nfiglet "+name+" |lolcat -a --speed=80")
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
def move_f():
	if os.path.exists("/data/data/com.termux/files/usr/etc/zshrc"):
		os.remove("/data/data/com.termux/files/usr/etc/zshrc")
	shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
	print ("  \033[95m DONE DONE DONE ")
cho = int(input("  ❐ Enter Your Choice :- "))
print ()
print()
if cho == 1 :
	evil()
	move_f()
elif cho == 2:
	neo()
	move_f()
print ()
if cho == 3 :
	time.sleep(3.0)
	exit()
else :
	print ()
	print ("  \033[95m Your Choice Is Wrong !! ")
	time.sleep(3.0)
	os.system("banner-Pro.py")
