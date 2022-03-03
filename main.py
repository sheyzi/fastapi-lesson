from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

class TodoSchema(BaseModel):
    content: str
    completed: bool

app = FastAPI()

todos = {
    1: {
        'content': 'learning',
        'completed': True
    },

    2: {
        'content': 'Practice',
        'completed': False
    },

    3: {
        'content': 'Startup',
        'completed': True
    }
}


@app.get('/')
def all_todos():
    return todos


@app.get('/{id}/')
def get_todo_with_id(id: int):
    todo = todos.get(id)
    if not todo:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f'todo with id {id} doesnt exist')

    return todo


@app.post('/{id}/')
def create_todo(id: int, body: TodoSchema):
    if todos.get(id):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, f"todo with id {id} already exists!")
    todos[id] = body
    return {'status': "success", "body": body}
