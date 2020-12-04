# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model
import random


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index', methods=["POST", "GET"])
def index():
    rand_fact = model.fact_picker()
    model.rand_fact_list.append(rand_fact)
    print(model.rand_fact_list)
    # rand_fact = "Hello there"
    rand_shift = random.randint(0, 24)
    encoded_fact = model.encoder(rand_fact, rand_shift)
    print(encoded_fact)
    # print(rand_fact)
    

    # print(fun_fact_list[rand_num])
    if request.method == "POST":
        user_fact = dict(request.form)
        user_guess = user_fact['guess']
        print(user_guess)
        print(rand_fact)
        if user_guess == model.rand_fact_list[-2]: 
            next_clue = "Clue 6: The person who requested a vegetarian lunch will also present second."
            next_challenge_link = "https://binaryCSscavengerHunt.msshuman.repl.co"
            try_again = "YAY"
            return "<h1>Correct!</h1> <h2>Your next clue is</h2> <p>Clue 6: The person who requested a vegetarian lunch will also present second. Your next challenge can be found at:</p> <a href='https://binarycsscavengerhunt.msshuman.repl.co/'>Click for your next challenge</a>"
            # return render_template("results.html")
        else:
            print(rand_fact)
            try_again = "Please try again. Note: the code and clue has been changed."
            return render_template("index.html", encoded_fact = encoded_fact, try_again = try_again)
    else:
        print(rand_fact)
        return render_template("index.html", encoded_fact = encoded_fact)

