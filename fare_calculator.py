# Travel Fare Calculators 
FARE_RATE = 14

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number

# Selection-structure-driven validation and input reentry

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

if distance >= 30:
    print ("Your fare is 45")
else:
    print ("Your fare is 25")

# Loop-based validation and input reentry

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

if distance >= 30:
    print ("Your fare is 45")
else:
    print ("Your fare is 25")
    
if not (1 <= passengers <= 20):
    print("Error: Passenger amount is not between 1 and 20.")
else:
    print("Valid passenger amount.")
