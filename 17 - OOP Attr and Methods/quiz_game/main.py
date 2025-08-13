from src.data_manager import get_questions_from_opentdb_url
from src.question_model import Question
from src.quiz_brain import QuizBrain
# Create a question bank list with Question objects from the qeustion data.
url = 'https://opentdb.com/api.php?amount=15&difficulty=easy&type=boolean' ## Generated from opentdb.com - True or False questions only
question_bank = [Question(q['text'], q['answer']) for q in get_questions_from_opentdb_url(url)]

# Initializse quiz object
quiz = QuizBrain(question_bank)

# Quiz loop
while quiz.still_has_questions():
    quiz.next_question()