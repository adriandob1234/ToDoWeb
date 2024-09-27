from flask import request, jsonify
from app import Todo
from main import session
app = Flask(__name__)
@app.route('/todo/<int:id>', methods=["GET"])
def get_todos(id):
    todos = session.query(Todo).all()
    for todo in todos:
        if todo.id == id:
            return jsonify({"todo": {"id": todo.id, "task": todo.task, "due": todo.due}}), 200
    return jsonify({"message": "Todo was not found"}), 404
@app.route('/todo', methods=["POST"])
def create_todo():
    data = request.json
    new_todo = Todo(id=data.get('id'), task=data.get('task'), due=data.get('due'))
    session.add(new_todo)
    session.commit()
    return jsonify({"todo": {"id": new_todo.id, "task": new_todo.task, "due": new_todo.due}}), 201
