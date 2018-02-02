#To restart the System
import os
while True:
	check = input("Want to restart your computer ? (y/n): ")
	if check == 'n':
		break
	else:
		os.system("shutdown /r /t 1")
