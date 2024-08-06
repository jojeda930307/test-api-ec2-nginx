from fastapi import FastAPI
from database.db import Base, engine
from routers import auth, books, endpoint_test

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(books.router)
app.include_router(endpoint_test.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
