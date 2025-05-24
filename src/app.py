from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False)

# Route to add a new todo item
@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    if title:
        new_todo = TodoItem(title=title)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

# Route to update a todo item
@app.route('/update/<int:todo_id>')
def update_todo(todo_id):
    todo = TodoItem.query.get_or_404(todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index'))

# Route to delete a todo item
@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = TodoItem.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

# Route to edit a todo item
@app.route('/edit_todo/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo = TodoItem.query.get_or_404(todo_id)
    if request.method == 'POST':
        todo.title = request.form.get('title')
        db.session.commit()
        return redirect(url_for('index'))
    # On GET, render base.html with edit_id
    todos = TodoItem.query.all()
    return render_template('base.html', todos=todos, edit_id=todo.id)

@app.route('/')
def index():
    todos = TodoItem.query.all()
    return render_template('base.html', todos=todos)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)