from fastapi import FastAPI


app=FastAPI()


@app.get("/")
def home():
    return {"Message":"Hello from github actions"}



@app.get("/health")
def health():
    return {"status":"ok"}