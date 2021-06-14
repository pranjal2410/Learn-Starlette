from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.schemas import SchemaGenerator
from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
import jwt
import bcrypt
from web.models import users, blogs
from web import database, config

schemas = SchemaGenerator({
    'openapi': '3.0.0', 'info': {'title': 'Learn Starlette API', 'version': '1.0'}
})


class Users(HTTPEndpoint):

    async def get(self, request):
        user_id = request.path_params.get('pk', None)
        if user_id:
            query = users.select().where(users.c.id == user_id)
            result = await database.fetch_one(query=query)
            data = {
                'username': result.__getitem__('username'),
                'email': result.__getitem__('email'),
                'age': result.__getitem__('age')
            }

            return JSONResponse(data, status_code=200)
        query = users.select()
        results = await database.fetch_all(query)
        content = [
            {
                'username': result.get('username'),
                'email': result.get('email'),
                'age': result.get('age'),
                'id': result.get('id')
            } for result in results
        ]
        return JSONResponse({'data': content})

    async def post(self, request):
        data = await request.json()
        age = data.pop('age')
        password = data.pop('password')
        query = users.insert().values(**data,
                                      age=int(age),
                                      password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode(
                                          'utf-8'))
        result = await database.execute(query)
        payload = {
            'email': data.get('email'),
            'username': data.get('username'),
            'id': result.__getitem__('id')
        }
        token = jwt.encode(payload, config('SECRET_KEY'), algorithm='HS256')

        return JSONResponse({'token': token}, status_code=200)

    async def delete(self, request):
        user_id = request.path_params.get('pk', None)
        await database.execute(users.delete().where(user_id == users.c.id))


class Blog(HTTPEndpoint):

    @requires('authenticated')
    async def get(self, request):
        query = blogs.select()
        results = await database.execute(query)
        content = [
            {
                'text': result.get('text'),
                'id': result.get('id'),
                'created': result.get('created')
            } for result in results
        ]

        return JSONResponse({'data': content})

    @requires('authenticated')
    async def post(self, request):
        user = request.user
        print(user)
        data = await request.json()


async def login(request):
    data = await request.json()
    result = await database.fetch_one(query=users.select().where(users.c.username == data.get('username')))
    if bcrypt.checkpw(data.get('password').encode('utf-8'), result.__getitem__('password').encode('utf-8')):
        payload = {
            'email': result.__getitem__('email'),
            'username': result.__getitem__('username'),
            'id': result.__getitem__('id'),
        }
        token = jwt.encode(payload, config('SECRET_KEY'), algorithm='HS256')

        return JSONResponse({'token': token}, status_code=200)
    else:
        return JSONResponse(status_code=401)


async def schema(request):
    return schemas.OpenAPIResponse(request)


routes = [
    Route('/users', Users, methods=['GET', 'POST']),
    Route('/users/{pk:int}/', Users),
    Route('/login', login, methods=['POST']),
    Route('/schema', endpoint=schema, include_in_schema=False)
]
