#dictionary to store user credentials
user={}
admin={"railwayadmin":"12345"}#username:password for admin
#function to sign up
def sign_up():
    username=input("Enter a new username:").strip()
    if username in user or admin :
        print('Username already taken!\nPlease try again with a different one.')
    else:
        password=input("Create a password").strip()
        user[username]=password
        print("you have successfully registered!")
#function to sign in
def sign_in():
    username=input("Enter username:").strip()
    password=input("Enter password:").strip()
    #to check if username exists and password matches:
    if username in user and user[username]==password:
        print("Welcome back,",username,"!")
        #userdashboard add
    if username in admin and admin[username]==password:
        print("Welcome back,",username,"!")
        #add admin dashboard
    else:
        print("Invalid username or password. Please try again.")
#main function:
def main():
    while True:
        print("Welcome to railway reservation System!")
        choice=input("Enter Your choice(1,2 or 3):\n1)Sign In\n2)Sign Up\n3)exit\n")
        if choice=="1":#sign in
            sign_in()
            break
        elif choice == "2":  # Sign Up
            sign_up()
            break
        
        elif choice == "3":  # Exit
            print("Exiting the system...")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
if __name__ == "__main__":
    main()
            
            
        
        
        
