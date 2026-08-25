from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Halo dari devops mini project"}

@app.get("/health")
def health_check():
    return {"Status": "healthy"}