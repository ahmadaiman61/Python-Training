from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    q_text = i["text"]
    q_answer = i["answer"]
    n_question = Question(q_text,q_answer)
    question_bank.append(n_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz\n")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")