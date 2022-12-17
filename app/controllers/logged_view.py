from app import app, render_template, request


@app.route('/projects')
def projects():
    if request.method == "GET":
        return render_template('projects.html')


@app.route('/boards')
def project():
    if request.method == "GET":
        return render_template('boards.html')


@app.route('/kanban')
def board():
    if request.method == "GET":
        return render_template('kanban.html')


@app.route('/members')
def members():
    if request.method == "GET":
        return render_template('members.html')