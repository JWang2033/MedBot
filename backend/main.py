from fastapi import FastAPI
from backend.routes import ask

app = FastAPI()

# Include the ask route
app.include_router(ask.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
