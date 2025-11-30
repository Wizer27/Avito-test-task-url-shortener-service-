from fastapi import FastAPI,Header,HTTPException,status
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/")
async def main():
    return {"API":"URL SHORTENER"}
