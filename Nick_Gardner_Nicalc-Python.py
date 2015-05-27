# Nicalc
flag = True
while flag:
	import math
	print "-----------------------------------------------------------------------------"
	print ("*** Please type in the number of the operation you would like to execute ***")
	choice = raw_input("|1.Add|2.Subtract|3.Divide|4.Multiply|5.Exponent|6.Square Root|7.Distance|8.Midpoint|9.Quadratic|10.Ellipse Foci|11.Logarithm|12.Natural Log|13.Arithmetic and Geometric Sequence or Series|14.Quit|  ").title()
	# Add
	if choice == "1":
		choice1 = float(raw_input("Please type in a number 1   "))
		choice2 = float(raw_input("Please type in a number 2   "))
		print choice1 + choice2
	# Subtract
	elif choice == "2":
		choice1 = float(raw_input("Please type in the orginal number   "))
		choice2 = float(raw_input("Please type in the number to be subtracted from the orginal number   "))
		print choice1 - choice2
	# Divide
	elif choice == "3":
		choice1 = float(raw_input("Please type in a Dividend   "))
		choice2 = float(raw_input("Please type in a Divisor   "))
		if choice2 == 0:
			print "ERROR divisor cannot be zero"
		else:
			print choice1 / choice2
	# Mulitply
	elif choice == "4":  
		choice1 = float(raw_input("Please type in a Multiplicand   "))
		choice2 = float(raw_input("Please type in a Multiplier   "))
		print choice1 * choice2
	# Exponent
	elif choice == "5":
		choice1 = float(raw_input("Please type in a number   "))
		choice2 = float(raw_input("Please type in an exponent  "))
		print choice1 ** choice2
	# Square Root
	elif choice == "6": 
		choice1 = float(raw_input("Please type in a number   "))
		if choice1 < 0:
			neg_choice = abs(choice1)
			neg_choice2 = math.sqrt(neg_choice)
			print "%si" % (neg_choice2)
		else: 
			print math.sqrt(choice1)
	# Distance
	elif choice == "7":
		x1 = float(raw_input("Please type in x1   "))
		y1 = float(raw_input("Please type in y1   "))
		x2 = float(raw_input("Please type in x2   "))
		y2 = float(raw_input("Please type in y2   "))

		distance1 = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
		distance2 = math.sqrt(distance1)

		print "The distance between your 2 points is %s" % (distance2)
	# Midpoint
	elif choice == "8":
		x1 = float(raw_input("Please type in x1   "))
		y1 = float(raw_input("Please type in y1   "))
		x2 = float(raw_input("Please type in x2   "))
		y2 = float(raw_input("Please type in y2   "))

		midpointX = ((x1 + x2) / 2)
		midpointY = ((y1 + y2) / 2)

		print "Your midpoint is ( %s, %s )" % (midpointX, midpointY)
	# Quadratic
	elif choice == "9":
		a = float(raw_input("What is your a value?   "))
		b = float(raw_input("What is your b value?   "))
		c = float(raw_input("What is your c value?   "))

		bottom_term = 2 * a
		top_left_term = b * - 1

		right = (b ** 2) 
		right2 = (4 * a * c)
		right3 = right - right2
		right4 = math.sqrt(abs(right3))
		step = (b * -1) + right4
		step2 = (b * -1) - right4
		step3 = step / (2 * a)
		step4 = step2 / (2 * a)
		if right4 - math.floor(right4) == 0:
			print "Your zeroes are %s and %s" % (step3, step4)
		if right4 - math.floor(right4) != 0:
			print "%s +- sqrt(%s)" % (top_left_term, right3)
			print "--------------"
			print "     %s       " % (bottom_term)
			print "Your zeroes are %s and %s" % (step3, step4)
	# Ellipse Foci
	elif choice == "10":
		orientation = raw_input("Is the ellipse 1. vertical or 2. horizontal?   ")
		h_input = float(raw_input("What is your h value?   "))
		k_input = float(raw_input("What is your k value?   "))
		choice3 = float(raw_input("What is the distance of your major axis?   "))
		choice4 = float(raw_input("What is the distance of your minor axis?   "))
		
		minor = (choice4 * .5) ** 2
		major = (choice3 * .5) ** 2

		if orientation == "1":
			if minor > 0:
				right_term = major - minor
				cF = math.sqrt(right_term)
				k = k_input + cF
				k2 = k_input - cF
				print "Your first focus is (%s, %s)" % (h_input, k)
				print "Your second focus is (%s, %s)" % (h_input, k2)
			if minor < 0:
				right_term = major + minor
				cF = math.sqrt(right_term)
				k = k_input + cF
				k2 = k_input - cF
				print "Your first focus is (%s, %s)" % (h_input, k)
				print "Your second focus is (%s, %s)" % (h_input, k2)
		if orientation == "2":
			if minor > 0:
				right_term = major - minor
				cF = math.sqrt(right_term)
				h = h_input + cF
				h2 = h_input - cF
				print "Your first focus is (%s, %s)" % (h, k_input)
				print "Your second focus is (%s, %s)" % (h2, k_input)
			if minor < 0:
				right_term = major + minor
				cF = math.sqrt(right_term)
				h = h_input + cF
				h2 = h_input - cF
				print "Your first focus is (%s, %s)" % (h, k_input)
				print "Your second focus is (%s, %s)" % (h2, k_input)

	#Logarithm
	elif choice == "11":
		print "Please input the corresponding numbers or type '0.0' if they do not exist."
		output = float(raw_input("What is the output?   "))
		x = float(raw_input("What is the x value?   "))
		base = float(raw_input("What is the base value?   "))
		if x == 0.0:
			x = math.log(output, base)
			print x
		elif base == 0.0:
			base = output ** 1 / x
			print base
		elif output == 0.0:
			output = base ** x
			print output
		else:
			print "That is not a valid response"

	#Natural log
	elif choice == "12":
		print "Please input the corresponding numbers or type '0.0' if they do not exist."
		sv = float(raw_input("What was your original value?   "))
		ev = float(raw_input("What was your ending value?   "))
		rate = float(raw_input("What was the rate?   "))
		time = float(raw_input("What was the time   "))

		if ev == 0.0:
			e = math.log(rate * time)
			print "Your ending value is %s" % (e*sv)
		elif rate == 0.0:
			left = ev / sv
			left2 = math.pow(left, (1 / time))
			print "Your rate is %s" % (math.log(left2))
		elif time == 0.0:
			left = ev / sv
			left2 = math.pow(left, (1/ rate))
			print "Your time value is %s" % (math.log(left2))
		elif sv == 0.0:
			exp = rate * time
			e = math.exp(exp)
			print exp
			print e
			print "Your starting value is %s" % (ev / e)
		elif sv != 0 and ev != 0 and rate != 0 and time != 0:
			print "One of the values must be zero for the equation to be solved, please try again."
		else:
			print "That is not a valid response"

	#Arithmetic and Geometric Sequences and Series
	elif choice == "13":
		op = float(raw_input("Is this an 1.Arithmetic Sequence, 2.Arithmetic Series, 3.Geometric Sequence, 4.Convergent Infinite Geometric Series, or 5.Partial Sum of a Geometric Series?   "))
		if op == 1:
			n = float(raw_input("How many terms are in your sequence?   "))
			d = float(raw_input("What is the difference from one number to the next number in your sequence?   "))
			u1 = float(raw_input("What is the first unit in your sequence?   "))
			
			right = ((n - 1) * d)
			un = right + u1
			print un

		elif op == 2:
			n = float(raw_input("How many terms are in your series?   "))
			u1 = float(raw_input("What is the first unit in your series?   "))
			d = float(raw_input("What is the difference from one number to the next number in your series?   "))

			right = ((n - 1) * d)
			un = right + u1
			print un

			par = (u1 + un) / 2
			sn = n * par
			print sn
			

		elif op == 3:
			n = float(raw_input("How many terms are in your sequence?   "))
			r = float(raw_input("What is the rate of your sequence?   "))
			u1 = float(raw_input("What is the first unit in your sequence?   "))
			
			exp = (n - 1)
			right = math.pow(r, exp)
			right2 = u1 * right
			print right2

		elif op == 4:
			r = float(raw_input("What is the rate of your series?   "))
			u1 = float(raw_input("What is the first unit in your series?   "))

			right = (1 - r)
			s = u1 / right
			print s
		elif op == 5:
			n = float(raw_input("How many terms are in your series?   "))
			r = float(raw_input("What is the rate of your series?   "))
			u1 = float(raw_input("What is the first unit in your series?   "))

			right = (1 - math.pow(r, n) / (1 - r))
			sn = right * u1
			print sn
		else:
			print "That is not a valid response"

	# Quit
	elif choice == "14":
		flag = False
	else:
		print "That is not a valid input"
