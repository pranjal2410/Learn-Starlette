from starlette.routing import Route
from starlette.responses import JSONResponse

async def homepage(request):
    return JSONResponse({'message': 'Hello user!'})

routes = [
    Route('/', )
]