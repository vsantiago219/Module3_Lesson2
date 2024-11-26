#Task 1 Formatting Flight Itineraries   

def itinerary(): 
    itinerary=([])
    
    while True:
        print("1.Add Traveler")
        print("2. Display Itineraries")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice =="1":

            traveler_name = input("Enter the traveler's name: ").title()
            origin = input("Enter the city of origin: ").upper()
            destination = input("Enter the destination city: ").upper()
            itinerary = [(traveler_name, origin, destination)]
            
            print(f"{traveler_name} {origin} {destination}")

        elif choice == "2":
            num = 1
            itineraries = itinerary.append(itinerary)
            for index, itinerary in enumerate (itineraries, start = 1):

                print(f"Itinerary {num}: {traveler_name} - From {origin} to {destination}")
                num +=1
            

        elif choice =="3":
            print("Exiting Itineraries")
            break
        else:
            print("Invalid entry. Please try again")

itinerary()