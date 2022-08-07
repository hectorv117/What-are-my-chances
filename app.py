from crypt import methods
from flask import Flask, render_template, request, url_for
import model 


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def Home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        school = int(request.form["school"])
        res = int(request.form["residency"])
        cap = int(request.form["cap"])
        gpa = float(request.form["gpa"])
        hours = int(request.form["hours"])
        score = str(model.getScore(school, gpa, hours, res, cap))


        return render_template('result.html', score = score)


 


if __name__ == "__main__":
    app.run(debug=True)