"""TommyTech main application module.

This is the entry point for the TommyTech platform service.
"""

import os
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI
from fastapi.responses import JSONResponse

log = structlog.get_logger()

VERSION = os.environ.get("TOMMTECH_VERSION", "0.1.0")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle management."""
    log.info("startup", version=VERSION)
    yield
    log.info("shutdown")


app = FastAPI(
    title="TommyTech Platform",
    description="Multi-service technology platform API",
    version=VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/api/openapi.json",
)


@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint."""
    return JSONResponse(
        status_code=200,
        content={"status": "healthy", "version": VERSION},
    )


@app.get("/", tags=["root"])
async def root():
    """Root endpoint."""
    return JSONResponse(
        content={"message": "TommyTech Platform API", "version": VERSION},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
