# Task 1: Develop a list of questions and answers.
# Task 2: Write a function that quizzes the user and takes their answers.
# Task 3: Score the quiz and give the user feedback on their performance.
questions = ['What is the capital of Okinawa?',
             'What is the numerical value of the meaning of life?',
             'What is the last name of the character in Shogun who is based on Tokugawa Ieyasu?',
             'Boxers, briefs, or boxer briefs?']
answers = ['Naha', '42', 'Toranaga', 'briefs']
score = 0

answer1 = input("\nWhat is the capital of Okinawa?: ")
if answer1.lower() == "naha":
    print("Correct!")
    score += 1
else:
    print(f"The answer is 'Naha', not {answer1}!")

answer2 = int(input("\nWhat is the numerical value of the meaning of life?: "))
if answer2 == 42:
    print("Correct!")
    score += 1
else:
    print(f"The answer is '42', not {answer2}!")

answer3 = input("\nWhat is the last name of the character in Shogun who is based on Tokugawa Ieyasu?: ")
if answer3.lower() == "toranaga":
    print("Correct!")
    score += 1
else:
    print(f"The answer is 'Toranaga', not {answer3}!")

answer4 = input("\nBoxers, briefs, or boxer briefs?: ")
if answer4.lower() == "briefs":
    print("Correct!")
    score += 1
else:
    print(f"The answer is 'briefs', not {answer4}!")

print(f"\nYour final score: {score} out of {len(questions)}\n")