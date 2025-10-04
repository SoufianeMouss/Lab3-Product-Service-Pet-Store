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
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ambitious-sea-0420d630f.1.azurestaticapps.net"
    ],  # your SWA frontend URL
    allow_credentials=True,
    allow_methods=["*"],
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