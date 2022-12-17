from app import app, render_template, request


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