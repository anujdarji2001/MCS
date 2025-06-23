from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.api.deps import get_current_user
from app.db.database import db
from bson import ObjectId, errors
from app.utils.nosql_sanitize import check_for_nosql_injection

router = APIRouter()

@router.post("/", response_model=TaskOut)
async def create_task(task: TaskCreate, user=Depends(get_current_user)):
    check_for_nosql_injection(task.dict())
    task_dict = task.dict()
    task_dict["owner_id"] = str(user["_id"])
    result = await db.tasks.insert_one(task_dict)
    task_dict["id"] = str(result.inserted_id)
    return TaskOut(**task_dict)

@router.get("/", response_model=list[TaskOut])
async def list_tasks(user=Depends(get_current_user)):
    tasks = await db.tasks.find({"owner_id": str(user["_id"])}).to_list(100)
    for t in tasks:
        t["id"] = str(t["_id"])
    return [TaskOut(**t) for t in tasks]

@router.put("/{task_id}", response_model=TaskOut)
async def update_task(task_id: str, task: TaskUpdate, user=Depends(get_current_user)):
    check_for_nosql_injection(task.dict(exclude_unset=True))
    try:
        obj_id = ObjectId(task_id)
    except errors.InvalidId:
        raise HTTPException(status_code=400, detail="Invalid task ID")
    db_task = await db.tasks.find_one({"_id": obj_id})
    if not db_task or db_task["owner_id"] != str(user["_id"]):
        raise HTTPException(status_code=404, detail="Task not found")
    await db.tasks.update_one({"_id": obj_id}, {"$set": task.dict(exclude_unset=True)})
    updated = await db.tasks.find_one({"_id": obj_id})
    updated["id"] = str(updated["_id"])
    return TaskOut(**updated)

@router.delete("/{task_id}")
async def delete_task(task_id: str, user=Depends(get_current_user)):
    try:
        obj_id = ObjectId(task_id)
    except errors.InvalidId:
        raise HTTPException(status_code=400, detail="Invalid task ID")
    db_task = await db.tasks.find_one({"_id": obj_id})
    if not db_task or db_task["owner_id"] != str(user["_id"]):
        raise HTTPException(status_code=404, detail="Task not found")
    await db.tasks.delete_one({"_id": obj_id})
    return {"msg": "Task deleted"} 