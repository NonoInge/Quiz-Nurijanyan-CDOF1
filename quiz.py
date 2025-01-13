questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["1. Paris", "2. Berlin", "3. Strasbourg", "4. Canada"],
        "correct": 1
    },
    {
        "question": "Which country has the largest population in the world?",
        "choices": ["1. India", "2. China", "3. United States", "4. Russia"],
        "correct": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["1. Mercury", "2. Mars", "3. Jupiter", "4. Venus"],
        "correct": 2
    },
    {
        "question": "What is the largest ocean in the world?",
        "choices": ["1. Atlantic", "2. Pacific", "3. Indian", "4. Arctic"],
        "correct": 2
    },
    {
        "question": "What is the official language of Brazil?",
        "choices": ["1. Spanish", "2. Portuguese", "3. French", "4. English"],
        "correct": 2
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["1. Picasso", "2. Van Gogh", "3. Leonardo da Vinci", "4. Rembrandt"],
        "correct": 3
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["1. Au", "2. Ag", "3. Fe", "4. Pb"],
        "correct": 1
    },
    {
        "question": "How many sides does a hexagon have?",
        "choices": ["1. 5", "2. 6", "3. 7", "4. 8"],
        "correct": 2
    },
    {
        "question": "What is the longest river in the world?",
        "choices": ["1. Nile", "2. Amazon", "3. Yangtze", "4. Mississippi"],
        "correct": 2
    },
    {
        "question": "Who wrote 'Les Misérables'?",
        "choices": ["1. Victor Hugo", "2. Émile Zola", "3. Gustave Flaubert", "4. Honoré de Balzac"],
        "correct": 1
    }
]

score = 0

for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    for choice in q['choices']:
        print(choice)
    
    user_answer = int(input("Enter answer number: "))
    if user_answer == q['correct']:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer was: {q['correct']}")

    print("\n")

print(f"Your score: {score}/10")
