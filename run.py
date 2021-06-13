from web.routes import routes
from web import database, middleware, startup
from starlette.applications import Starlette

app = Starlette(debug=True,
                routes=routes,
                middleware=middleware,
                on_startup=[database.connect, startup],
                on_shutdown=[database.disconnect])
