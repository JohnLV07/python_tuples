''' 
*Objective*
-The aim of this assignment is to deepen your understanding of tuples in Python.

* Task 1: Formatting Flight itineraries
Create a Python function that takes a list of tuples as an argument.
Each tuple contains information about a flight itinerary:(travel_name, origin, destination).
The function should format and return a string that lists each itinerary. For example, if the input is '[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]'
The output should be a string formated as:


"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"


'''


flight_itinerary = [
    ("Jonathan", ("Dallas"),( "Los Angeles")),
    ("Daniela", ("Chicago"), ("Mexico City")),
    ("Erick", ("Aguascalientes"),( "Buenos Aires"))
]

for name in flight_itinerary:
    print(f"Itinerary for Passenger: '{name[0]}' deperting from: {name[1]}, flying to: {name[2]}. " )