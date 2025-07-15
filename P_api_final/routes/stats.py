from fastapi import APIRouter, HTTPException, Query
from models import CountStat, ProblemDetail
from db import get_connection

router = APIRouter()

@router.get("/v1/stats/count", response_model=CountStat, responses={
    400: {"model": ProblemDetail},
    404: {"model": ProblemDetail}
})
def get_count(
    speciesCode: str = Query(...),
    strataCode: str = Query(...),
    genderCode: str = Query(...)
):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT count, percentage FROM stats
            WHERE species_code = %s AND strata_code = %s AND gender_code = %s
        """, (speciesCode, strataCode, genderCode))
        result = cur.fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="No hay datos disponibles para los filtros proporcionados")
    return {"count": result[0], "percentage": result[1]}

@router.get("/v1/stats/age", response_model=AgeStat, responses={
    400: {"model": ProblemDetail},
    404: {"model": ProblemDetail}
})
def get_age_stats(
    speciesCode: str = Query(...),
    strataCode: str = Query(...),
    genderCode: str = Query(...)
):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT MIN(age), MAX(age), AVG(age), STDDEV(age) FROM individuals
            WHERE species_code = %s AND strata_code = %s AND gender_code = %s
        """, (speciesCode, strataCode, genderCode))
        result = cur.fetchone()
    if not result or result[0] is None:
        raise HTTPException(status_code=404, detail="No hay datos disponibles para los filtros proporcionados")
    return {
        "min": result[0],
        "max": result[1],
        "mean": result[2],
        "stddev": result[3]
    }
