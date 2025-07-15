# ISEKAI API Clone (FastAPI + PostgreSQL)

Este proyecto es una réplica funcional del API publicado en https://api.sebastian.cl/isekai/swagger-ui/index.html, desarrollada en **FastAPI** y conectada a una base de datos **PostgreSQL**.

## 📦 Estructura de Carpetas

```
isekai_api/
├── main.py              # Punto de entrada de la app FastAPI
├── models.py            # Esquemas de datos (Pydantic)
├── db.py                # Conexión a PostgreSQL
├── requirements.txt     # Dependencias del proyecto
└── routes/
    ├── info.py          # Rutas de /v1/info/*
    └── stats.py         # Rutas de /v1/stats/*
```

## ⚙️ Requisitos

- Python 3.11+
- PostgreSQL 16.9
- Sistema Ubuntu Server 24.04 (o compatible)

## 🚀 Instalación y ejecución

1. **Clona o descomprime el repositorio:**

```bash
unzip isekai_api_updated.zip
cd isekai_api
```

2. **Instala las dependencias:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Ejecuta el servidor:**

```bash
uvicorn main:app --reload
```

4. **Accede a la documentación Swagger:**

- Swagger UI: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json

## 🔗 Conexión a Base de Datos

Edita `db.py` si necesitas cambiar las credenciales:

```python
psycopg2.connect(
    dbname="isekaidb",
    user="isekai",
    password="Fr9tL28mQxD7vKcp",
    host="159.223.200.213",
    port=5432
)
```

## ✅ Endpoints disponibles

- `GET /v1/info/strata`
- `GET /v1/info/species`
- `GET /v1/info/genders`
- `GET /v1/stats/count`
- `GET /v1/stats/age`

Todos devuelven respuestas estructuradas según OpenAPI, y manejan correctamente errores 400/404/500.

## 📄 Licencia

Uso académico / educativo.
