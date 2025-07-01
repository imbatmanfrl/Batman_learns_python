def new_game():
    guesses= []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num +=1

    display_score(correct_guesses,guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses,guesses):
    print("-------------")
    print("RESULTS")
    print("--------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses/len(questions)*100)
    print("Your score is: "+ str(score)+"%")
def pay_again():
    pass

questions = {
    "Who is my alter ego? ": "B",
    "What is my favorite anime? ": "A",
    "What is my dream job? ": "C",
    "What is my dream car? " : "D"
}

options = [["A. Obito","B. Batman🦇","C. Kenpachi zaraki","D. Madara"],
           ["A. Bleach","B.Naruto","C.Attack on Titans","D.Jujitsu Kaisen"],
           ["A. Tech Bro" , "B. Engineer", "C. Finance", "D. Law"],
           ["A. Bugatti Veyron", "B. Mclaren P1","C. Porshe 918 Spyder","D. Ferrai LaFerrari Aperta.❤️"]]

new_game()