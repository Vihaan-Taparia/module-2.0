#TRIP EXPENDITURE
def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if"Vihaan"==city:
        return 183
    elif"Taparia"==city:
        return 220
    elif"Lambo"==city:
        return 222
    elif"Ronaldo"==city:
        return 475
def rental_car_cost(days):
    if days>=7:
        return 40*days - 50
    if days>=3:
        return 40*days - 20
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
print("Cost of car rental:",rental_car_cost(5))
print("Cost of plane ride:",plane_ride_cost("Ronaldo"))
print("Cost of hotel room:",hotel_cost(7))
print("Total cost of the trip:",trip_cost("Ronaldo",7,500))
print(trip_cost("Taparia",6,500))