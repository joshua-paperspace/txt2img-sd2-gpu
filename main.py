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
    image.save("generated_image.jpeg")

    return FileResponse('generated_image.jpeg', media_type="image/jpeg")