from fastapi import FastAPI

from app.database import Base, engine
from app.models import business  # noqa: F401
from app.routes.health import router as health_router


app = FastAPI(title="Leadgen AI")
app.include_router(health_router)


@app.on_event("startup")
def create_tables() -> None:
    Base.metadata.create_all(bind=engine)
