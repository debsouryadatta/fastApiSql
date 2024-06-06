from fastapi import FastAPI
from sqlmodel import SQLModel, Field

app : FastAPI = FastAPI()

# Create Model
class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str = Field(index=True, min_length=3, max_length=54)
    is_completed: bool = Field(default=False)

@app.get("/") # Decorator - Runs the below func without calling it
async def root():
    return {"message": "Welcome to Dad Todo!"}

@app.get("/todo/")
async def get_todo():
    return {"dummy": "Get the todo list"}