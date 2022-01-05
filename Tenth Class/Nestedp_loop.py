
number_of_passagers = 5
number_of_baggages = 2

for passanger in range(1, number_of_passagers+1): # 1 to 5(6 not included)
    for baggage in range(1, number_of_baggages+1):
        print("Security check cleared or not for baggage : ", baggage, " passanger ", passanger)
        security_check = input("Enter True or False : ")
        if (security_check == "True"):
            print("Security check cleared for baggage ", baggage," of passanger ", passanger)
        else:
            print("Security check not cleared for baggage ", baggage," of passanger ", passanger)