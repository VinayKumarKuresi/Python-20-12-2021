
'''
greatest of three numbers

a = 23
b = 50
c = 70

if a > b and a > c:
    print("A is greater")	
elif b > a and b > c:
    print("B is greater")	
else :
    print("C is greater")

'''

'''
# Loop Statement :
    # 1) Passanger Count :

passenger = 1
print("Passanger Count : ", passenger)
passenger = passenger  + 1
print("Passanger Count : ", passenger)
passenger = passenger  + 1
print("Passanger Count : ", passenger)

'''

baggage_count = 30

while baggage_count > 0 :
    picked_up_count = int(input("Enter the picked up bags : "))
    if picked_up_count <= baggage_count :
        baggage_count = baggage_count - picked_up_count 
        print("Remaning bags are : ", baggage_count)
    else:
        print("Picked up bags should be less than or equal to Baggage_count")
