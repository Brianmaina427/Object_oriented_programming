# The parent class
class Superhero:
    """A class to represent a generic superhero."""
    
    # The constructor, which initializes each new object
    def __init__(self, name, secret_identity, power, nemesis):
        self.name = name
        self.secret_identity = secret_identity
        self.power = power
        self.nemesis = nemesis
        self.health = 100  # Default attribute
    
    # Methods (actions)
    def display_info(self):
        print(f"--- {self.name} ---")
        print(f"Secret Identity: {self.secret_identity}")
        print(f"Primary Power: {self.power}")
        print(f"Current Health: {self.health} HP")

    def use_power(self):
        print(f"{self.name} is using their {self.power} power!")

# The child class, which inherits from Superhero
class FlyingSuperhero(Superhero):
    """A specialized superhero that can fly."""
    
    # This method overrides the parent's method, a form of polymorphism
    def use_power(self):
        print(f"{self.name} soars into the sky with incredible speed!")
        
    # This is a new method unique to this class
    def fly(self):
        print(f"{self.name} is flying high above the city! 🏙️")

# --- Using the classes ---
dark_knight = Superhero("Dark Knight", "Bruce Wayne", "Gadgets & Tactics", "The Joker")
dark_knight.display_info()
dark_knight.use_power()

print("\n--- The Flying Superhero ---")
speedster = FlyingSuperhero("The Streak", "Barry Allen", "Super Speed", "Reverse Flash")
speedster.display_info()
speedster.use_power()  # This will call the overridden method
speedster.fly()
