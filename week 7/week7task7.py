from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/notfound")

def notfound():
    return JSONResponse(content={"message": "Resource Not Found"}, status_code=404)
