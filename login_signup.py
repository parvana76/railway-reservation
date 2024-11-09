#dictionary to store user credentials
user_db={}
#function to sign up
def sign_up():
    username=input("Enter a new username:").strip()
    if username in user_db:
        print('Username already taken!\nPlease try again with a different one.')
    else:
        password=input("Create a password").strip()
        user_db[username]=password
        print("you have successfully registered!")
#function to sign in
def sign_in():
    username=input("Enter username:").strip()
    password=input("Enter password:").strip()
    #to check if username exists and password matches:
    if username in user_db and user_db[username]==password:
        print("Welcome back,",username,"!")
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
            
            
        
        
        
