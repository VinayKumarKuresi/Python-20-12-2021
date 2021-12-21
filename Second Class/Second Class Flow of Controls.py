# yeswant_baggage = -1
# Air_India_baggage = 25
# Emirates_baggage = 40
#
# if yeswant_baggage >= 0 and yeswant_baggage <= Air_India_baggage:
#     print("Yeswant is Allowed in Air India")
# elif yeswant_baggage >= 0 and yeswant_baggage <= Emirates_baggage:
#     print("Yeswant is Allowed in Emirates")
# else:
#     print("Baggage weight should be greater than zero")
ticket_status = "Confirmed"
person_luguage_weight = 55
flight_weight_limit = 30
extra_charge = 0
if ticket_status == "Confirmed":
    print("Yeswant is allowed")
    if person_luguage_weight == 0:
        print("No charges")
    if person_luguage_weight > 0 and person_luguage_weight <= flight_weight_limit:
        print("No Charges")
    elif person_luguage_weight <= flight_weight_limit + 10:
        extra_charge = 300 * (person_luguage_weight - flight_weight_limit)
        print("Extra charges : ",extra_charge)
    elif person_luguage_weight > flight_weight_limit + 10:
        extra_charge = 500 * (person_luguage_weight - flight_weight_limit)
        print("Extra charges : ", extra_charge)
else:
    print("Yeswant is not allowed")

