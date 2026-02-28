from fastapi import FastAPI 
from auth_routes import auth_router
from order_routes import order_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
import inspect
import re
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Pizza Delivery API",
        version="1.0",
        description="An API for a Pizza Delivery service",
        routes=app.routes,
    )

    # Add Bearer Auth
    openapi_schema["components"]["securitySchemes"] = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter: Bearer <JWT>"
        }
    }

    # Loop through routes
    for route in app.routes:
        if isinstance(route, APIRoute):
            path = route.path
            methods = route.methods
            endpoint = route.endpoint

            for method in methods:
                method = method.lower()

                if (
                    re.search("jwt_required", inspect.getsource(endpoint)) or
                    re.search("fresh_jwt_required", inspect.getsource(endpoint)) or
                    re.search("jwt_optional", inspect.getsource(endpoint))
                ):
                    openapi_schema["paths"][path][method]["security"] = [
                        {"Bearer Auth": []}
                    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(order_router)






