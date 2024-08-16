import logging
from flask import Flask, render_template, request

app = Flask(__name__)

results = [0,0]
question = "test question"
option_1 = "question 1"
option_2 = "question 2"
val_1 = 0
val_2 = 0
quiz_index = 0

def set_questions(q_index):
    
      if q_index == 0:
          question = "Which do you prefer?"
          option1 = "Tea"
          val_1 = 1
        
          option2 = "Coffee"
          val_2 = 0

          return question, option1, val_1, option2, val_2
        
      elif q_index == 1:
          question = "Which class would you play?"
          option1 = "Mage"
          val_1 = 0
        
          option2 = "Bard"
          val_2 = 1

          return question, option1, val_1, option2, val_2
        
      elif q_index == 2:
          question = "Pick a color"
          option1 = "Teal"
          val_1 = 0
        
          option2 = "Brown"
          val_2 = 1

          return question, option1, val_1, option2, val_2
 
      elif q_index == 3:
          question = "At the end of the path you see "
          option1 = "The ocean"
          val_1 = 0
        
          option2 = "A forest"
          val_2 = 1

          return question, option1, val_1, option2, val_2
 
      elif q_index == 4:
          question = "A rat visits your bakery. They buy "
          option1 = "Tiramisu"
          val_1 = 1
        
          option2 = "Chocolate Cookie"
          val_2 = 0

          return question, option1, val_1, option2, val_2
 
      elif q_index == 5:
          question = "The sky is lit by "
          option1 = "The sun"
          val_1 = 1
        
          option2 = "The moon"
          val_2 = 0

          return question, option1, val_1, option2, val_2
 
      else:
          question = "Empty Question"
          option1 = "Empty Answer"
          val_1 = 0
        
          option2 = "Empty Answer 2"

          val_2 = 1

          return question, option1, val_1, option2, val_2
        

qpack = set_questions(quiz_index)

question = qpack[0]
option_1 = qpack[1]
val_1 = qpack[2]
option_2 = qpack[3]
val_2 = qpack[4]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz/")
def quiz_page(answered = False, result_index = None, quiz_index = 0):
    qpack = set_questions(quiz_index)
    
    question = qpack[0]
    option_1 = qpack[1]
    val_1 = qpack[2]
    option_2 = qpack[3]
    val_2 = qpack[4]

    
    if(answered):
        results[result_index] +=1
    return render_template("quiz.html",
                           score = results,
                           title = question,
                           q1 = option_1,
                           q2 = option_2,
                           value1 = val_1,
                           value2 = val_2,
                           q_index = quiz_index)

@app.route("/quiz_result/")
def quiz_result(final_result):
    return render_template("result.html", f_result = final_result)

@app.get("/answer_get/")
def answer_get():
    quiz_index = int(request.args['quiz_button'])
    quiz_index += 1
    num = int(request.args['quiz_form'])
    if(quiz_index < 6):
        return quiz_page(True,int(num),quiz_index)
    else:
        final_result = "empty"
        results[num] += 1
        
        if results[0] > results[1]:
            final_result = "Chihuahua"
        elif results[0] < results[1]:
            final_result = "Poodle"
        elif results[0] == results[1]:
            final_result = "Tie! You are part Poodle part Chihuahua"
        else:
            final_result - "Error"
        
        return quiz_result(final_result)

if __name__ == '__main__':
    app.run()
 
