## First set of questions
import random as rd

questions = [
    {
        "question": "What is the capital of France?",
        "type": "Geography",
        "choices": ["1. Paris", "2. Berlin", "3. Strasbourg", "4. Canada"],
        "correct": 1
    },
    {
        "question": "Which country has the largest population in the world?",
        "type": "Geography",
        "choices": ["1. India", "2. China", "3. United States", "4. Russia"],
        "correct": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "type": "Astronomy",
        "choices": ["1. Mercury", "2. Mars", "3. Jupiter", "4. Venus"],
        "correct": 2
    },
    {
        "question": "What is the largest ocean in the world?",
        "type": "Geography",
        "choices": ["1. Atlantic", "2. Pacific", "3. Indian", "4. Arctic"],
        "correct": 2
    },
    {
        "question": "What is the official language of Brazil?",
        "type": "Geography",
        "choices": ["1. Spanish", "2. Portuguese", "3. French", "4. English"],
        "correct": 2
    },
    {
        "question": "Who painted the Mona Lisa?",
        "type": "Arts",
        "choices": ["1. Picasso", "2. Van Gogh", "3. Leonardo da Vinci", "4. Rembrandt"],
        "correct": 3
    },
    {
        "question": "What is the chemical symbol for gold?",
        "type": "Chemistry",
        "choices": ["1. Au", "2. Ag", "3. Fe", "4. Pb"],
        "correct": 1
    },
    {
        "question": "How many sides does a hexagon have?",
        "type": "Geometry",
        "choices": ["1. 5", "2. 6", "3. 7", "4. 8"],
        "correct": 2
    },
    {
        "question": "What is the longest river in the world?",
        "type": "Geography",
        "choices": ["1. Nile", "2. Amazon", "3. Yangtze", "4. Mississippi"],
        "correct": 2
    },
    {
        "question": "Who wrote 'Les Misérables'?",
        "type": "Litterature",
        "choices": ["1. Victor Hugo", "2. Émile Zola", "3. Gustave Flaubert", "4. Honoré de Balzac"],
        "correct": 1
    }
]

def add_question(questions):
    """Add questions to the past mcq. Inplace function."""
    question = input("What is the new question ?")
    type = input("What is the theme of this question ?")
    choices = []
    for i in range(4):
        choice = input("Choice number "+str(i+1))
        choices.append(str(i+1)+". "+choice)
    correct = '0'
    while not correct.isdigit() or int(correct) not in [1, 2, 3, 4]:
        correct = input("Give the number for the correct answer.")#To ensure the correct is one of the possibility
    correct = int(correct)
    questions.append({"question": question,
                        "type": type,
                        "choices": choices,
                        "correct": correct})
    return questions

# Example of use : questions = add_question(questions)

def MCQ(n_questions:int):
    """MCQ containing n_questions different questions from the previously
    given list.
    It will never do more than the number of questions in the full MCQ."""
    score = 0
    selected_questions = rd.sample(questions, min(len(questions), n_questions))
    for i, q in enumerate(selected_questions, start=1):
        print(f"Question {i}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        
        user_answer = 0
        while not user_answer.isdigit() or int(user_answer) not in [1, 2, 3, 4]:#ensures answer is valid
            user_answer = input("Enter answer number: ")
        user_answer = int(user_answer)
        if user_answer == q['correct']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: { q['choices'][q['correct']-1] }")
        print("\n")
    
    print(f"Your score: {score}/{n_questions}")

# Example of use : MCQ(5)

