Good idea, Darshan. Keeping clean notes is exactly what good engineers do. Below are structured notes from Step 1 → Step 6 based on what you have learned so far.
You can save this as FastAPI_Notes.md or FastAPI_Notes.txt.

---

FastAPI Notes (Beginner → Current Progress)

1. What is an API
   API (Application Programming Interface) allows two software systems to communicate.
   Example:
   Frontend → API → Backend Server → Database
   Example request:
   GET /users
   Example response:
   [
   {"name":"Darshan"},
   {"name":"Alex"}
   ]
   APIs are used in:
   • Web applications
   • Mobile apps
   • Games
   • AI systems
   • Cloud services

---

2. HTTP Methods
   APIs communicate using HTTP methods.
   Method Purpose
   GET Retrieve data
   POST Create data
   PUT Update data
   DELETE Remove data
   Example:
   GET /users
   POST /users
   DELETE /users/10

---

3. What is FastAPI
   FastAPI is a modern Python framework for building APIs.
   Advantages:
   • Very fast performance
   • Automatic documentation
   • Data validation
   • Async support
   • Easy to learn
   Used by companies like:
   • Uber
   • Netflix
   • Microsoft

---

4. Installing FastAPI
   Install required packages:
   pip install fastapi uvicorn
   Explanation:
   Package Purpose
   FastAPI API framework
   Uvicorn ASGI server to run the API
   Run server using:
   uvicorn main:app --reload

---

5. Basic FastAPI Application
   Example code:
   from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
return {"message": "Hi Darshan"}
Open in browser:
http://127.0.0.1:8000/
Response:
{
"message": "Hi Darshan"
}

---

6. API Documentation
   FastAPI automatically generates documentation.
   Swagger UI:
   http://127.0.0.1:8000/docs
   Another documentation format:
   http://127.0.0.1:8000/redoc
   These allow testing APIs without Postman.

---

7. Routes (Endpoints)
   Routes define API paths.
   Example:
   @app.get("/")
   def home():
   return {"message": "Hello"}
   Example routes:
   /
   /about
   /users
   /products
   Example:
   @app.get("/about")
   def about():
   return {"app": "FastAPI Learning"}
   Test:
   http://127.0.0.1:8000/about

---

8. Path Parameters (Dynamic Routes)
   Used when API needs dynamic values.
   Example:
   /users/1
   /users/2
   /users/100
   Example code:
   @app.get("/user/{user_id}")
   def get_user(user_id: int):
   return {"user_id": user_id}
   Test:
   http://127.0.0.1:8000/user/10
   Response:
   {
   "user_id": 10
   }
   FastAPI automatically validates the type.
   Example error case:
   /user/abc

---

9. Query Parameters
   Used for filtering data.
   Example:
   /products?limit=10
   /search?name=darshan&age=22
   Example code:
   @app.get("/search")
   def search(name: str, age: int):
   return {"name": name, "age": age}
   Test:
   http://127.0.0.1:8000/search?name=darshan&age=22
   Response:
   {
   "name": "darshan",
   "age": 22
   }
   Query parameters are used in real systems for:
   • Pagination
   • Filtering
   • Searching
   Example:
   /products?page=2
   /products?category=mobile
   /products?limit=20

---

10. POST Requests
    POST is used to create data.
    Example APIs:
    POST /login
    POST /signup
    POST /create-user
    Basic example:
    @app.post("/create-user")
    def create_user(name: str, age: int):
    return {"name": name, "age": age}
    Test:
    http://127.0.0.1:8000/create-user?name=darshan&age=22
    Response:
    {
    "name": "darshan",
    "age": 22
    }
    But this method is not professional. Real APIs send JSON request bodies.
    Example:
    {
    "name": "darshan",
    "age": 22
    }
    Handling JSON requests requires Pydantic Models.
    (This is the next topic.)

---

11. Current FastAPI Code Example
    Example application combining everything learned:
    from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
return {"message": "Hi Darshan"}

@app.get("/products/{product_id}")
def products(product_id: int):
return {"product_id": product_id}

@app.get("/search")
def search(name: str, age: int):
return {"name": name, "age": age}

@app.post("/create-user")
def create_user(name: str, age: int):
return {"name": name, "age": age}

---

Concepts Learned So Far
You now understand:

1. API fundamentals
2. HTTP methods
3. FastAPI setup
4. Running FastAPI server
5. API routes
6. Path parameters
7. Query parameters
8. Basic POST requests
   These are core API fundamentals used in every backend framework.
