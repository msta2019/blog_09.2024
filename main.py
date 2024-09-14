from flask import Flask, redirect, url_for, request, render_template
from random import randint
import db

app = Flask(__name__)
quiz = 0
last_question = 0
score = 0

def index():
    global quiz, last_question, score
    last_question = 0
    score = 0
    quiz = randint(1,3)
    print(quiz)

    if request.method == "GET":
    



        return render_template("index.html", quizes=db.get_quizes())

        
    elif request.method == "POST":
        quiz = request.form.get("quiz")
        return redirect(url_for("test"))


def test():
    global last_question, score
    try:
        result = db.get_questions(quiz)[last_question]
    except IndexError:
        return redirect(url_for("result"))
    
    if request.method == "GET":

        return render_template("test.html", question=result)
    

    if request.method == "POST":
        last_question+=1
        user_answer = request.form.get("user_answer")
        text = ""
        if user_answer == result[1]:
            text =  "Правильно"
            score += 1
        else:
            text =  "Неправильно"
            score -= 1
        return render_template("test.html", result_text=text)
        

def result():
    return render_template("result.html", score_text = score)


app.add_url_rule("/", "index", index, methods=["GET", "POST"])
app.add_url_rule("/test", "test", test, methods=["GET", "POST"])
app.add_url_rule("/result", "result", result)

if __name__ == "__main__":
    app.run(debug=True)