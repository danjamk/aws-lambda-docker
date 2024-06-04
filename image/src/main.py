import uvicorn
from fastapi import FastAPI, Request
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)