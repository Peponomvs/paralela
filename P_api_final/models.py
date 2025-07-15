from pydantic import BaseModel, Field, HttpUrl
from typing import Dict, Optional

class CodeInfo(BaseModel):
    code: str
    name: str

class CountStat(BaseModel):
    count: int
    percentage: float

class AgeStat(BaseModel):
    min: float
    max: float
    mean: float
    stddev: float

class ProblemDetail(BaseModel):
    type: HttpUrl
    title: str
    status: int
    detail: str
    instance: HttpUrl
    properties: Optional[Dict[str, str]]
