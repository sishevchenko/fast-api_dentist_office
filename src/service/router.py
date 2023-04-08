from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.service.models import Service
from src.service.schemas import ServiceReed, ServiceCreate, ServiceUpdate

router = APIRouter(
    prefix="/service",
    tags=["Service"]
)


@router.get("/")
async def get_all_service(session: AsyncSession = Depends(get_async_session)):
    query = select(Service)
    res = await session.execute(query)
    return res.scalars().all()


@router.get("/{service_id}")
async def get_service(service_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Service).where(Service.id == service_id)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/")
async def service_create(new_service: ServiceCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Service).values(**new_service.dict())
    await session.execute(stmt)
    await session.commit()
    return {201: "Created"}


@router.put("/{service_id}")
async def service_update(service_id: int, new_service: ServiceUpdate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Service).where(Service.id == service_id).values(**new_service.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {200: "OK"}


@router.delete("/{service_id}")
async def service_delete(service_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Service).where(Service.id == service_id).returning(Service)
    await session.execute(stmt)
    await session.commit()
    return None
