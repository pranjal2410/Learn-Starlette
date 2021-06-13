from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.schemas import SchemaGenerator
from starlette.endpoints import HTTPEndpoint
from sqlalchemy import select
import bcrypt
from web.models import users
from web import database

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
                                      password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'))
        await database.execute(query)

        return JSONResponse(status_code=200)

    async def delete(self, request):
        user_id = request.path_params.get('pk', None)
        await database.execute(users.delete().where(user_id==users.c.id))


async def login(request):
    data = await request.json()
    result = await database.fetch_one(query=users.c.username == data.get('username'))


async def schema(request):
    return schemas.OpenAPIResponse(request)


routes = [
    Route('/users', Users, methods=['GET', 'POST']),
    Route('/users/{pk:int}/', Users),
    Route('/schema', endpoint=schema, include_in_schema=False)
]
