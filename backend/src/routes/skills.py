from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.skills as crud
from src.auth.jwthandler import get_current_user
from src.schemas.skills import SkillOutSchema, SkillInSchema, UpdateSkill
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/skills",
    response_model=List[SkillOutSchema],
    tags=["Skills"]
)
async def get_skills():
    return await crud.get_skills()


@router.get(
    "/skill/{skill_id}",
    response_model=SkillOutSchema,
    tags=["Skills"]
)
async def get_skill(skill_id: int) -> SkillOutSchema:
    try:
        return await crud.get_skill(skill_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="skill does not exist",
        )


@router.post(
    "/skills", response_model=SkillOutSchema, dependencies=[Depends(get_current_user)], tags=["Skills"]
)
async def create_skill(
    skill: SkillInSchema, current_user: SkillOutSchema = Depends(get_current_user)
) -> SkillOutSchema:
    return await crud.create_skill(skill, current_user)


@router.patch(
    "/skill/{skill_id}",
    dependencies=[Depends(get_current_user)],
    response_model=SkillOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
    tags=["Skills"]
)
async def update_skill(
    skill_id: int,
    skill: UpdateSkill,
    current_user: SkillOutSchema = Depends(get_current_user),
) -> SkillOutSchema:
    return await crud.update_skill(skill_id, skill, current_user)


@router.delete(
    "/skill/{skill_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
    tags=["Skills"]
)
async def delete_skill(
    skill_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_skill(skill_id, current_user)
