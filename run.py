#  Game functions----

def new_game():

    Suppos = []
    correct_Suppos = 0
    question_num = 1

    for key in questions:
        print(" ")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        Suppos.append(guess)

        correct_Suppos += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_Suppos, Suppos)


#  Answer functions----    
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


#  display functions----    
def display_score(correct_Suppos, Suppos):
    print(" ")
    print("RESULTS")
    print(" ")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Suppos: ", end="")
    for i in Suppos:
        print(i, end=" ")
    print()

    score = int((correct_Suppos/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#  play again functions----    
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# Question and Answers ---
questions = {
 "Which city is the capital of Canada ?: ": "A",
 "How many continents in the world ?: ": "B",
 "Where is the highest mountain in the world located ?: ": "C",
 "Is the Earth round?: ": "A"
}

Answers = [["A. Ottawa", "B. Toronto", "C. Vancouver", "D. Calgary"],
          ["A. 8", "B. 7", "C. 20", "D. 16"],
          ["A. China", "B. Srilanka", "C. Between Nepal and Tibet", "D. Europe"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]  