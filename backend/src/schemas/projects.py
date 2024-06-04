from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Projects


ProjectInSchema = pydantic_model_creator(
    Projects, name="ProjectIn", exclude=["author_id"], exclude_readonly=True)
ProjectOutSchema = pydantic_model_creator(
    Projects, name="Project", exclude =[
      "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)


class UpdateProject(BaseModel):
    title: Optional[str]
    description: Optional[str]
    image: Optional[str]
    url: Optional[str]
