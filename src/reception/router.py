from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.reception.models import Reception
from src.reception.schemas import ReceptionRead, ReceptionCreate, ReceptionUpdate

router = APIRouter(
    prefix="/reception",
    tags=["Reception"]
)


@router.get("/")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    query = select(Reception)
    res = await session.execute(query)
    return res.scalars().all()


@router.get("/{reception_id}")
async def get(reception_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Reception).where(Reception.id == reception_id)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/")
async def reception_create(new_reception: ReceptionCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Reception).values(**new_reception.dict())
    await session.execute(stmt)
    await session.commit()
    return {201: "Created"}


@router.put("/{reception_id}")
async def reception_update(reception_id: int, new_reception: ReceptionUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Reception).where(Reception.id == reception_id).values(**new_reception.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {200: "OK"}


@router.delete("/{reception_id}")
async def reception_delete(reception_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Reception).where(Reception.id == reception_id).returning(Reception)
    await session.execute(stmt)
    await session.commit()
    return None
