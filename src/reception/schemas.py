from datetime import time, date, datetime
from typing import Optional
from pydantic import BaseModel


class ReceptionRead(BaseModel):
    user_id: int
    service_id: int
    recording_date: date
    start_time: time
    end_time: time


class ReceptionCreate(BaseModel):
    user_id: int
    service_id: int
    recording_date: date = date.today()
    start_time: time = datetime.now().time()
    end_time: time = datetime.now().time()


class ReceptionUpdate(BaseModel):
    user_id: Optional[int]
    service_id: Optional[int]
    recording_date: Optional[date] = date.today()
    start_time: Optional[time] = datetime.now().time()
    end_time: Optional[time] = datetime.now().time()
