from fastapi import APIRouter
from app.api.deps import SessionDep

router = APIRouter(
    prefix="/user"
)

#
# @router.get("/{id}")
# async def get(id: str):
#     return id


@router.get("/{id")
async def test(session: SessionDep, id: str):

    return id
