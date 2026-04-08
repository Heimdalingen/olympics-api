"""FastAPI application entry point."""
from fastapi import FastAPI
from app.database import Base, engine
app = FastAPI(title="Olympics API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    """Health check endpoint."""
    return {"message": "Olympics API is running"}