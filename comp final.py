#basic data for trains
#2days prior-cancellation isnt possible
trains = [ {"train_id": 1, "name": "Express A", "o_d": ["station A","station B"], "seats": 100,"timings":['2pm-7pm','9pm-11am'],"days":['Mon','Tue','Fri'],"stations":["station A","station B","station C","station D"]},
{"train_id": 2, "name": "Express B", "o_d": ["station B","station C"], "seats": 150,"timings":['8pm-7am','8am-4pm'],"days":['Fri','Sat','Sun'],"stations":["station D","station E","station F","station G"]}]
#basic data for reservations
reservations = [{"reservation_id": 1, "train_id": 1, "passenger_name": "Sanjana", "seat_number": 1,'PNR status':'confirmed',"class":"EC","age":17,"sex":"F","zone":"normal","phone no.":'9911882277',"email id":"xyz@gmail.com",'date':[7,1,2025]},
                {"reservation_id": 2, "train_id": 1, "passenger_name": "Raman k", "seat_number": 23,'PNR status':'confirmed',"class":"2A","age":65,"sex":"M","zone":"normal","phone no.":'8811882277',"email id":"xyqz@gmail.com",'date':[7,1,2025]},
                {"reservation_id": 3, "train_id": 1, "passenger_name": "Ruhaan", "seat_number": 55,'PNR status':'waitlisted',"class":"2S","age":25,"sex":"M","zone":"normal","phone no.":'7211882277',"email id":"xz@gmail.com",'date':[7,1,2025]},
                {"reservation_id": 4, "train_id": 1, "passenger_name": "Srivalli", "seat_number": 20,'PNR status':'confirmed',"class":"3A","age":30,"sex":"F","zone":"ladies only","phone no.":'7811882277',"email id":"yz@gmail.com",'date':[8,1,2025]},
                {"reservation_id": 5, "train_id": 2, "passenger_name": "Rakshan", "seat_number": 1,'PNR status':'Waitlisted',"class":"CC","age":30,"sex":"M","zone":"normal","phone no.":'9911882333',"email id":"xyza@gmail.com",'date':[8,1,2025]},
                {"reservation_id": 6, "train_id": 2, "passenger_name": "mohamad", "seat_number": 3,'PNR status':'confirmed',"class":"CC","age":22,"sex":"M","zone":"normal","phone no.":'9911882836',"email id":"xysz@gmail.com",'date':[8,1,2025]},
                {"reservation_id": 7, "train_id": 2, "passenger_name": "Mridula", "seat_number": 40,'PNR status':'confirmed',"class":"FC","age":19,"sex":"M","zone":"normal","phone no.":'9914482277',"email id":"xyzk@gmail.com",'date':[8,1,2025]}]
#basic prices per class
classes={'1A':1940,'EC':1930,'2A':1150,'FC':950,'3A':815,'CC':665,'SL':315,'2S':180}
#stations
station=["station A","station B","Station C","station D","station E","station F","station G"]
# Admin functions
class_seats={'1A':[1,30],'EC':[31,50],'2A':[51,90],'FC':[91,125],'3A':[126,160],'CC':[161,200],'SL':[201,240],'2S':[240,300]}
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

def add_train(x):#to add trains
    print("Add a New Train:")
    train_id = len(trains) + 1
    name = input("Enter train name: ")
    o_d = input("Enter origin-destination: ")
    seats = int(input("Enter number of seats: "))
    timings=input("Enter timings:")
    days=input("Enter days of run:")
    stations=input("Enter stations:")
    trains.append({"train_id": train_id, "name": name, "o_d": o_d, "seats": seats,"timings":timings,"days":days,"stations":stations})
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
def edit_classprice(edit):#to edit the price
    print("\n1A\tFirst AC\tPrice: Rs.",edit['1A'],
          "\nEC\tExecutive Class\tPrice: Rs.",edit['EC'],
                      "\n2A\tSecond AC\tPrice: Rs.",edit['2A'],
                      "\nFC\tFirst Class\tPrice: Rs.",edit['FC'],
                      "\n3A\tThird AC\tPrice: Rs.",edit['3A'],
                      "\nCC\tChair Car\tPrice: Rs.",edit['CC'],
                      "\nSL\tSleeper\tPrice: Rs.",edit['SL'],
                      "\n2S\tSecond Seating\tPrice: Rs.",edit['2S'],"\n")
    Class=input("Enter preferred class(1A,EC,2A,FC,3A,CC,SL,2S):")
    new_amt=eval(input("Enter new amount:"))
    classes[Class]=new_amt
    print("Price of seat has been successfully edited!")

def admin_dashboard(st,edi):#main function
    print("Welcome to the Admin Dashboard")
    while True:
        print("\n--- Admin Dashboard ---")
        print("1. View Train Schedules")
        print("2. Add a New Train")
        print("3. View Reservations")
        print("4. Edit seat/class prices") 
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_trains()
        elif choice == "2":
            add_train(st)
        elif choice == "3":
            view_reservations()
        elif choice=="4":
            edit_classprice(edi)
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
    return payment_method.get(choice)


#Booking
def book_train(x):
    tot=0
    Total=0
    T={}
    dis=0
    inter=[]
    n=len(reservations)
    print("List Of Stations:")
    for i in x:
        print(i)
    origin=input('Enter origin:')
    destination=input('Enter Destination:')
    print("available trains:")
    flag=1
    for train in trains:
        if origin in train["stations"] and destination in train["stations"]:
            print(flag,"Train id:",train["train_id"],"\tName:",train["name"],'\tTimings:',train["timings"],"\tDays of run:",train["days"])

            flag=flag+1
    if flag==1:
        print("no trains available for the selected route.")
        return None
    else:
        id_=int(input("Enter the train id of your preferred train:"))
        for train in trains:
            if train["train_id"]==id_:
                print("1)",train["timings"][0],"\t2)",train["timings"][1])
                time=int(input('Enter prefferred timing (1/2):'))
                train_id=train["train_id"]
                print(train["days"])
                day=input("Enter the day you want to travel:")
                date=input("enter the date you want to travel(in a list)")
                passengers=int(input('Enter no. of passengers:'))
                if passengers<=train["seats"]:
                    global name
                    global res_id
                    for i in range(1,passengers+1):
                        print("passenger:",i)
                        name=str(input('Enter full name:'))
                        age=int(input('Enter age:'))
                        sex=str(input('Enter sex (M/F):'))
                        if sex.strip()=="F":
                            LOZ=str(input('''Would you like to book a seat in the ladies only zone? (Y/N)'''))
                            if LOZ==('Y' or 'y' or 'yes' or 'YES'):
                               zone='Ladies only zone'
                            else:
                                zone='Normal'
                        else:
                            zone='Normal'
                        print("\n1A\tFirst AC\tPrice: Rs.",classes['1A'],
          "\nEC\tExecutive Class\tPrice: Rs.",classes['EC'],
                      "\n2A\tSecond AC\tPrice: Rs.",classes['2A'],
                      "\nFC\tFirst Class\tPrice: Rs.",classes['FC'],
                      "\n3A\tThird AC\tPrice: Rs.",classes['3A'],
                      "\nCC\tChair Car\tPrice: Rs.",classes['CC'],
                      "\nSL\tSleeper\tPrice: Rs.",classes['SL'],
                      "\n2S\tSecond Seating\tPrice: Rs.",classes['2S'],"\n")
    Class=input("Enter preferred class(1A,EC,2A,FC,3A,CC,SL,2S):")
                    
                        for c in classes.keys():
                            if c==Class:
                                Total=Total+classes[c]
                        pno=input('''Enter phone number:''')
                        if len(pno)<10 or len(pno)>10:
                            print("invalid phone number.")
                            pno=input('''Enter phone number:''')
                            
                        e_id=str(input('''Enter email id:'''))
                        if age<=5:
                            dis=100
                        elif age<=12:
                            dis=50
                        #Here add payment integration
                        res_id=reservations[n-1]['reservation_id']+1
                        print("available seats:")
                        for k in range(class_seats[Class][0],class_seats[Class][1]+1):
                            for l in reservations:
                                if l["train_id"]==id_:
                                    if l["seat_number"]==k:
                                        continue
                                    else:
                                        print(k,end=",")
                                        break
                        seatno=int(input("\nSelect a seat number from above:"))
                        T={'passenger_name':name,'date':date,'age':age,'sex':sex,"zone":zone,'class':Class,'reservation_id':res_id,'Seat_Number':seatno,"phone no.":pno,"email id":e_id,"train_id":id_}
                        inter.append(T)

                tot=Total+100-dis
                print('Total price: ','Rs.',tot)
                s=str(input('Proceed with payment? (Y/N)'))
                if s==('Y' or 'y' or 'Yes' or 'YES' or 'yes'):
                    select_payment_method()
                #simulating payemnt success (In real life scenario , payment status will come from the RAZORPAY API response and will send signal)
                    print("BILL:\nPASSENGER DETAILS:\n",inter,"\nDiscount:",dis,"\nTax:100","\nTotal:",tot)
                    print('PAYMENT SUCCESSFUL')   #printing bill
                    for q in inter:
                        q["PNR status"]="confirmed"
                        reservations.append(q)
                        train["seats"]-=passengers

                       
def pnr_check():
    t=int(input("Enter train id"))
    r=int(input("Enter Reservation id"))
    for pnr in reservations:
        if pnr['reservation_id']==r and pnr["train_id"]==t:
            print('PNR status:',pnr['PNR status'])
            break
    else:
        print('Reservation id invalid')


def cancel():
    t=int(input("Enter train id"))
    r=int(input("Enter reservation id"))
    date=input("enter todays date(in a list):")
    for pnr in reservations:
        if pnr['reservation_id']==r and pnr["train_id"]==t:
            if pnr['date']==date:
                print("Cancellation not possible")
                break
            elif (pnr['date'][0]-date[0])<=2:
                print("Cancellation not possible")
                break
            elif date[0]>pnr['date'][0]:
                print("Cancellation not possible")
                break
            elif date[1]>pnr['date'][1]:
                print("Cancellation not possible")
                break
            else:
                del reservations[pnr]
                print('Your ticket has been cancelled')
                break
    else:
        print('Reservation id invalid')
    for train in trains:
        if train["train_id"]==t:
            train["seats"]-=1
    

def user_dashboard(st):
    print("Welcome to the User Dashboard")
    while True:
        #User menu
        print("\n--- User Dashboard ---")
        choice=int(input('Enter your choice: (1,2,3,4,5)\n1.Check availabe trains\n2.Book a train\n3.Check PNR status\n4.Cancel ticket\n5.Exit\n'))
        T={}
        Total=0
        if choice==1:
            view_trains()
        elif choice==2:
            book_train(st)
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
def hide_pass(password):
    x=''
    for i in password:
        x=x+"*"
    return x
#function to sign up
def sign_up(sta):
    username=input("Enter a new username:").strip()
    if username not in user or admin:
        password=input("Create a password:").strip()
        hidden_pass=hide_pass(password)
        print("password:",hidden_pass,end="\n")
        user[username]=password
        print("you have successfully registered!")
        user_dashboard(sta)
    else:
        print('Username already taken!\nPlease try again with a different one.')

#function to sign in
def sign_in(sta,ed):
    username=input("Enter username:").strip()
    password=input("Enter password:").strip()
    hidden_pass=hide_pass(password)
    print("password:",hidden_pass,end="\n")
    #to check if username exists and password matches:
    if username in user and user[username]==password:
        print("Welcome back,",username,"!")
        user_dashboard(sta)
    if username in admin and admin[username]==password:
        print("Welcome back,",username,"!")
        admin_dashboard(sta,ed)
    else:
        print("Invalid username or password. Please try again.")
while True:
        print("Welcome to railway reservation System!")
        ch=input("Are you an admin or user?\n(a)Admin\n(b)User\n")
        if ch=='b':
            choice=input("Enter Your choice(1,2 or 3):\n1)Sign In\n2)Sign Up\n3)exit\n")
            if choice=="1":#sign in
                sign_in(station,classes)
            elif choice == "2":  # Sign Up
                sign_up(station)
            elif choice == "3":  # Exit
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        elif ch=='a':
            choice=input("Enter Your choice(1,2):\n1)Sign In\n2)exit\n")
            if choice=="1":#sign in
                sign_in(station,classes)
            elif choice == "2":  # Exit
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        else:
            print("Invalid choice. Please select 'a' or 'b'.")

    
       



