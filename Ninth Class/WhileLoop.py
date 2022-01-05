
initial_number_of_bags = 100

while(initial_number_of_bags > 0): # initial_number_of_bags = 0 -> 
    picked_up_bags = int(input("Enter the number of bags Picked up : "))
    initial_number_of_bags = initial_number_of_bags - picked_up_bags
    print("Remaining bags : ", initial_number_of_bags)
