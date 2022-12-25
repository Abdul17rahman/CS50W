#This program creates a class called Flights that we can use to add passengers to a specific flight.

#define a class called Flight
class Flight():
    #define a self method/constructor
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.name = name
        self.passenger = []
    #define a func that adds a passenger.
    def add_passenger(self, pass_name):
        #Check if we have seats available
        if not self.open_seats():
            return False
        self.passenger.append(pass_name)
        return True
    #define a functions that allocates seats.
    def open_seats(self):
        #return available seats
        return self.capacity - len(self.passenger)
    #Print the available passengers
    def print_passengers(self):
        for client in self.passenger:
            print(client) 

#Use the flight object

f = Flight(3,"EK170")

#Add passengers to the EK-flight
people = ["Abdul", "Hadijah", "Birungi", "Juma"]

for person in people:
    if f.add_passenger(person):
        print(f"{person} has been successfully added to {f.name}")
    else:
        print(f"We have no available seats on {f.name} for {person}")
print("Below are the available passengers")
f.print_passengers()
