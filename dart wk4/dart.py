// Abstraction: Define an abstract class
abstract class Vehicle {
  String brand;

  Vehicle(this.brand);

  // Abstract method
  void honk();
}

// Inheritance: Define a subclass that inherits from Vehicle
class Car extends Vehicle {
  // Encapsulation: private variable to hide sensitive data
  int _speed;

  Car(String brand, this._speed) : super(brand);

  // Getter for private variable
  int get speed => _speed;

  // Setter with controlled access
  set speed(int value) {
    if (value >= 0) {
      _speed = value;
    } else {
      print("Speed cannot be negative");
    }
  }

  // Polymorphism: Method overriding
  @override
  void honk() {
    print("$brand Car is honking: Beep! Beep!");
  }
}

// Another subclass implementing the abstract class Vehicle
class Bike extends Vehicle {
  int _gear;

  Bike(String brand, this._gear) : super(brand);

  // Getter and setter for encapsulated field
  int get gear => _gear;

  set gear(int value) {
    if (value > 0) {
      _gear = value;
    } else {
      print("Gear value should be positive");
    }
  }

  // Polymorphism: Method overriding
  @override
  void honk() {
    print("$brand Bike is honking: Ring! Ring!");
  }
}

void main() {
  // Create a Car object
  Car myCar = Car('Toyota', 120);
  print('Car brand: ${myCar.brand}, Speed: ${myCar.speed} km/h');
  myCar.honk();

  // Change car speed using encapsulated setter
  myCar.speed = 150;
  print('Updated Speed: ${myCar.speed} km/h');

  // Create a Bike object
  Bike myBike = Bike('Yamaha', 5);
  print('Bike brand: ${myBike.brand}, Gear: ${myBike.gear}');
  myBike.honk();

  // Attempt to set an invalid gear
  myBike.gear = -1; // Controlled access prevents negative values
}