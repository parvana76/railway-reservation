import mysql.connector as ms
mycon=ms.connect(host='localhost',user='root',password='cajc',database='railco')
mycur=mycon.cursor()

from datetime import date

#basic data for trains
trains = [ {"train_id": 1, "name": "Express A", "o_d": ["station A","station B"], "seats": 100,"timings":['2pm-7pm','9pm-11am'],"days":['Mon','Tue','Fri'],"stations":["station A","station B","station C","station D"]},
{"train_id": 2, "name": "Express B", "o_d": ["station B","station C"], "seats": 150,"timings":['8pm-7am','8am-4pm'],"days":['Fri','Sat','Sun'],"stations":["station D","station E","station F","station G"]}]
#basic data for reservations
reservations = [{"reservation_id": 1, "train_id": 1, "passenger_name": "Sanjana", "seat_number": 1,'PNR status':'confirmed',"class":"EC","age":17,"sex":"F","zone":"normal","phone no.":'9911882277',"email id":"xyz@gmail.com",'date':"2025-04-02","timing":'2pm-7pm'},
                {"reservation_id": 2, "train_id": 1, "passenger_name": "Raman k", "seat_number": 23,'PNR status':'confirmed',"class":"2A","age":65,"sex":"M","zone":"normal","phone no.":'8811882277',"email id":"xyqz@gmail.com",'date':"2025-04-12","timing":'2pm-7pm'},
                {"reservation_id": 3, "train_id": 1, "passenger_name": "Ruhaan", "seat_number": 55,'PNR status':'waitlisted',"class":"2S","age":25,"sex":"M","zone":"normal","phone no.":'7211882277',"email id":"xz@gmail.com",'date':"2025-05-06","timing":'8am-4pm'},
                {"reservation_id": 4, "train_id": 1, "passenger_name": "Srivalli", "seat_number": 20,'PNR status':'confirmed',"class":"3A","age":30,"sex":"F","zone":"ladies only","phone no.":'7811882277',"email id":"yz@gmail.com",'date':"2025-05-06","timing":'8am-4pm'},
                {"reservation_id": 5, "train_id": 2, "passenger_name": "Rakshan", "seat_number": 1,'PNR status':'Waitlisted',"class":"CC","age":30,"sex":"M","zone":"normal","phone no.":'9911882333',"email id":"xyza@gmail.com",'date':"2025-05-06","timing":'8am-4pm'},
                {"reservation_id": 6, "train_id": 2, "passenger_name": "mohamad", "seat_number": 3,'PNR status':'confirmed',"class":"CC","age":22,"sex":"M","zone":"normal","phone no.":'9911882836',"email id":"xysz@gmail.com",'date':"2025-06-05","timing":'8am-4pm'},
                {"reservation_id": 7, "train_id": 2, "passenger_name": "Mridula", "seat_number": 40,'PNR status':'confirmed',"class":"FC","age":19,"sex":"M","zone":"normal","phone no.":'9914482277',"email id":"xyzk@gmail.com",'date':"2025-05-09","timing":'8am-4pm'}]
#basic prices per class
classes={'1A':1940,'EC':1930,'2A':1150,'FC':950,'3A':815,'CC':665,'SL':315,'2S':180}
#stations
station=["station A","station B","station C","station D","station E","station F","station G"]
# Admin functions
class_seats={'1A':[1,30],'EC':[31,50],'2A':[51,90],'FC':[91,125],'3A':[126,160],'CC':[161,200],'SL':[201,240],'2S':[240,300]}

def view_trains():#to view trains
    print("\nTrain Schedules:")
    
    mycur.execute("select*from trains")
    dat=mycur.fetchall()
   
    for tid,name,og,ds,seats in dat:
        
        print("id:",tid," \tname:",name," \torigin:",og," \tdestination:",ds," \tseats:",seats,sep=' ')

passengers=0
T={}
Class=0
name=''
res_id=0
from datetime import datetime
def add_train(x):#to add trains
    print("Add a New Train:")
    mycur.execute('select train_id from trains')
    t1=mycur.fetchall()
    train_id =t1[len(t1)-1][0]+1
    n=t1[len(t1)-1][0]
    name = input("Enter train name: ")
    o=input("Enter origin: ")
    d=input("Enter destination: ")
    seats = int(input("Enter number of seats: "))
    n=int(input("enter no. of stations:"))
    mycur.execute('select*from stations')
    dat=mycur.fetchall()
    q6="insert into stations(train_id) values(%s)"%(train_id)
    mycur.execute(q6)
    mycon.commit()
    for i in range(1,n+1):
        x='s'+str(i)
        st=input("enter station:")
        q5="update stations set %s='%s' where train_id=%s"%(x,st,train_id)
        mycur.execute(q5)
        mycon.commit()
    mycur.execute('select*from stations')
    stations=mycur.fetchmany(n)
    station=mycur.fetchone()
    
    mycur.fetchall()
    mycur.execute("select*from timings")
    we=mycur.fetchall()
    
    q6="insert into timings(train_id) values(%s)"%(train_id)
    mycur.execute(q6)
    mycon.commit()
    for i in range(1,n+1):
        x='s'+str(i)
       
        tm=input("enter time of arrival(hh:mm am/pm):")
        tms=datetime.strptime(tm, '%I:%M %p')
        timing=tms.strftime('%H:%M:%S')
        q5="update timings set %s='%s' where train_id=%s"%(x,timing,train_id)
        mycur.execute(q5)
        mycon.commit()
    days=['mon','tue','wed','thu','fri','sat','sun']
    mycur.execute("select*from tdays")
    we=mycur.fetchall()
    q6="insert into tdays(train_id) values(%s)"%(train_id)
    mycur.execute(q6)
    mycon.commit()
    for i in days:
        print("day:",i)
        yn=input("does the train run?(yes,no)")
        if yn=='yes':
            q5="update tdays set %s='%s' where train_id=%s"%(i,'yes',train_id)
            mycur.execute(q5)
            mycon.commit()
        else:
            continue
        
    q5="insert into trains values(%s,'%s','%s','%s',%s)"%(train_id,name,o,d,seats)
    mycur.execute(q5)
    mycon.commit()
    print("Train has been successfully added!")
def del_train():
    tid=int(input("enter train id"))
    yn=(input("are you sure you want to delete(y/n)")).lower()
    if yn=='y':
         mycur.execute('select train_id from trains')
         q5="delete from trains where train_id=%s"%(tid)
         mycur.execute(q5)
         mycon.commit()
         mycur.execute('select train_id from stations')
         q5="delete from stations where train_id=%s"%(tid)
         mycur.execute(q5)
         mycon.commit()
         mycur.execute('select train_id from seats')
         q5="delete from seats where train_id=%s"%(tid)
         mycur.execute(q5)
         mycon.commit()
         mycur.execute('select train_id from tdays')
         q5="delete from tdays where train_id=%s"%(tid)
         mycur.execute(q5)
         mycon.commit()
         mycur.execute('select train_id from timings')
         q5="delete from timings where train_id=%s"%(tid)
         mycur.execute(q5)
         mycon.commit()
         
         print("Train has successfully been removed!!!")
         
    
         
    
def view_reservations():#to view reservations
    idtrain=eval(input("Enter train id:"))
    print("Reservations List:")
    mycur.execute("select*from trains")
    t=mycur.fetchall()
    
    for train in t:
            if train[0]==idtrain:
                train_name=train[1]
                print("Train Id:",idtrain,"\t\tTrain name:",train_name,"\n")
                print('Reservation ID\t|\tName\t\t|\tSeat number\t|\tPNR status\t|\tClass\n')
                break
    else:
        print("train not found")
    mycur.execute("select*from res")
    r=mycur.fetchall()
    for reservation in r:
        if reservation[1]==idtrain:
            print(reservation[0],'\t\t|\t',reservation[2],'\t|\t',reservation[3],"\t\t|\t",reservation[4],"\t|\t",reservation[5])
#classes={'1AC':1940,'EC':1930,'2A':1150,'FC':950,'3A':815,'CC':665,'SL':315,'2S':180}
def edit_classprice(edit):#to edit the price
    mycur.execute("select*from sprice")
    r=list(mycur.fetchall()[0])
    print("\n1AC\tFirst AC\tPrice: Rs.",r[0],
          "\nEC\tExecutive Class\tPrice: Rs.",r[1],
                      "\n2A\tSecond AC\tPrice: Rs.",r[2],
                      "\nFC\tFirst Class\tPrice: Rs.",r[3],
                      "\n3A\tThird AC\tPrice: Rs.",r[4],
                      "\nCC\tChair Car\tPrice: Rs.",r[5],
                      "\nSL\tSleeper\tPrice: Rs.",r[6],
                      "\n2S\tSecond Seating\tPrice: Rs.",r[7],"\n")
    Class=input("Enter preferred class(1AC,EC,2A,FC,3A,CC,SL,2S):")
    new_amt=int(input("Enter new amount:"))
    q5="update sprice set %s=%s"%(Class,new_amt)
    mycur.execute(q5)
    mycon.commit()
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

#date

def datefn():
    today=date.today()
    year=today.year
    q=True
    while q==True:
        month = int(input('Select Month:(1-12)\n1)January\t2)February\n3)March\t\t4)April\n5)May\t\t6)June\n7)July\t\t8)August\n9)September\t10)October\n11)November\t12)December\nmonth:'))
        if month>12 or month<1:
            print("invalid value")
            continue
        else:
            break
    if month==2:
        day = int(input('Select Day:\nMo\tTu\tWe\tTh\tFr\tSa\tSu\n1\t2\t3\t4\t5\t6\t7\n8\t9\t10\t11\t12\t13\t14\n15\t16\t17\t18\t19\t20\t21\n22\t23\t24\t25\t26\t27\t28\nday:'))
    elif month in(1,3,5,7,8,10,12):
        day = int(input('Select Day:\nMo\tTu\tWe\tTh\tFr\tSa\tSu\n1\t2\t3\t4\t5\t6\t7\n8\t9\t10\t11\t12\t13\t14\n15\t16\t17\t18\t19\t20\t21\n22\t23\t24\t25\t26\t27\t28\n29\t30\t31\nday:'))
    else:
        day = int(input('Select Day:\nMo\tTu\tWe\tTh\tFr\tSa\tSu\n1\t2\t3\t4\t5\t6\t7\n8\t9\t10\t11\t12\t13\t14\n15\t16\t17\t18\t19\t20\t21\n22\t23\t24\t25\t26\t27\t28\n29\t30\nday:'))
     
    travel_date = date(year,month,day)
    delta=travel_date-today
    if delta.days>60:
        print("You can only book the ticket max 60 days prior\nkindly choose a new date!!\n")
        datefn()
    if delta.days<1:
        print("cannot book to this date!!")
        datefn()
    else:
        return travel_date

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
            print(flag,")","Train id:",train["train_id"],"\t\tName:",train["name"],'\tTimings:',train["timings"],"\tDays of run:",train["days"])

            flag=flag+1
    if flag==1:
        print("no trains available for the selected route.")
        return None
    else:
        id_=int(input("Enter the train id of your preferred train:"))
        for train in trains:
            if train["train_id"]==id_:
                trav_date=datefn()
                if trav_date.day not in train["days"]:
                    print("train not available for selected day")
                    trav_date=datefn()
                print("1)",train["timings"][0],"\t2)",train["timings"][1])
                time=int(input('Enter prefferred timing (1/2):'))
                timing=train["timings"][time-1]
                train_id=train["train_id"]
                day=trav_date.day
                passengers=int(input('Enter no. of passengers:'))
                if passengers<=train["seats"]:
                    global name
                    global res_id
                    for i in range(1,passengers+1):
                        print("passenger:",i)
                        name=str(input('Enter full name:'))
                        if name.isdigit()==True or name.isalpha==False:
                            print("invalid name")
                            name=str(input('Enter full name:'))
                        age=int(input('Enter age:'))
                        if isinstance(age,int)==False or age<1 or age>190:
                            print("invalid age")
                            age=int(input('Enter age:'))
                            
                            
                        sex=str(input('Enter sex (M/F):'))
                        if sex.strip()=="F":
                            LOZ=str(input('Would you like to book a seat in the ladies only zone? (Y/N)'))
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
                        pno=input('Enter phone number:')
                        if len(pno)<10 or len(pno)>10:
                            print("invalid phone number.")
                            pno=input('Enter phone number:')
                            
                        e_id=str(input('Enter email id:'))
                        if e_id.endswith("@gmail.com")==False:
                             print("invalid email id.")
                             e_id=input('Enter email id:')
                
                        if age<=5:
                            dis=100
                        elif age<=12:
                            dis=50
                      
                        res_id=reservations[n-1]['reservation_id']+1
                        print("available seats:")
                        for k in range(class_seats[Class][0],class_seats[Class][1]+1):
                            for l in reservations:
                                if l["train_id"]==id_:
                                    if l["seat_number"]==k:
                                        continue
                                    for res in reservations:
                                        if date(res["date"])==trav_date:
                                            if res["timings"]==timing:
                                                continue;
                                        
                                            
                                    else:
                                        print(k,end=",")
                                        break
                        seatno=int(input("\nSelect a seat number from above:"))
                        T={'passenger_name':name,'date':date,'timing':timing,'age':age,'sex':sex,"zone":zone,'class':Class,'reservation_id':res_id,'seat_Number':seatno,"phone no.":pno,"email id":e_id,"train_id":id_}
                        inter.append(T)

                tot=Total-(Total)*(dis/100)+100
                print('Total price: ','Rs.',tot)
                m=True
                while m==True:
                    s=str(input('Proceed with payment? (Y/N)'))
                    if s==('Y' or 'y' or 'Yes' or 'YES' or 'yes'):
                        select_payment_method()
                        m=False
                    else:
                        print("invalid choice!")
                        u=input("do you want to exit?(Y/N)")
                        if u=='Y':
                            m=False
                    
                #simulating payemnt success (In real life scenario , payment status will come from the RAZORPAY API response and will send signal)
                    #printing bill
                    print("BILL:\nPASSENGER DETAILS:")
                    for x in inter:
                        print("passenger name:",x['passenger_name'],"\treservation id:",x['reservation_id'],"\tzone:",x['zone'],"\tseat no.:",x["seat_Number"],"\tdate:",x['date'])
                    print("\nDiscount:",dis,"%","\nTax:100","\nTotal:",tot)
                    print('PAYMENT SUCCESSFUL')
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
    date=eval(input("enter todays date(in a list):"))
    for pnr in reservations:
        if pnr['reservation_id']==r and pnr["train_id"]==t:
            x=pnr['date']
            y=x[0]
            z=x[1]
            if x==date:
                print("Cancellation not possible")
                break
            elif (y-date[0])<=2:
                print("Cancellation not possible")
                break
            elif date[0]>y:
                print("Cancellation not possible")
                break
            elif date[1]>z:
                print("Cancellation not possible")
                break
            else:
                reservations.remove(pnr)
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
        choice=int(input('Enter your choice: (1-5)\n1.Check availabe trains\n2.Book a train\n3.Check PNR status\n4.Cancel ticket\n5.Exit\n'))
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
    q5='select username from userlog'
    mycur.execute(q5)
    username=input("Enter a new username:").strip()
    if username not in mycur.fetchall():
        password=input("Create a password:").strip()
        if len(password)<10:
            print("create a stronger password")
            password=input("Create a password:").strip()   
        hidden_pass=hide_pass(password)
        print("password:",hidden_pass,end="\n")
        q5="insert into userlog values('%s','%s','%s')"%(username,password,'user')
        mycur.execute(q5)
        mycon.commit()
        print("you have successfully registered!")
        user_dashboard(sta)
    else:
        print('Username already taken!\nPlease try again with a different one.')

#function to sign in
def sign_in(sta,ed):
    q5='select* from userlog'
    mycur.execute(q5)
    username=input("Enter username:").strip()
    password=input("Enter password:").strip()
    hidden_pass=hide_pass(password)
    print("password:",hidden_pass,end="\n")
    #to check if username exists and password matches:

    #if username in user and user[username]==password:
    da=mycur.fetchall()
    if (username,password,'user') in da:    
        print("Welcome back,",username,"!")
        user_dashboard(sta)
    if (username,password,'admin') in da:
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


    
       



