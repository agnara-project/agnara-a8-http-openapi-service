import os
import uvicorn
from src.app.server import app

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    print(f"Starting Order API server on {host}:{port}...")
    uvicorn.run(app, host=host, port=port)
