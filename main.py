# main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load .env locally (harmless in Azure if no .env exists)
load_dotenv()

# Read environment variables (Azure injects PORT automatically)
PORT = int(os.getenv("PORT", 3030))

app = FastAPI()

# Enable CORS so your Vue frontend can call this API
# Read allowed origins from environment (comma-separated string)
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,   # list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],             # GET, POST, OPTIONS, etc.
    allow_headers=["*"],
)

# Root endpoint just to check health
@app.get("/")
async def root():
    return {"status": "ok"}

# Products endpoint
@app.get("/products")
async def get_products():
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)