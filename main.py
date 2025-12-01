from fastapi import FastAPI,Header,HTTPException,status
from fastapi.responses import RedirectResponse
import uvicorn
import string
from secrets import choice
from database.redis_cli import write_data,get_url_by_slug

def random_slug() -> str:
    ALP = string.ascii_letters + string.digits
    res = ""
    for _ in range(6):
        res += choice(ALP)
    return res    

print(random_slug())



app = FastAPI()

@app.get("/")
async def main():
    return {"API":"URL SHORTENER"}

@app.get("/write/{url}")
async def genrate_slug_write(url:str):
    try:
        slug:str = random_slug()
        write_data(url,slug)
        return slug
    except Exception as e:
        raise HTTPException(status_code = 400,detail = f"Error : {e}")

@app.get("/url/{slug}")
async def rediredt_slug(slug:str):
    try:
        url = get_url_by_slug(slug)
        return RedirectResponse(url = url,slug = slug)
    except Exception as e:
        raise HTTPException(status_code = 400,detail = f"Error : {e}")    
    



if __name__ == "__main__":
    uvicorn.run(app,host = "0.0.0.0",port = 8080)

