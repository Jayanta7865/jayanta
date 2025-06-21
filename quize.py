class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")
        answer = input("Enter the number of your answer: ")

        if question.options[int(answer) - 1] == question.answer:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong. The correct answer is {question.answer}.\n")

    print(f"Your final score is {score}/{len(questions)}.")

# Define the questions
questions = [
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Mars"),
    Question("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"], "Harper Lee"),
    Question("What is the smallest prime number?", ["0", "1", "2", "3"], "2"),
    Question("Which element has the chemical symbol 'O'?", ["Gold", "Oxygen", "Hydrogen", "Carbon"], "Oxygen")
]

# Run the quiz
run_quiz(questions)


