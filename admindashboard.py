
#basic data for trains
trains = [ {"train_id": 1, "name": "Express A", "origin": "City A", "destination": "City B", "seats": 100, "price": 600},
{"train_id": 2, "name": "Express B", "origin": "City B", "destination": "City C", "seats": 150, "price": 500},
{"train_id": 3, "name": "Express C", "origin": "City A", "destination": "City C", "seats": 75, "price":700}]
#basic data for reservation
reservations = [{"reservation_id": 1, "train_id": 1, "passenger_name": "Paul", "seat_number": 1},
{"reservation_id": 2, "train_id": 2, "passenger_name": "Sara", "seat_number": 1}]
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
    
#Fuction to select payment method
def select_payment_method():
    print("Select payment method:")
    print("1. Credit/Debit card")
    print("2. Net Banking")
    print("3.UPI(Google pay, phonePe,etc.)")
    print("4.Wallets(Paytm,etc.)")
    print("5.EMI")
    
    choice = input("Enter your choice:")
    payment_method={
        "1":"card", "2":"netbanking","3":"upi","4":"wallet","5":"emi"}
    return payment_method.get(choice,None)
    
 
        order=client.order.create({"Amount":total_amt,"currency":"INR","payment_capture":"1","method":payment_mathods})
        print("payment Order ID:",order_id)
        print("Payment Method:", payment_methods)
        #simulating payemnt success (In real life scenario , payment status will come from the RAZORPAY API response)
        payment_status="SUCCESS"

        if payment_status =="SUCCESS":
            #reduce the seat count
            trains[train_no]['seats']-=num_seats
            print("Payment successful!",num_seats,"seats booked on ",trains[train_no]['name'],". Remaining seats :", trains[train_no]['seats'])
        else:
            print("Payment failed! Please try again.")
except ValueError:
     print("Please enter a valid number ")
    
    
def admin_dashboard():#mai#fuction to book train and initiate payment 
def book_train():
    view_trains()
    #plays a role in handling tasks ,ie. 
    try:
        train_no=int(input("enter the train number you want to book: "))
        if train_no not in trains:
            print("Invalid choice!")
            return
        num_seats=int(input("Enter the number of seats required:"))
        if num_seats<=0 or num_seats > trains[train_no]['seats']:
            print("Invalid number of seats")
            return
        #calculating total amount 
        total_amt=num_seats*trains[train_no]['price']*100
        print("Total amount : ",total_amt," for ",num_seats," tickets.")
        #ask user to select a payment method
        payment_methods=select_payment_method()
        
        if not payment_methods: 
            print("invalid payment method selection !")
            return
        #Create an ordern function
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
    
