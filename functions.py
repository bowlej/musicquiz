import random
#Opening the files i need to read, using 'with open' this will close the files at the end of the quiz
#Songs
with open('Songs.txt', 'r') as songsfilecontents:
    list_of_songs = songsfilecontents.readlines()
#Bands
with open('bands.txt', 'r') as bandsfilecontents:
    list_of_bands = bandsfilecontents.readlines()
#Year
with open('yearofsong.txt', 'r') as yearfilecontents:
    list_of_years = yearfilecontents.readlines()

#Creating a random number to use to get a song and band
random_number = random.randint(0, 7)
#Getting a random song
random_song = list_of_songs[random_number]
#Removing any whitespace after the random song
random_song = random_song.rstrip("\n")
#Getting a matching random band
random_band = list_of_bands[random_number]
#Getting the matching year of the song
random_year = list_of_years[random_number]
#Getting the intials of the random song
song_initails = "".join(item[0].upper() for item in random_song.split())

#Functions
def check_password(u_name, p_word):
    if u_name == "John" and p_word == "musicquiz":
        print("Welcome John")
        return "login_ok"
    elif u_name == "Jules" and p_word == "musicquiz1":
        print("Welcome Jules")
        return "login_ok"

def login():
    while True:
        print("Welcome to the music quiz, please enter your username")
        #Creating an input for the user name
        u_name = input("User Name: ")
        print("Now please enter your password:")
        #Create an input for the password
        p_word = input("Password: ")
        #Checking that its a know user and password combo
        login = check_password(u_name, p_word)
        if login == "login_ok":
            break
        else:
            print("Sorry you dont have a valid user / password, please try again")
    return u_name

def save_score(score, user):
    #Making a dict to save the current user and score
    a_dictionary = {user: score}
    #Appending the dict to a txt file
    with open('scores.txt', 'a') as fp:
        print(a_dictionary, file=fp)
        #fp.write(json.dumps(a_dictionary, indent=4))

def read_scores(file):
    d = {}
    s = open(file, 'r')
    print("The current list of all players and scores are:")
    for line in s:
        (user, score) = line.split()
        d[user] = score
        print(user, score)

def musicQuiz(user):
    points = 3
    print("Can you guess the name of the song with just the intials and the band name?, you will have 3 trys")
    print("The initals of the song are", song_initails, "the band name is", random_band,)
    clue = input("Would you like a clue?, if so type clue, if not type no ")
    if (clue == 'clue'):
        print("the year the song was released was", random_year)
    #Adding an input for the user to guess the song
    guess_the_song = input("Guess the name of the song! ")
    #Setting the number of trys to 3
    number_of_trys_left = 2
    #Defining a wrong answer
    wrong_answer = (guess_the_song != random_song)
    #Starting the quiz answer trys
    while number_of_trys_left > 0 and wrong_answer:
        guess_the_song = input("Thats wrong sorry, please try again! ")
        points -= 1
        #adding a used try
        number_of_trys_left -= 1
        wrong_answer = (guess_the_song != random_song)
    #Getting it wrong
    if wrong_answer:
        print ("Thats wrong you clown!, you have had your 3 trys now go away!")
    #Getting it right
    else:
        #Getting the final score
        final_score = points
        #Saving the final score and the user that played the quiz in a text file
        save_score(final_score, user)
        print("Ohh look at you knowing the right band!, well done!")
        print("You scored {0} point/s".format(final_score))
        read_scores('scores.txt')