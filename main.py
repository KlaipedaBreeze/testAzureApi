from fastapi import FastAPI

app = FastAPI(__name__)


@app.get("/")
def home():
    print("Hello")





