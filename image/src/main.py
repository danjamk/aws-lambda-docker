
from fastapi import FastAPI, Request
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root():
    return {"message": "Hello World"}