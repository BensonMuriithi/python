#Introduction to variables

cars = 100
car_capacity = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars -drivers
cars_driven = drivers
carpool_capacity = cars_driven * car_capacity
avg_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "cars not used."
print "We can transport", carpool_capacity, "passengers today."
print "We have", passengers, "to ferry."
print "We need to put about", avg_passengers_per_car, "people in each car."