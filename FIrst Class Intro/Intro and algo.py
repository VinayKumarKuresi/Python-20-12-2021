Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Vinay")
Vinay
>>> at_the_start = 100
>>> take_off = 40
>>> landing_planes = 60
>>> 
>>> Current_no_of_flights = at_the_start - take_off + landing_planes
>>> 
>>> Current_no_of_flights
120
>>> at_the_start
100
>>> 
>>> 


>>> 

>>> 


>>> 


>>> 

>>> 

>>> 
>>> 
>>> 
>>> num1 = 30
>>> num2 = 10
>>> 
>>> num1 + num2
40
>>> num1 / num2
3.0
>>> 
>>> num1 % num2
0
>>> 5 % 2
1
>>> num1 == num2
False
>>> num1 == 30
True
>>> num1 == 30 and num2 == 10
True
>>> num1 == 30 and num2 == 20
False
>>> num1 == 30 or num2 == 20
True
>>> not num1 == 30
False
>>> 
>>> runway = "free"
>>> if runway == "free":
	print("You can land")
else :
	print("should circle in AIR")

	
You can land
>>> runway = "not free"
>>> if runway == "free":
	print("You can land")
else :
	print("should circle in AIR")

	
should circle in AIR
>>> 
>>> runway = "free"
>>> fuel = "efficient"
>>> 
>>> if runway == "free":
	print("You can land")
else if fuel == "low":
	print("Emergency landing")
else :
	print("should circle in AIR")	

SyntaxError: invalid syntax
>>> if runway == "free":
	print("You can land")
elif fuel == "low":
	print("Emergency landing")
else :
	print("should circle in AIR")

	
You can land
>>> runway = "free"
>>> runway = "not free"
>>> fuel = "efficient"
>>> 
>>> if runway == "free":
	print("You can land")
elif fuel == "low":
	print("Emergency landing")
else :
	print("should circle in AIR")

	
should circle in AIR
>>> runway = "not free"
>>> fuel = "low"
>>> 
>>> if runway == "free":
	print("You can land")
elif fuel == "low":
	print("Emergency landing")
else :
	print("should circle in AIR")

	
Emergency landing
>>> 
>>> yeswant_baggage = 30
>>> Air_India_baggage = 25
>>> Emirates_baggage = 40
>>> 
>>> if yeswant_baggage <= Air_India_baggage :
	print("Yeswant is Allowed in Air India")
elif yeswant_baggage <= Emirates_baggage:
	print("Yeswant is Allowed in Emirates")
else:
	print("Yeswant is Not Allowed")

	
Yeswant is Allowed in Emirates
>>> 
