class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def addPassenger(self, name):
        if self.openSeats() > 0:
            self.passengers.append(name)
            return True
        return False
    def openSeats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
for a in {"a","b","c","d"}:
    if flight.addPassenger(a):
        print(f"{a} added")
    else:
        print(f"Flight Full for {a}")
