from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.spider2ybanana.com",
    "http://localhost.spider2ybanana.com:8080",
    "https://spider2ybanana.com",
    "http://www.spider2ybanana.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
