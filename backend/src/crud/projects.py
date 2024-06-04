from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Projects
from src.schemas.projects import ProjectOutSchema


async def get_projects():
    return await ProjectOutSchema.from_queryset(Projects.all())


async def get_project(project_id) -> ProjectOutSchema:
    return await ProjectOutSchema.from_queryset_single(Projects.get(id=project_id))


async def create_sproject(project, current_user) -> ProjectOutSchema:
    project_dict = project.dict(exclude_unset=True)
    project_dict["author_id"] = current_user.id
    project_obj = await Projects.create(**project_dict)
    return await ProjectOutSchema.from_tortoise_orm(project_obj)


async def update_project(project_id, project, current_user) -> ProjectOutSchema:
    try:
        db_project = await ProjectOutSchema.from_queryset_single(Projects.get(id=project_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Project {project_id} not found")

    if db_project.author.id == current_user.id:
        await Projects.filter(id=project_id).update(**project.dict(exclude_unset=True))
        return await ProjectOutSchema.from_queryset_single(Projects.get(id=project_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_project(project_id, current_user):
    try:
        db_project = await ProjectOutSchema.from_queryset_single(Projects.get(id=project_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Project {project_id} not found")

    if db_project.author.id == current_user.id:
        deleted_count = await Projects.filter(id=project_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Project {project_id} not found")
        return f"Deleted project {project_id}"

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
