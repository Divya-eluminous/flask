from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return " Welcome page"

@app.route("/services")
def services():
    return "Our Services"

@app.route("/profile")
def profile():
    return " My Profile"

@app.route("/profile/<name>")
def getdetails(name):
    return "f{name}"

if __name__ =="__main__":
    app.run(debug=True)