from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.projects as crud
from src.auth.jwthandler import get_current_user
from src.schemas.projects import ProjectOutSchema, ProjectInSchema, UpdateProject
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/projects",
    response_model=List[ProjectOutSchema],
    tags=["Project"]
)
async def get_projects():
    return await crud.get_projects()


@router.get(
    "/project/{project_id}",
    response_model=ProjectOutSchema,
    tags=["Project"]
)
async def get_project(project_id: int) -> ProjectOutSchema:
    try:
        return await crud.get_project(project_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Project does not exist",
        )


@router.post(
    "/project", response_model=ProjectOutSchema, dependencies=[Depends(get_current_user)], tags=["Project"]
)
async def create_project(
    project: ProjectInSchema, current_user: ProjectOutSchema = Depends(get_current_user)
) -> ProjectOutSchema:
    return await crud.create_project(project, current_user)


@router.patch(
    "/project/{project_id}",
    dependencies=[Depends(get_current_user)],
    response_model=ProjectOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
    tags=["Project"]
)
async def update_project(
    project_id: int,
    project: UpdateProject,
    current_user: ProjectOutSchema = Depends(get_current_user),
) -> ProjectOutSchema:
    return await crud.update_project(project_id, project, current_user)


@router.delete(
    "/project/{project_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
    tags=["Project"]
)
async def delete_project(
    project_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_project(project_id, current_user)
