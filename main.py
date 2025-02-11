from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def auth():
    return JSONResponse(content={"status": "Running"})