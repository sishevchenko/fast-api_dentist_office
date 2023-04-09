from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
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
    try:
        query = select(Reception)
        res = await session.execute(query)
        return res.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.get("/{reception_id}")
async def get(reception_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Reception).where(Reception.id == reception_id)
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.post("/")
async def reception_create(new_reception: ReceptionCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Reception).values(**new_reception.dict())
        await session.execute(stmt)
        await session.commit()
        return {201: "Created"}
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.put("/{reception_id}")
async def reception_update(reception_id: int, new_reception: ReceptionUpdate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = update(Reception).where(Reception.id == reception_id).values(**new_reception.dict(exclude_unset=True))
        await session.execute(stmt)
        await session.commit()
        return {200: "OK"}
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.delete("/{reception_id}")
async def reception_delete(reception_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(Reception).where(Reception.id == reception_id).returning(Reception)
        await session.execute(stmt)
        await session.commit()
        return None
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })
