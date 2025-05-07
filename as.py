total_car = {}
total_cost = 0
 

STAFF_USERNAME = "sta001"
STAFF_PASSWORD = "givemethekeys123"

def staff_login():
    print("==== Staff Login ====")
    username = input("Username: ")
    password = input("Password: ")
    if username == STAFF_USERNAME and password == STAFF_PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Login failed. Please try again.\n")
        return False

def calculate_cost(days, car_type, fuel_type, unlimited_mileage, breakdown_cover):
    base_rate = 25
    car_extra = {
        "city": 0,
        "family": 50,
        "sports": 75,
        "suv": 65
    }
    fuel_extra = {
        "petrol": 0,
        "diesel": 0,
        "hybrid": 30,
        "full electric": 50
    }

    if car_type not in car_extra or fuel_type not in fuel_extra:
        return None

    total = days * base_rate
    total += car_extra[car_type.lower()]
    total += fuel_extra[fuel_type.lower()]
    
    if unlimited_mileage:
        total += 10 * days
    if breakdown_cover:
        total += 2 * days

    return total

def booking(first_name, surname, address, age, license_status, number_of_days, car_type, fuel_type, unlimited_mileage, breakdown_cover):
    global total_car

    if license_status.lower() != "yes":
        return "Booking can't proceed without a valid driving license."

    if not (1 <= number_of_days <= 28):
        return "Number of days must be between 1 and 28."

    total = calculate_cost(number_of_days, car_type, fuel_type, unlimited_mileage, breakdown_cover)
    if total is None:
        return "Invalid car or fuel type."

    booking_id = first_name.lower() + surname.lower() + str(number_of_days)

    total_car[booking_id] = {
        "First Name": first_name,
        "Surname": surname,
        "Address": address,
        "Age": age,
        "License Valid": license_status,
        "Days": number_of_days,
        "Car Type": car_type,
        "Fuel Type": fuel_type,
        "Unlimited Mileage": unlimited_mileage,
        "Breakdown Cover": breakdown_cover,
        "Total Cost": total
    }

    return f"""
Booking Summary:
----------------------
Name: {first_name} {surname}
Address: {address}
Age: {age}
License: {license_status}
Car Type: {car_type}
Fuel Type: {fuel_type}
Days: {number_of_days}
Unlimited Mileage: {unlimited_mileage}
Breakdown Cover: {breakdown_cover}
----------------------
Total Cost: £{total}
Booking ID: {booking_id}
"""

def display_bookings():
    if not total_car:
        print("No bookings found.")
    else:
        print("\n==== All Bookings ====")
        for bid, details in total_car.items():
            print(f"\nBooking ID: {bid}")
            for key, value in details.items():
                print(f"{key}: {value}")

def booking_input():
    print("\n==== Booking Form ====")
    first_name = input("Customer First Name*: ")
    surname = input("Customer Surname*: ")
    address = input("Customer Address*: ")
    age = input("Customer Age*: ")
    license_status = input("Do you have a valid driving license? (yes/no)*: ")
    number_of_days = int(input("Number of Days (1-28)*: "))
    car_type = input("Car Type (city/family/sports/suv)*: ").lower()
    fuel_type = input("Fuel Type (petrol/diesel/hybrid/full electric)*: ").lower()
    
    unlimited_mileage = input("Add Unlimited Mileage? (yes/no): ").lower() == 'yes'
    breakdown_cover = input("Add Breakdown Cover? (yes/no): ").lower() == 'yes'

    result = booking(first_name, surname, address, age, license_status, number_of_days, car_type, fuel_type, unlimited_mileage, breakdown_cover)
    print(result)




if staff_login():
    while True:
        print("\n--- Menu ---")
        print("1. Create a Booking")
        print("2. View All Bookings")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            booking_input()
        elif choice == '2':
            display_bookings()
        elif choice == '3':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")