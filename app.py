
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    os = request.form["os"]
    antivirus = request.form["antivirus"]
    firewall = request.form["firewall"]
    password = request.form["password"]

    risks = []
    if antivirus == "no":
        risks.append("Your system is at risk without antivirus protection.")
    if firewall == "no":
        risks.append("A disabled firewall can expose you to threats.")
    if password == "weak":
        risks.append("Weak passwords are easy to guess.")
    elif password == "same":
        risks.append("Reusing passwords makes all your accounts vulnerable.")

    if not risks:
        risks.append("Your system appears to have a low risk setup.")

    return "<h2>Risk Analysis Result</h2><ul>{}</ul><a href='/'>Go Back</a>".format("".join(f"<li>{r}</li>" for r in risks))

if __name__ == "__main__":
    app.run(debug=True)
