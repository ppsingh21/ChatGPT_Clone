from flask import Flask, render_template,request #josinfy, 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods=["GET","POST"])
def qa():
    if request.method=="POST":
        data = {"result": "Thank you! I'm glad I could help. If you have any more questions, feel free to ask!"}
        return josinfy(data)
    return render_template("index.html")

app.run(debug=True)