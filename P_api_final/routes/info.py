from fastapi import APIRouter, HTTPException
from models import CodeInfo, ProblemDetail
from db import get_connection

router = APIRouter()

@router.get("/v1/info/strata", response_model=list[CodeInfo], responses={404: {"model": ProblemDetail}})
def get_strata():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT code, name FROM strata")
        rows = cur.fetchall()
    if not rows:
        raise HTTPException(status_code=404, detail="No hay información de estratos disponible")
    return [{"code": r[0], "name": r[1]} for r in rows]

@router.get("/v1/info/species", response_model=list[CodeInfo], responses={404: {"model": ProblemDetail}})
def get_species():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT code, name FROM species")
        rows = cur.fetchall()
    if not rows:
        raise HTTPException(status_code=404, detail="No hay información de especies disponible")
    return [{"code": r[0], "name": r[1]} for r in rows]

@router.get("/v1/info/genders", response_model=list[CodeInfo], responses={404: {"model": ProblemDetail}})
def get_genders():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT code, name FROM genders")
        rows = cur.fetchall()
    if not rows:
        raise HTTPException(status_code=404, detail="No hay información de géneros disponible")
    return [{"code": r[0], "name": r[1]} for r in rows]
