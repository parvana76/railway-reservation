#basic data for trains
trains = [ {"train_id": 1, "name": "Express A", "o_d": ["station A","station B"], "seats": 100,"timings":['2pm-7pm','9pm-11am'],"days":['Mon','Tue','Fri'],"stations":["station A","station B","station C","station D"]},
{"train_id": 2, "name": "Express B", "o_d": ["station B","station C"], "seats": 150,"timings":['8pm-7am','8am-4pm'],"days":['Fri','Sat','Sun'],"stations":["station D","station E","station F","station G"]}]
#basic data for reservations
reservations = [{"reservation_id": 1, "train_id": 1, "passenger_name": "Sanjana", "seat_number": 1,'PNR status':'confirmed',"class":"EC"},
                {"reservation_id": 2, "train_id": 1, "passenger_name": "Raman kk", "seat_number": 23,'PNR status':'confirmed',"class":"2A"},
                {"reservation_id": 3, "train_id": 1, "passenger_name": "Ruhaan", "seat_number": 55,'PNR status':'waitlisted',"class":"2S"},
                {"reservation_id": 4, "train_id": 1, "passenger_name": "Shambavi", "seat_number": 20,'PNR status':'confirmed',"class":"3A"},
                {"reservation_id": 1, "train_id": 2, "passenger_name": "Rakshan", "seat_number": 1,'PNR status':'Waitlisted',"class":"CC"},
                {"reservation_id": 2, "train_id": 2, "passenger_name": "Mohamed", "seat_number": 3,'PNR status':'confirmed',"class":"CC"},
                {"reservation_id": 3, "train_id": 2, "passenger_name": "Onnikrishnan", "seat_number": 40,'PNR status':'confirmed',"class":"FC"}]
#basic prices per class
classes={'1A':1940,'EC':1930,'2A':1150,'FC':950,'3A':815,'CC':665,'SL':315,'2S':180}
# Admin functions

def view_trains():#to view trains
    print("\nTrain Schedules:")
    print('Train ID|\tName\t\t|\tOrigin-Destination\t\t|\tSeats Available\t|\tTimings\t\t\t|\tDays of run\n')
    for train in trains:
        print(train['train_id'],'\t|\t',train['name'],'\t|\t',train['o_d'],'\t|\t',train['seats'],'\t\t|\t',train['timings'],
              '\t|\t',train['days'],"\n",sep='')
passengers=0
T={}
Class=0
name=''
res_id=0

def add_train():#to add trains
    print("Add a New Train:")
    train_id = len(trains) + 1
    name = input("Enter train name: ")
    o_d = input("Enter origin-destination: ")
    seats = int(input("Enter number of seats: "))
    timings=input("Enter timings:")
    days=input("Enter days of run:")
    trains.append({"train_id": train_id, "name": name, "o_d": o_d, "seats": seats,"timings":timings,"days":days})
    print("Train has been successfully added!")
    
def view_reservations():#to view reservations
    idtrain=eval(input("Enter train id:"))
    print("Reservations List:")
    for train in trains:
            if train["train_id"]==idtrain:
                train_name=train["name"]
                print("Train Id:",idtrain,"\t\tTrain name:",train_name,"\n")
                print('Reservation ID\t|\tName\t\t|\tSeat number\t|\tPNR status\t|\tClass\n')
                break
    else:
        print("train not found")
    for reservation in reservations:
        if reservation["train_id"]==idtrain:
            print(reservation['reservation_id'],'\t\t|\t',reservation['passenger_name'],'\t|\t',reservation['seat_number'],"\t\t|\t",reservation['PNR status'],"\t|\t",reservation["class"])
classes={'1A':1940,'EC':1930,'2A':1150,'FC':950,'3A':815,'CC':665,'SL':315,'2S':180}
def edit_classprice():#to edit the price
    Class=input('''Enter preferred class:
         1A     Price: Rs.1940
         EC     Price: Rs.1930
         2A     Price: Rs.1150
         FC     Price: Rs.950
         3A     Price: Rs.815
         CC     Price: Rs.665
         SL     Price: Rs.315
         2S     Price: Rs.180\n''')
    new_amt=eval(input("Enter new amount:"))
    classes[Class]=new_amt
    print("Price of seat has been successfully edited!")

def admin_dashboard():#main function
    print("Welcome to the Admin Dashboard")
    while True:
        print("\n--- Admin Dashboard ---")
        print("1. View Train Schedules")
        print("2. Add a New Train")
        print("3. View Reservations")
        print("4. Edit seat/class prices") 
        print("5. Exit")
        
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_trains()
        elif choice == "2":
            add_train()
        elif choice == "3":
            view_reservations()
        elif choice=="4":
            edit_classprice()
        elif choice == "5":
            print("Exiting Admin Dashboard...")
            break
        else:
            print("Invalid choice. Please try again.")
#user functions
            #select payment function
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


#Booking
def book_train():
    tot=0
    Total=0
    n=len(reservations)
    origin=str(input('''Enter origin:
    '''))
    destination=str(input('''Enter Destination
    '''))
    for train in trains:
        if train["origin"]==origin.strip() and train["destination"]==destination.strip():
            print('Train details for',train["name"],':',"\nTimings:",train["timings"],"\tDate:",train["date"])
            time=int(input('''Enter prefferred timing (1/2)
            '''))
            train_id=train["train_id"]
            passengers=int(input('''Enter no. of passengers
            '''))
            if passengers<=train["seats"]:    
                global name
                global res_id
                for i in range(1,passengers+1):
                    name=str(input('''Enter full name:'''))
                    age=int(input('''Enter age:'''))
                    sex=str(input('''Enter sex (M/F):'''))
                    if sex.strip()=="F":
                        LOZ=str(input('''Would you like to book a seat in the ladies only zone? (Y/N)'''))
                        if LOZ==('Y' or 'y' or 'yes' or 'YES'):
                            zone='Ladies only zone'
                        else:
                            zone='Normal'
                    else:
                        zone='Normal'
                    Class=int(input('''select class:
1) 1A     Price: Rs.1940
2) SL     Price: Rs.665
3) CC     Price: Rs.315
4) 2S     Price: Rs.180
'''))

                    for c in classes:
                        if c==Class:
                            Total=Total+classes[c]
                    T['Passenger'+str(i)]={'Name':name,'Age':age,'Sex':sex,'Zone':zone,'Class':Class}

                pno=int(input('''Enter phone number'''))
                e_id=str(input('''Enter email id'''))
                T['collective details']={'Phone':pno,'Email':e_id}
                #Here add payment integration
                res_id=reservations[n-1]['reservation_id']+1
                seatno=reservations[n-1]["seat_number"]+1
                fullseat=str(seatno)+'-'+str(Class)
                T['collective details'].update({'reservationid':res_id,'Seat':fullseat,'Price':Total})
                tot=Total+100
                print('Total price: ','Rs.',tot)
                s=str(input('Proceed with payment? (Y/N)'))
                if s==('Y' or 'y' or 'Yes' or 'YES' or 'yes'):
                    select_payment_method()
                #simulating payemnt success (In real life scenario , payment status will come from the RAZORPAY API response and will send signal)
                    print('''               BILL:
               Total:  Rs.{}
               PASSENGER DETAILS:
               {}'''.format(tot,T))
                    print('PAYMENT SUCCESSFUL, Booking confirmed for',name,'under reservation id',res_id)   #printing bill and dictionary w details
                    reservations.append({"reservation_id": n+1, "train_id":train_id, "passenger_name": name, "seat_number":seatno,'PNR status':'confirmed'})
            else:
                print('No seats available for the selected train.')
                
            break
    else:
        print("No trains available for the selected route.")
def pnr_check():
    r=int(input('''Enter Reservation id
    '''))
    for pnr in reservations:
        if pnr['reservation_id']==r:
            print('PNR status:',pnr['PNR status'])
            break
    else:
        print('Reservation id invalid')


def cancel():
      r=int(input('''Enter reservation id
      '''))
      for pnr in reservations:
          if pnr['reservation_id']==r:
              pnr['PNR status']=['Cancelled']
              print('Your ticket has been cancelled')
              break
      else:
          print('Reservation id invalid')

def user_dashboard():
    print("Welcome to the User Dashboard")
    while True:
        #User menu
        choice=int(input('Enter your choice: (1,2,3,4,5)\n1.Check availabe trains\n2.Book a train\n3.Check PNR status\n4.Cancel ticket\n5.Exit\n'))
        T={}
        Total=0
        if choice==1:
            view_trains()
        elif choice==2:
            book_train()
        elif choice==3:
            pnr_check()
        elif choice==4:
            cancel()
        elif choice==5:
            print("Exiting User Dashboard...")
            break
        else:
            print("Invalid choice. Please try again.")

#dictionary to store user credentials
user={'user1':'railwayuser'}
admin={"railwayadmin":"12345"}#username:password for admin
#to hide the pasword
#function to sign up
def sign_up():
    username=input("Enter a new username:").strip()
    if username not in user or admin:
        password=input("Create a password:").strip()
        user[username]=password
        print("you have successfully registered!")
        user_dashboard()
    else:
        print('Username already taken!\nPlease try again with a different one.')
def hide_pass(password):
    x=''
    for i in password:
        x=x+"*"
    return x
#function to sign in
def sign_in():
    username=input("Enter username:").strip()
    password=input("Enter password:").strip()
    hidden_pass=hide_pass(password)
    print("password:",hidden_pass,end="\n")
    #to check if username exists and password matches:
    if username in user and user[username]==password:
        print("Welcome back,",username,"!")
        user_dashboard()
    if username in admin and admin[username]==password:
        print("Welcome back,",username,"!")
        admin_dashboard()
    else:
        print("Invalid username or password. Please try again.")
while True:
        print("Welcome to railway reservation System!")
        ch=input("Are you an admin or user?\n(a)Admin\n(b)User\n")
        if ch=='b':
            choice=input("Enter Your choice(1,2 or 3):\n1)Sign In\n2)Sign Up\n3)exit\n")
            if choice=="1":#sign in
                sign_in()
            elif choice == "2":  # Sign Up
                sign_up()
            elif choice == "3":  # Exit
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        elif ch=='a':
            choice=input("Enter Your choice(1,2):\n1)Sign In\n2)exit\n")
            if choice=="1":#sign in
                sign_in()
            elif choice == "2":  # Exit
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        else:
            print("Invalid choice. Please select 'a' or 'b'.")

    
       



