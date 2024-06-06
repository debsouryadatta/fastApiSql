from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from fastapibk import settings
from typing import Annotated
from contextlib import asynccontextmanager


# Create Model
class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str = Field(index=True, min_length=3, max_length=54)
    is_completed: bool = Field(default=False)
    

#  Engine is one for whole application
connection_string : str = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode":"require"}, pool_recycle=3000, pool_size=10, echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)
    


def get_session():
    with Session(engine) as session:
        yield session

# Creating a context manager so that we can connect to db & create tables before starting the app
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating Tables")
    create_table()
    print("Tables Created")
    yield




app : FastAPI = FastAPI(lifespan=lifespan, title="Dad Todo", version="0.1.0")

@app.get("/") # Decorator - Runs the below func without calling it
async def root():
    return {"message": "Welcome to Dad Todo!"}


@app.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo, session: Annotated[Session, Depends(get_session)]):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

    
@app.get("/todos/", response_model=list[Todo])
async def get_all(session: Annotated[Session, Depends(get_session)]):
    todos = session.exec(select(Todo)).all()
    if todos:
        return todos
    else:
        raise HTTPException(status_code=404, detail="No task found!")
    
    
@app.get("/todos/{id}")
async def get_single_todo(id: int, session: Annotated[Session, Depends(get_session)]):
    todo = session.exec(select(Todo).where(Todo.id == id)).first()
    if todo:
        return todo
    else:
        raise HTTPException(status_code=404, detail="No task found!")
        

    
@app.put("/todos/{id}")
async def edit_todo(id: int, todo: Todo, session: Annotated[Session, Depends(get_session)]):
    existing_todo = session.exec(select(Todo).where(Todo.id == id)).first()
    if existing_todo:
        existing_todo.content = todo.content
        existing_todo.is_completed = todo.is_completed
        session.add(existing_todo)
        session.commit()
        session.refresh(existing_todo)
        return existing_todo
    else:
        raise HTTPException(status_code=404, detail="No task found!")
    
    
@app.delete("/todos/{id}")
async def delete_todo(id: int, session: Annotated[Session, Depends(get_session)]):
    todo = session.exec(select(Todo).where(Todo.id == id)).first()
    if todo:
        session.delete(todo)
        session.commit()
        return {"message": "Task deleted successfully!"}
    else:
        raise HTTPException(status_code=404, detail="No task found!")