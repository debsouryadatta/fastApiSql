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
9. Parsing the Database URL from the environment variable using starlette.
10. Creating the engine, poetry add "psycopg[binary]" -> driver to convert the orm queries to sql queries.
11. Editing the connection string & creating the engine using the connection string.
12. pool_size -> no. of connections to the database, by default its 5, it is done so that the engine does not have to connect to the database every time a query is made.
13. pool_recycle -> time in seconds after which the connection will be recycled

14. When we give table=true during model creation, the fields in the model automatically gets registered SQLModel metadata.
15. Session concept - separate session for each funcionality/transaction, session.add(), session.commit(), session.close(). After commiting, the in memory data is freed, session.refresh() -> to refresh the data from the database.
16. Commiting the earlier code, creating the get_session() func, creating the create_todo post endpoint, setting the session before the request using dependency injection of get_session func.
17. Creating a context manager(lifespan) so that we can connect to db & create tables before starting the app
18. Creating the get_all get endpoint, get_single_todo get endpoint, creating the edit_todo put endpoint, creating the delete_todo delete endpoint, using session.exec() to execute the queries.
19. Using HTTPException to throw the errors

20. Copying the whole frontend code from the github repo since i have idea about frontend.

21. Starting the next part -> Adding OAuth2 Authentication for Multi-user
