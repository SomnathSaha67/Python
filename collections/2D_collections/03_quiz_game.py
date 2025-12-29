#Create quiz with questions, options, and scoring
questions=[]
num_questions=int(input("Enter number of questions in the quiz: "))
for i in range(num_questions):
    question_text=input("Enter text for question {}: ".format(i+1))
    num_options=int(input("Enter number of options for question {}: ".format(i+1)))
    options=[]
    for j in range(num_options):
        option_text=input("Enter text for option {}: ".format(j+1))
        options.append(option_text)
    correct_option=int(input("Enter the number of the correct option (1-{}): ".format(num_options)))
    questions.append({
        'question': question_text,
        'options': options,
        'correct': correct_option
    })
score=0
for i, q in enumerate(questions):
    print("\nQuestion {}: {}".format(i+1, q['question']))
    for idx, option in enumerate(q['options']):
        print("{}. {}".format(idx+1, option))
    answer=int(input("Enter your answer (1-{}): ".format(len(q['options']))))
    if answer==q['correct']:
        print("Correct!")
        score+=1
    else:
        print("Wrong! The correct answer was option {}.".format(q['correct']))
print("\nQuiz Over! Your total score is {}/{}.".format(score, num_questions))