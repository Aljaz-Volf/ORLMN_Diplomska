from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    stats = {
        "leagues": 2,
        "teams": 28,
        "matches": 150
    }
    return render_template("home.html", stats=stats)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
