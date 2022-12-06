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


@app.route('/boards')
def boards():
    if request.method == "GET":
        return render_template('boards.html')


if __name__ == "__main__":
    app.run(debug=True)
