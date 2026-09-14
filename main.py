import uvicorn
from src.app.server import app

if __name__ == "__main__":
    print("Starting Order API server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
