from web.routes import routes
from web import database
from starlette.applications import Starlette
from starlette_jwt import JWTAuthenticationBackend
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware


async def startup():
    print('Application has started')


middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*']),
    Middleware(AuthenticationMiddleware,
               backend=JWTAuthenticationBackend(
                       secret_key='a9cb4ea36a5175e2cb840db5fa2210254d25c25d6344ebebd493af00bf922416',
                       prefix='Bearer'
    ))
]


app = Starlette(debug=True,
                routes=routes,
                middleware=middleware,
                on_startup=[database.connect, startup],
                on_shutdown=[database.disconnect])
