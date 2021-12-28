

# extra charges

wt_limmit = 30 # global variable
extra_baggage_cost = 200 # global variable
def baggage_check(person_baggage_weight):
    extra_weight = 0 # local variable
    if (person_baggage_weight > 0 and person_baggage_weight <= wt_limmit):
        return extra_weight
    else:  
        extra_weight = person_baggage_weight - wt_limmit
        extra_baggage_cost = extra_weight * 200 # local variable

        return extra_baggage_cost


def update_wt_limit(up_weight_limit):
    global wt_limmit
    wt_limmit = up_weight_limit


up_weight_limit = int(input("Enter updated weight : "))
update_wt_limit(up_weight_limit)
person_baggage_weight = int(input("Enter the person baggage weight : "))
print("The person baggage weight : ", person_baggage_weight)
extra_baggage_cost = baggage_check(person_baggage_weight)
print("The extra baggage cost : ", extra_baggage_cost)

