from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    titulo: str
    completada: bool = False

tasks: List[Task] = []

@app.get("/")
def readRoot():
    return {"mensaje": "Bienvenido a la API de tareas"}

@app.get("/tareas")
def getTask():
    return tasks

@app.post("/tareas")
def createTask(task: Task):
    tasks.append(task)
    return {"mensaje": "Tarea creada", "tarea": task}

@app.get("/tareas/{tarea_id}")
def getTaskId(tarea_id: int):
    for tarea in tasks:
        if tarea.id == tarea_id:
            return tarea
    return {"error": "Tarea no encontrada"}

@app.delete("/tareas/{tarea_id}")
def deleteTask(tarea_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != tarea_id]
    return {"mensaje": f"Tarea {tarea_id} eliminada"}
