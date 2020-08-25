import functions

def dothequiz():
    #Login user and returning the user name
    user = functions.login()
    #Do quiz and passing in the username so it can be stored
    functions.musicQuiz(user)


dothequiz()
