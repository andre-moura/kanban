from flask import Flask, render_template, request, session


# configuring application
app = Flask(__name__)


@app.route('/')
def home():
    if request.method == "GET":
        return render_template('index.html')


@app.route('/login')
def login():
    if request.method == "GET":
        return render_template('login.html')


@app.route('/register')
def register():
    if request.method == "GET":
        return render_template('register.html')


@app.route('/projects')
def boards():
    if request.method == "GET":
        return render_template('projects.html')


@app.route('/board')
def board():
    if request.method == "GET":
        return render_template('board.html')


@app.route('/members')
def members():
    if request.method == "GET":
        return render_template('members.html')


if __name__ == "__main__":
    app.run(debug=True, host='localhost')