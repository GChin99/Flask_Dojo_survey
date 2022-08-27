from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Any string we want here"

# Have the root route ("/") show a page with the form
@app.route("/")
def groot():
    return render_template("/index.html")

# Put the form data into session
@app.route("/ninjas", methods=["POST"])
def create_ninjas():
    print(request.form)
    session["ninja_name"] = request.form["name"]
    session["ninja_location"] = request.form["location"]
    session["ninja_language"] = request.form["language"]
    session["ninja_comments"] = request.form["comments"]
    return redirect("/result")

# Have the "/result" route display the information from the form on a new HTML page
@app.route("/result")
def show_user():
    return render_template("result.html")



if __name__ == "__main__":
    app.run(debug=True)