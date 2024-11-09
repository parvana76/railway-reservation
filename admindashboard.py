#basic data for trains
trains = [ {"train_id": 1, "name": "Express A", "origin": "City A", "destination": "City B", "seats": 100},
{"train_id": 2, "name": "Express B", "origin": "City B", "destination": "City C", "seats": 150}]
#basic data for reservations
reservations = [{"reservation_id": 1, "train_id": 1, "passenger_name": "Sanjana", "seat_number": 1},
{"reservation_id": 2, "train_id": 2, "passenger_name": "Rakshan", "seat_number": 1}]
# Admin functions
def view_trains():#to view trains
    print("\nTrain Schedules:")
    for train in trains:
        print('Train ID:',train['train_id'],'\tName:',train['name'],'\nOrigin:',train['origin'],
        '\tDestination:',train['destination'],'\nSeats Available:',train['seats'])

def add_train():#to add trains
    print("Add a New Train:")
    train_id = len(trains) + 1
    name = input("Enter train name: ")
    origin = input("Enter origin city: ")
    destination = input("Enter destination city: ")
    seats = int(input("Enter number of seats: "))
    trains.append({"train_id": train_id, "name": name, "origin": origin, "destination": destination, "seats": seats})
    print("Train has been successfully added!")
    
def view_reservations():#to view reservations
    idtrain=eval(input("Enter train id:"))
    print("Reservations List:")
    for train in trains:
            if train["train_id"]==idtrain:
                train_name=train["name"]
    for reservation in reservations:
        if reservation["train_id"]==idtrain:
            print('Reservation ID:',reservation['reservation_id'],'Train:',train_name,
            'Passenger:',reservation['passenger_name'],'Seat Number:',reservation['seat_number'])

def admin_dashboard():#main function
    print("Welcome to the Admin Dashboard")
    while True:
        print("\n--- Admin Dashboard ---")
        print("1. View Train Schedules")
        print("2. Add a New Train")
        print("3. View Reservations")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_trains()
        elif choice == "2":
            add_train()
        elif choice == "3":
            view_reservations()
        elif choice == "4":
            print("Exiting Admin Dashboard...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    admin_dashboard()
    
