# todo_app/app/routes.py
from flask import request, jsonify, abort
from apps import db
from apps.models import Task
from flask import current_app as app
from flask_restful import Resource, Api

api = Api(app)

class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])

    def post(self):
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')

        if not title:
            abort(400, description="Title is required")

        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return jsonify(task.to_dict())

    def put(self, task_id):
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        db.session.commit()
        return jsonify(task.to_dict())

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')
