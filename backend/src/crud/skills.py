from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Skills
from src.schemas.skills import SkillOutSchema
from src.schemas.token import Status  # NEW


async def get_skills():
    return await SkillOutSchema.from_queryset(Skills.all())


async def get_skill(skill_id) -> SkillOutSchema:
    return await SkillOutSchema.from_queryset_single(Skills.get(id=skill_id))


async def create_skill(skill, current_user) -> SkillOutSchema:
    skill_dict = skill.dict(exclude_unset=True)
    skill_dict["author_id"] = current_user.id
    skill_obj = await Skills.create(**skill_dict)
    return await SkillOutSchema.from_tortoise_orm(skill_obj)


async def update_skill(skill_id, skill, current_user) -> SkillOutSchema:
    try:
        db_skill = await SkillOutSchema.from_queryset_single(Skills.get(id=skill_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Skill {skill_id} not found")

    if db_skill.author.id == current_user.id:
        await Skills.filter(id=skill_id).update(**skill.dict(exclude_unset=True))
        return await SkillOutSchema.from_queryset_single(Skills.get(id=skill_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_skill(skill_id, current_user) -> Status:
    try:
        db_skill = await Skills.get(id=skill_id).prefetch_related("author")
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Skill {skill_id} not found")

    if db_skill.author.id == current_user.id:
        deleted_count = await Skills.filter(id=skill_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Skill {skill_id} not found")
        return Status(message=f"Deleted skill {skill_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
