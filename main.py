from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hi Darshan"}

@app.get("/about")
def about():
    return {"app":"FastAPI Learning","developer":"Darshan"}

@app.get("/user_id/{user_id}")
def user_id(user_id:int):
    return {"user_id":user_id} 


@app.get("/products/")
def products(product_id:int,name:str):
    return {"Product id":product_id,
            "Product name":name
            }

@app.get("/search/")
def search(name:str,age:int):
    return {"name":name,
            "age":age
            }