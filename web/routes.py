from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.schemas import SchemaGenerator
from starlette.authentication import requires
from web.models import users
from web import database

schemas = SchemaGenerator({
    'openapi': '3.0.0', 'info': {'title': 'Learn Starlette API', 'version': '1.0'}
})


async def homepage(request):
    query = users.select()
    results = await database.fetch_all(query)
    content = [
        {
            'username': result.get('username'),
            'email': result.get('email'),
            'age': result.get('age')
        } for result in results
    ]
    return JSONResponse({'data': content})


async def schema(request):
    return schemas.OpenAPIResponse(request)


routes = [
    Route('/', homepage),
    Route('/schema', endpoint=schema, include_in_schema=False)
]
