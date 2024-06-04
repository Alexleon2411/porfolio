from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Skills


SkillInSchema = pydantic_model_creator(
    Skills, name="SkillIn", exclude=["author_id"], exclude_readonly=True)
SkillOutSchema = pydantic_model_creator(
    Skills, name="Skills", exclude =[
      "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)


class UpdateSkill(BaseModel):
    title: Optional[str]
    content: Optional[str]
    image: Optional[str]
