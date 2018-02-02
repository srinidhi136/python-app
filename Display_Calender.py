import calendar
while True:
	print("Enter 'x' for exit." )
	y = input("Enter Year: ")
	m = input("Enter month: ")
	d = input("Enter Day :")
	if y == 'x':
		break
	else:
		yy = int(y)
		mm = int(m)
		dd = int(d)
		print("\n",calendar.month(yy,mm,dd))
