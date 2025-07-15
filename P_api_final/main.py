from fastapi import FastAPI
from routes import info, stats

app = FastAPI(
    title="ISEKAI API Clone",
    version="1.0.0",
    description="Clon de la API de https://api.sebastian.cl/isekai"
)

app.include_router(info.router)
app.include_router(stats.router)
