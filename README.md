### Steps of Dev:
1. pip install poetry(on the python env) never do it in the system, faced a big fat kde error.
2. poetry new fastApiBK, cd fastApiBK
2. poetry add fastapi, poetry add uvicorn
3. Initializing the fastApi app.
4. poetry run uvicorn fastapibk.main:app --reload -> to run the server on port 8000 by default.
5. poetry add sqlmodel -> to add the ORM for the database.
6. Creating model -> Previously we had to create 2 models, data model(like pydantic) -> for validation, and table model(like sqlAlchemy) -> for adding tables to the database.
7. Now with sqlmodel, we only need to create one model, which will be used for both validation and table creation.
8. Creating the common Todo model both for validation and table creation.
9. 