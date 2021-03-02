"""A game that tries to guess your major"""

from random import randint

__author__ = "930410205"


questions_list = ["Would You like to get started? \n(1) Yes \n(2) No \n(3) You just wanna tell me your major \n(4) Play the Random Major Guessing Game",
    "Do you use words or numbers in your classes more often? \n(1) Words \n(2) Numbers \n(3) A bit of both \n(4) Quit and view points",
    "Do you like working independently or with other people? \n(1) Other People \n(2) By yourself \n(3) It depends \n(4) Quit and view points",
    "Do you get a lot of homework? \n(1) No \n(2) Yes \n(3) Kind of \n(4) Quit and view points",
    "Do you prefer going to parties or having some alone time? \n(1) Partying \n(2) Me time \n(3) Both \n(4) Quit and view points",
    "Are you a hands-on or a visual/auditory learner? \n(1) Viz-Aud \n(2) Hands-On \n(3) Other \n(4) Quit and view points"]

list_of_majors = ["Business", "Nursing", "Psychology", "Biology", "BME", "Education", "Anthropology", "Sociology", "Computer Science",
    "English", "Economics", "Political Science", "History", "EXSS", "Math", "Chemistry", "Physics", "Philosophy", "Art"]

def main() -> None:
    """function that will run the game"""
    player = str(greet())
    print("Questions will be multiple choice and you'll input an answer choice.")
    print("Some questions may ask to input a number, which you will do so.")
    getting_started = starting_question()
    if getting_started == 1:
        game_questions(game_start)
    else:
        if getting_started == 4:
            random_major()
        else:
            print("Do You want to play again? \n(1) Yes \n(2) No")
            rematch = int(input())
            if rematch == 1:
                main()
            else:
                print("Bye!")
            

    
def greet() -> None:
    """greets and introduces the player and breaksdown the game to them"""
    print("Welcome! I will try to guess your major by asking you some questions about what your days may look like")
    print("Before we get started, what is your name?")
    player = str(input())
    print(f"Well nice to meet you, {player}, I hope you enjoy! {COWBOY}")
    return player


def starting_question() -> None:
    """prompts the player with the first question to get started with the game"""
    i = 0
    print(questions_list[i])
    answer1 = input()
    if int(answer1) == 1:
        print("Great! Have fun!")
        return 1
    else:
        if int(answer1) == 4:
            print("Great! Enjoy!")
            return 4
        else:
            print("Aw... Oh Well...")
    if int(answer1) == 3:
        print("What's your major?")
        major = str(input())    
        print(f"Ooh, Interesting. You're a {major} major so you must be smart!")
        print(f"points awarded: {points} ")
        return 3



def game_questions(puntos: None) -> None:
    """Will prompt the user with the first set of questions"""
    i = 1
    while i < len(questions_list):
        print(questions_list[i])
        answers_to_questions = int(input())
        if answers_to_questions == 1:
            puntos += 10
        else:
            if answers_to_questions == 2:
                puntos += 30
            else:
                if answers_to_questions == 3:
                    puntos += 20      
                else:
                    if answers_to_questions == 4:
                        print("Aw, oh well")
                        print(f"Points awarded: {puntos}")
                        print("Do You want to play again? \n(1) Yes \n(2) No")
                        rematch = int(input())
                        if rematch == 1:
                            main()
                            return puntos
                        else:
                            print("Bye!")
                            return puntos
                            
                        break
        i += 1
    if puntos < 100:
        print("Are you a humanities major?!")
        print("Was I right? \n(1) Yes :) \n(2) No :(")
        ans_correct = int(input())
        if ans_correct == 1:
            print("YAY!! I WIN!!")
            print("Do You want to play again? \n(1) Yes \n(2) No")
            rematch = input()
            if int(rematch) == 1:
                main()            
        else: 
            print("Aw man... I thought I had it... well what is your major?")
            major = str(input())    
            print(f"Ooh, Interesting. You're a {major} major so you must be super smart!")
            print("Do You want to play again? \n(1) Yes \n(2) No")
            rematch = input()
            if int(rematch) == 1:
                main()
            else:
                print("Bye!")
                print(f"Points awarded: {puntos}")            
    else:
        print("Are you a STEM major?!")
        print("Was I right? \n(1) Yes :) \n(2) No :(")
        ans_correct = int(input())
        if ans_correct == 1:
            print("YAY!! I WIN!!")
            print("Do You want to play again? \n(1) Yes \n(2) No")
            rematch = input()
            if int(rematch) == 1:
                main()
            else:
                print("Bye!")
                print(f"Points awarded: {puntos}")
        else: 
            print("Aw man... I thought I had it... well what is your major?")
            major = str(input())    
            print(f"Ooh, Interesting. You're a {major} major so you must be super smart!")
            print("Do You want to play again? \n(1) Yes \n(2) No")
            rematch = input()
            if int(rematch) == 1:
                main()
            else:
                print("Bye!")
                print(f"Points awarded: {puntos}")

    return puntos

def random_major() -> None:
    """Introduces the Random Major Guessing Game"""
    print("The objective of this game is to randomly guess your major")
    print("If you're getting bored, or don't think your major is added, there will be an option to quit")
    def is_this_your_major() -> None:
        """Majors are randomly called and you're asked if you are that major"""
        i = randint(0, len(list_of_majors)-1)
        print(list_of_majors[i])
        print("Is this your major? \n(1) Yes \n(2) No \n(3) Quit")
        rand_ans = int(input())
        if rand_ans == 1:
            print(f"Nice! I win! {COWBOY}")
            print("Do You want to play again? \n(1) Yes \n(2) No")
            rematch = input()
            if int(rematch) == 1:
                main()
            else:
                print("Bye!")
            return None
        if rand_ans == 2:
            print(f"Let's try again...")
            is_this_your_major()  
            return None
        else:
            print("Aw... oh well...")
            if rand_ans == 3:
                print("Do You want to play again? \n(1) Yes \n(2) No")
                rematch = input()
                if int(rematch) == 1:
                    main()
                else:
                    print("Bye!")
    is_this_your_major()                
    return None


COWBOY: str = "\U0001F920"
game_start = 0
points = 0


if __name__ == "__main__":
    main()