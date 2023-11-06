from flask import Flask, render_template

app = Flask("my_website")


@app.route("/home")
def home():
    return render_template("mypage.html")

app.run(debug=True)