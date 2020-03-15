from fastapi import APIRouter, HTTPException, Response
from app.models.installation import Installation
from typing import List


installation = APIRouter()
INSTALLATIONS = {}  # In memory store


@installation.get("/", response_model=List[Installation])
async def get_installations():
    return list(INSTALLATIONS.values())


@installation.post("/")
async def post_installation(installations: List[Installation]):
    for installation in installations:
        INSTALLATIONS[installation.id] = installation.dict()
    return Response()


@installation.put("/{installation_id}")
async def put_installation(installation_id: int, installation: Installation):
    installation.id = installation_id
    INSTALLATIONS[installation_id] = installation.dict()
    return Response()


@installation.get("/{installation_id}", response_model=Installation)
async def get_installation(installation_id: int):
    if installation_id not in INSTALLATIONS:
        raise HTTPException(status_code=404, detail='installation not found')
    try:
        installation = INSTALLATIONS[installation_id]
        return installation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
