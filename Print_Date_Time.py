import datetime
while True:
	print("Want to print Today's Date and Time ? (y/n): ")
	check = input()
	if check == 'n':
		break
	else:
		print("Today's date and time:")
		print(datetime.datetime.today())
		print()
