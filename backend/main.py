from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from EventFlow!"}

handler = Mangum(app)