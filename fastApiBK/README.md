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
22. On the backend, Segregating the parts, models.py -> For models, db.py -> For creating engine/connection, router/user.py ->   , auth.py -> 
23. Inside router, creating an user_router of prefix "/user", adding the user_router in the main.py
24. Creating a new class for Register_User for validation of the user registration
25. Creating a new model class User for the user table, making user_id the foreign_key for the todo table.
26. To use formdata we need to install python-multipart, poetry add python-multipart
27. Creating the endpoint for user_registration, poetry add "passlib[bcrypt]" -> for hashing the password, creating a hash_password func inside auth.py
28. Also creating get_user_from_db func in the auth.py to get the user from the database
29. user_registration endpoint created, validating and then adding the user to the database.
30. Creating the login endpoint, using OAuth2PasswordRequestForm for validation, creating an authenticate_user func in auth.py to authenticate the user
31. Creating a create_access_token func in auth.py, poetry add "python-jose[cryptography]" -> for creating the jwt token, wrote the code for creating the jwt token.

32. Creating a new Token class for validating the token which will be sent to the client after login.
33. Creating a current_user func in the auth.py to get the current user from the token.
34. Protecting the create_todo endpoint with the current_user func
35. Creating a new user_router endpoint "/me", to get the profile, also protecting it with the current_user func and get the user from the token.
36. Creating an additional Todo_Create model just for validating the todo creation.
37. The db was not updating even after adding a new field, so i had to drop the table and recreate it, then the create_todo endpoint woked fine.
38. Updating the code of get_all endpoint and the get_single_todo endpoint, also protecting them with the current_user func.
39. Updating the code of edit_todo endpoint and the delete_todo endpoint, also protecting them with the current_user func.
40. Creating refresh_token, validate_refresh_token funcs in the auth.py, same as the create_access_token func & current_user funcs, one change - this time in the jwt_token, we are adding the email and not the username
41. Creating the refresh_token endpoint, validating the old_refresh_token and then creating a new access_token and refresh_token, sending them to the client.
42. Finishing the backend part, only part left is to implement the final signin/signup part in the frontend.




- Working of Refresh Token -> After User Registration, whenever the user logs in, he/she will get an access_token and a refresh_token. After the access_token expires, the frontend will get expiration errors, then the frontend will send the refresh_token to the refresh_token endpoint, which will generate a new access_token and a new refresh_token, the frontend will then use the new access_token and the new refresh_token to make the requests. And the loop goes on!

- For Installing all the dependencies in the poetry.toml file, run - poetry install


*** The route handlers are marked as async functions, the rest are normal functions. ***