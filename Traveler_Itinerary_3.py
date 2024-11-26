def add_traveler(itineraries):
    # Input the traveler's information
    traveler_name = input("Enter the name of the traveler: ").title()
    origin = input("Enter the origin city: ").upper()
    destination = input("Enter the destination city: ").upper()
    
    # Create a new itinerary as a dictionary (for clarity and structure)
    itinerary = {
        "traveler_name": traveler_name,
        "origin": origin,
        "destination": destination
    }

    itineraries.append(itinerary)
    print(f"{traveler_name} is going from {origin} to {destination}")

def display_itineraries(itineraries):
    # Check if there are any itineraries to display
    if not itineraries:
        print("No itineraries to display.")
        return

    for num, itinerary in enumerate(itineraries, start=1):
        print(f"(Itinerary {num}: - {itinerary['traveler_name']} From {itinerary['origin']} to {itinerary['destination']})")

def main():
    # Initialize an empty list to hold all itineraries
    itineraries = []
    
    while True:
        # Menu options
        print("1. Add Traveler")
        print("2. View Itineraries")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_traveler(itineraries)  # Add traveler to the itineraries list
        elif choice == "2":
            display_itineraries(itineraries)  # Display all itineraries
        elif choice == "3":
            print("Exiting Itineraries.")
            break  # Exit and end the program
        else:
            print("Invalid entry. Please try again.")

if __name__ == "__main__":
    main()
