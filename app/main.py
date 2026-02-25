from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.admin.setup import setup_admin, UserAdmin
from app.middlewares.logging_middlewares import RequestLoggingMiddleware
from app.routers import posts
from app.api.v1 import auth
from app.core.config import settings
from app.db.database import Base, engine
from fastapi.staticfiles import StaticFiles
from app.core.config import setup_logging
from sqladmin import Admin, ModelView
from starlette.middleware.sessions import SessionMiddleware
from app.admin.auth import AdminAuth

SECRET = "super-secret"

app = FastAPI(
    title=settings.PROJECT_NAME,
    version='1.0.0',
    description="fastapi-boilerplate",
    docs_url="/api/docs",
    redoc_url=None

    # lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(SessionMiddleware, secret_key=SECRET)


# Base.metadata.create_all(bind=engine)

app.include_router(posts.router)
app.include_router(auth.router, prefix='/api/v1/auth', tags=["auth"])
admin = Admin(
    app,
    engine,
    authentication_backend=AdminAuth(secret_key=SECRET),
)
setup_logging()

if settings.DEBUG:
    # On Local/Staging, FastAPI serves static files for convenience
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
else:
    # On Production, we expect Nginx to handle /static/ before it hits Python
    pass

admin.add_view(UserAdmin)

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "CoGym API",
        "version": settings.VERSION,
        "docs": "/docs",
        "health": "/health",
    }