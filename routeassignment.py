from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Bootcamp"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}. Welcome to Flask."

@app.route("/student/<int:id>")
def student(id):
    return f"Student ID is {id}"

@app.route("/product/<int:id>")
def product(id):
    return f"Product ID is {id}"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")

    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]

        return f"username : {username}, password : {password}"


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
            return render_template("registration.html")
    
    if request.method=="POST":
            fullname = request.form["fullname"]
            email = request.form["email"]
            password = request.form["password"]
    
            return f"fullname : {fullname},email:{email}, password : {password}"


@app.route("/profile")
def profile():
    return render_template(
        "profile.html",
        name="Divya",
        email="divya@yopmail.com",
        city="Nsk"
    )


@app.route("/students")
def students():
     students = [
            {
                "name": "Divya",
                "course": "Python",
                "city": "Nashik"
            },
            {
                "name": "Rahul",
                "course": "Flask",
                "city": "Pune"
            },
            {
                "name": "Neha",
                "course": "Django",
                "city": "Mumbai"
            }
        ]
     return render_template("student.html",students = students)    

if __name__ == "__main__":
    app.run(debug=True)

