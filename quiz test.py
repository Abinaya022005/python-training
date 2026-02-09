# ONLINE QUIZ PROJECT (PYTHON)
#List
#dictionary
questions = [
    {
        "question": "Python is which type of language?",
        "options": ["a) Low level", "b) High level", "c) Machine", "d) Assembly"],
        "answer": "b"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["a) func", "b) define", "c) def", "d) function"],
        "answer": "c"
    },
    {
        "question": "Which data type is used to store multiple values?",
        "options": ["a) int", "b) float", "c) list", "d) bool"],
        "answer": "c"
    }
]
#function 
def start_quiz():
    score = 0
    name = input("Enter your name: ")
    #for loop 
    for i in range(len(questions)):
        print("\n", i + 1, questions[i]["question"])
        for opt in questions[i]["options"]:
            print(opt)

        # TRY-EXCEPT for user answer
        try:
            ans = input("Enter your answer (a/b/c/d): ").lower()

            if ans not in ['a', 'b', 'c', 'd']:
                raise ValueError   # manually create error

            elif ans == questions[i]["answer"]:
                print("Correct ")
                score += 1
            else:
                print("Wrong ")

        except:
            print("Invalid input! Please enter only a/b/c/d")

    print("\nFinal Score:", score, "/", len(questions))
    save_result(name, score)

def save_result(name, score):
    # TRY-EXCEPT for file handling
    try:
        file = open("quiz_results.txt", "a")
        file.write(name + " - Score: " + str(score) + "\n")
        file.close()
        print("Result saved in file")
    except:
        print("Error while saving file")

start_quiz()
