# main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env (only for local dev)
load_dotenv()

# Fetch the port from environment or default to 3030
PORT = int(os.getenv("PORT", 3030))

# Create FastAPI app
app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
# Allow requests from any origin, but only GET methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any domain
    allow_methods=["GET"],  # Restrict allowed HTTP methods
    allow_headers=["*"],
)

# Define a route for /products
@app.get("products")
async def get_products():
    # Return JSON array of product objects
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]


if __name__ == "__main__":
    import uvicorn
    # Start the web server
    uvicorn.run("src.main:app", host="0.0.0.0", port=PORT, reload=True)
