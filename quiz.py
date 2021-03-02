class Question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer=answer

question_list=["What color is an Apple?: \n a. Red\n b. Magenta\n c. Orange\n",
                 "What one of these a bird?: \n a. Dog\n b. Penguin\n c. Whale\n",
                 "Who is the president of USA?: \n a. Trump\n b. Magenta\n c. Orange\n"]


quiz_questions = [Question(question_list[0],"a"),
Question(question_list[1],"b"),
Question(question_list[2],"a")]

score=0
for each_question in quiz_questions:
    answer = input(each_question.prompt)
    if answer == each_question.answer:
        score += 1

print(f"You got {score}/{len(quiz_questions)} answers correct !!!")
