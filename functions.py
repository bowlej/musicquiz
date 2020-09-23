import random
import json


# Opening the files i need to read, using 'with open' this will close the files at the end of the quiz
# Songs
with open('Songs.txt', 'r') as songsfilecontents:
    list_of_songs = songsfilecontents.readlines()
# Bands
with open('bands.txt', 'r') as bandsfilecontents:
    list_of_bands = bandsfilecontents.readlines()
# Year
with open('yearofsong.txt', 'r') as yearfilecontents:
    list_of_years = yearfilecontents.readlines()

# Creating a random number to use to get a song and band
random_number = random.randint(0, 7)
# Getting a random song
random_song = list_of_songs[random_number]
# Removing any whitespace after the random song
random_song = random_song.rstrip("\n")
# Getting a matching random band
random_band = list_of_bands[random_number]
# Getting the matching year of the song
random_year = list_of_years[random_number]
# Getting the intials of the random song
song_initials = "".join(item[0].upper() for item in random_song.split())


# Functions
def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def writeUsers(usr):
    with open("users.json", "w+") as f:
        json.dump(usr, f)


def save_score(score, user):
    # Making a dict to save the current user and score
    a_dictionary = {user: score}
    # Appending the dict to a txt file
    with open('scores.txt', 'a') as fp:
        print(a_dictionary, file=fp)
        # fp.write(json.dumps(a_dictionary, indent=4))


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
    print("The initals of the song are", song_initials, "the band name is", random_band)
    clue = input("Would you like a clue?, if so type yes, if not type no ")
    if (clue == 'yes'):
        print("the year the song was released was", random_year)
    # Adding an input for the user to guess the song
    guess_the_song = input("Guess the name of the song! ")
    # Setting the number of trys to 3
    number_of_trys_left = 2
    # Defining a wrong answer
    wrong_answer = (guess_the_song != random_song)
    # Starting the quiz answer trys
    while number_of_trys_left > 0 and wrong_answer:
        guess_the_song = input("Thats wrong sorry, please try again! ")
        points -= 1
        # adding a used try
        number_of_trys_left -= 1
        wrong_answer = (guess_the_song != random_song)
    # Getting it wrong
    if wrong_answer:
        print("Sorry that's incorrect, you have had your 3 trys now so the quiz is over for you {0}".format(user))
        #Checking if the player would like to try again
        playagainafterfail = input("Would you like to try the same question again or quit the quiz? Type same for the same question again, or no to quit ")
        if (playagainafterfail == 'same'):
            #Ask same question again, the random_band already used should still be in memory for this session when running this function again
            musicQuiz(user)
        else:
            print("Thanks for playing and goodbye!")
    # Getting it right
    else:
        # Getting the final score
        final_score = points
        # Saving the final score and the user that played the quiz in a text file
        save_score(final_score, user)
        print("Ohh look at you knowing the right band!, well done!")
        print("You scored {0} point/s".format(final_score))
        read_scores('scores.txt')
        print("Thanks for playing and goodbye!")