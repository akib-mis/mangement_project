import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Depends, FastAPI
from config.config import session_maker, engine, create_tables
from routers.routers import router as product_router
from models.products import Products


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:3030",
    "http://localhost:3009",
]

app = FastAPI(title="Products")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(product_router)

# Products.Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def on_startup():
    
    create_tables()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")