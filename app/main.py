"""FastAPI application entry point."""
from app.routers import users, tokens, athletes, countries, sports, events
from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI(title="Olympics API")
app.include_router(users.router)
app.include_router(tokens.router)
app.include_router(sports.router)
app.include_router(events.router)
app.include_router(countries.router)
app.include_router(athletes.router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    """Health check endpoint."""
    return {"message": "Olympics API is running"}
