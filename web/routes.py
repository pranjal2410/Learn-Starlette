from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.authentication import requires


async def homepage(request):
    return JSONResponse({'message': 'Hello user!'})

routes = [
    Route('/', homepage)
]
