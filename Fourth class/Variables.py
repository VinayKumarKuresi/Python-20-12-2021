'''
Variable name defining

try :
    for = 3
except:
    print("we shouldn' use keywords for variable defining")

try :
    raise ValueError("That is not a positive number!")
except ValueError as e:
    print(e)

'''
#  we should follow this format,
#  we should give proper understandable name to the value

x = 34
y = 30
z = 12

c = x - y + z

print(c)

# we should give proper understandable name to the value
# in the below format

'''

    here are caluculating
    current number of
    flights

'''

initial_number_of_flights = 34
take_off_flights = 30
landed_flights = 12

current_number_of_flights = initial_number_of_flights - take_off_flights + landed_flights 

print(current_number_of_flights) # displays current no of flights