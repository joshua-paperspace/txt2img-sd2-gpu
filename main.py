from fastapi import FastAPI
from fastapi.responses import FileResponse
from pipeline import pipe


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/generate")
async def predict(prompt: str):
    image = pipe(prompt).images[0]
    image.save("low_res.png")

    return FileResponse('low_res.png', media_type="image/jpeg")