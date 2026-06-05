from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import analyzer
import generate

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:5173",
    "https://password-analyzer-frontend.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PasswordRequest(BaseModel):
    password: str
    check: bool = False

@app.post("/analyze")
def analyze_password(data: PasswordRequest):
    return analyzer.analyze(data.password, check=data.check)

@app.get("/generate")
def generate_password(length: int = 12):
    return {"password": generate.generate_password(length)}