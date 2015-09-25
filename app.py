from flask import Flask, render_template

app = Flask(__name__), render_template

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def profile():
    dict = {'last' : "Flintstone",
            'first' : "Fred"}
    dict['title'] = "Grand Poobah"

    list = [10,20,"thirty",40,"fifty"]

    return render_template("person.html", d = dict, l = list)

@app.route("/")


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)