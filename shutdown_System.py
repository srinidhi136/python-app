import os
while True:
	check = input("Want to shutdown your computer ? (y/n): ")
	if check == 'n':
		break
	else:
		os.system("shutdown /s /t 1")
