from __future__ import annotations

from typing import Optional
from uuid import uuid4

from fastapi import FastAPI, Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Resource Management API")

# In-memory storage: id -> resource
resources: dict[str, "Resource"] = {}


class ResourceIn(BaseModel):
    name: str
    type: str


class Resource(ResourceIn):
    id: str


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=400, content={"detail": "Invalid input"})


@app.post("/resources", response_model=Resource)
def create_resource(payload: ResourceIn) -> Resource:
    resource = Resource(id=str(uuid4()), **payload.dict())
    resources[resource.id] = resource
    return resource


@app.get("/resources", response_model=list[Resource])
def list_resources(type: Optional[str] = Query(default=None)) -> list[Resource]:
    items = list(resources.values())
    if type is not None:
        items = [r for r in items if r.type == type]
    return items

@app.get("/health")
def health():
    return {"status": "ok"}


