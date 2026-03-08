from fastapi import FastAPI
from pydantic import BaseModel

# class Product(BaseModel):
#     name : str
#     price : float


app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message":"Hi Darshan"}

# @app.get("/about")
# def about():
#     return {"app":"FastAPI Learning","developer":"Darshan"}

# @app.get("/user_id/{user_id}")
# def user_id(user_id:int):
#     return {"user_id":user_id} 


# @app.get("/products/")
# def products(product_id:int,name:str):
#     return {"Product id":product_id,
#             "Product name":name
#             }

# @app.get("/search/")
# def search(name:str,age:int):
#     return {"name":name,
#             "age":age
#             }

# @app.post("/product/")
# def create_product(product:Product):
#     return product


add_items = []

@app.post("/items")
def items(item:str):
    add_items.append(item)
    return add_items

@app.get("/search/{id}")
def search(id:int):
    if id > len(add_items):
        return {"no item":"Item not found"}
    else:
        return {"Item":add_items[id]}

@app.get("/")
def read_root():
    return {"message":"Hello world"}