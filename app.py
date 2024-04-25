"""Main entry point for the application
"""


import sys

from fastapi import (
    FastAPI,
)
from fastapi.exception_handlers import http_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from routers.persons_router import persons_router

app = FastAPI(title="Simple crud api built with FastAPI", version="1.0.0")


# Jinja setup for static files
templates = Jinja2Templates(directory="templates")

# for simplicity, we will allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# include the persons router
app.include_router(persons_router)


@app.get("/raise-500")
def raise_500():
     """
     Dummy route that raises a 500 error to test 500 page.
     """
     return 1 / 0

available_routes = set([route.path.split("/")[1] for route in app.routes])


@app.middleware("http")
async def page_not_found(request: Request, call_next):
        """
        Middleware that checks if the route is available.
        If it's not, it will return a 404 page.
        """
        if request.url.path.split("/")[1] not in available_routes:
            return templates.TemplateResponse("404.html", {"request": request})
        response = await call_next(request)
        return response


async def python_unhandled_error_handler(request: Request, exc: Exception):
    """
    This middleware will log all unhandled exceptions.
    Unhandled exceptions are all exceptions that are not HTTPExceptions
    """

    # here we can do several things, like logging the exception,
    # sending an email to the development team, etc.
    print(f"Unhandled exception: {exc}", file=sys.stderr)
    return templates.TemplateResponse("500.html", {"request": request})

app.add_exception_handler(Exception, python_unhandled_error_handler)     