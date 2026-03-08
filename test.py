from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message":"Hello world"}

@app.get("/products/{product_id}")
def products(product_id:int):
    return {"Product id":product_id}

@app.get("/search/")
def search(name:str,age:int):
    return  {"name":name,"age":age}