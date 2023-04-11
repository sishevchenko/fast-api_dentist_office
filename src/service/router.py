from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from src.database import get_async_session
from src.service.models import Service
from src.service.schemas import ServiceReed, ServiceCreate, ServiceUpdate

router = APIRouter(
    prefix="/service",
    tags=["Service"]
)


@router.get("/")
@cache(expire=30)
async def get_all_service(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Service)
        res = await session.execute(query)
        return res.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.get("/{service_id}")
@cache(expire=30)
async def get_service(service_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Service).where(Service.id == service_id)
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.post("/")
async def service_create(new_service: ServiceCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Service).values(**new_service.dict())
        await session.execute(stmt)
        await session.commit()
        return {201: "Created"}
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.put("/{service_id}")
async def service_update(service_id: int, new_service: ServiceUpdate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = update(Service).where(Service.id == service_id).values(**new_service.dict(exclude_unset=True))
        await session.execute(stmt)
        await session.commit()
        return {200: "OK"}
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.delete("/{service_id}")
async def service_delete(service_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(Service).where(Service.id == service_id).returning(Service)
        await session.execute(stmt)
        await session.commit()
        return None
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })
