from fastapi import FastAPI
from backend.routes import ask
from backend.config import config

app = FastAPI()

app.include_router(ask.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.HOST, port=config.PORT)
