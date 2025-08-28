# A class representing a Car
class Car:
    def move(self):
        print("The car is driving down the road. 🚗")

# A class representing a Plane
class Plane:
    def move(self):
        print("The plane is flying high in the sky! ✈️")

# A class representing a Boat
class Boat:
    def move(self):
        print("The boat is cruising across the water. 🚤")

# --- Putting polymorphism to the test ---
# Create a list of different vehicle objects
vehicles = [Car(), Plane(), Boat()]

print("--- Time to get moving! ---")
for vehicle in vehicles:
    # This single line of code calls the 'move' method.
    # The output changes based on the object's class.
    vehicle.move()