# a fastapi system for todo managament

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class ToDo(BaseModel):
    id: int
    name: str
    description: str
    date: date  # ISO format date string

# type hint for a list of todos
todos:list[ToDo] = []

@app.post("/todos/")
def create_todo(todo: ToDo):
    todos.append(todo)
    return {"message": "ToDo created successfully"}

@app.get("/todos/")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "ToDo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    todos[:] = [todo for todo in todos if todo.id != todo_id]
    return {"message": "ToDo deleted successfully"}
