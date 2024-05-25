# todo_app/run.py
from apps import create_app, db
from apps.models import Task

app = create_app()

app.app_context().push()
db.create_all()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Task': Task}

if __name__ == '__main__':
    app.run(debug=True)
