from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model = joblib.load("regression")
        pred = model.predict([[rates]])
        return(render_template("index.html", result = pred))
    else:
        return(render_template("index.html", result = "WAITING"))

if __name__=="__main__":
    app.run()