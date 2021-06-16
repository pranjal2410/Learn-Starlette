# Starlette learning repo
## About
Starlette is an ASGI framework used to build asyncio services and for high performance.
In this project I have used starlette to develop backend for a website which lets users
register themselves and write blogs and post images related to their blog.<br/>
For authentication, I have used <code>starlette-jwt</code> package.<br/>
I have used PostgreSQL and <code>sqlalchemy</code> package of python for database. Also for database migrations, the starlette
documentation recommends to use <code>alembic</code>. 
## Requirements:
<li>Python 3.7+</li>
<li>Yarn 1.22</li>
<li>SQL database</li>

## Steps to run this project:
<li>Clone this repository using the command:<br/>
<code>git clone https://github.com/pranjal2410/Learn-Starlette.git</code>
</li>
<li>Create a pip virtual environment and activate it</li>
<li>Install the dependencies using <code>pip install -r requirements.txt</code></li>
<li>Create a .env file and add the following:<br/>
DATABASE_URL={url to the database}<br/>
SECRET_KEY={any secret key, I recommend to use secrets module of python}<br/>
</li>
<li>Create a media folder in the root directory</li>
<li>Run the backend server using <code>uvicorn run:app --reload</code></li>
<li>Navigate to the frontend directory and run <code>yarn install</code></li>
<li>Create a .env file and add:<br/>REACT_APP_API_URL={your api url, most likely http://localhost:8000}</li>
<li>Run the client server using <code>yarn start</code></li>

## References
- [Starlette Documentation](https://www.starlette.io/)
- [UI Templates](https://material-ui.com/getting-started/templates/)
