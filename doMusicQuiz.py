import functions
import json

def login(usr):
    print("Welcome to the music quiz, please login if you have already registered, if not add a user and password and those details will be registered for you to use next time")

    #Asking for Name
    uN = input("Name: ")
    #Asking for Password
    pW = input("Password: ")

    #Checking if Name and password are already in the user file
    if uN in usr.keys():
        if pW == usr[uN]:
            print("Welcome back {0}".format(uN))
        else:
            print("Incorrect password.")
            #Try login again
            return False
    #If username not found add that and password to the users file
    else:
        print("Hello, {0} Thanks for registering and enjoy the quiz".format(uN))
        #Add new username with password
        usr[uN] = pW
        #Add the new username with password to the users file
        functions.writeUsers(usr)
    #Run the quiz, passing the username being used
    functions.musicQuiz(uN)
    return True

def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

#Read users from the users file
users = readUsers()

#Check if entered username and password are already in the users.json file
success = login(users)
while not success:
    success = login(users)
