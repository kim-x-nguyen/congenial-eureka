import imp
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI
from routes.api import router as api_router

app = FastAPI(title="FastAPI Demo", description="This is a FastAPI demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005,
                log_level="info", reload=True)
    print("running")
