from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW
from tortoise import Tortoise
from src.database.register import register_tortoise  # NEW
from src.database.config import TORTOISE_ORM         # NEW
from src.routes import users, skills, projects


Tortoise.init_models(["src.database.models"], "models")  # NEW
"""
import 'from src.routes import users, notes' must be after 'Tortoise.init_models'
why?
https://stackoverflow.com/questions/65531387/tortoise-orm-for-python-no-returns-relations-of-entities-pyndantic-fastapi
"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(skills.router)
app.include_router(projects.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "Hello, World!"
