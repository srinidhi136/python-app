#To find the ip address #
import socket
while True:
	print("Want to get IP Address ? (y/n): ")
	check = input()
	if check == 'n':
		break
	else:
		print("Your IP Address is: ",end="")
		print(socket.gethostbyname(socket.gethostname()))
		print()
