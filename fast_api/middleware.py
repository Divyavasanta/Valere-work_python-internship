import time
from fastapi import FastAPI, Request, Response


app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}"
    
    print(f"Request to '{request.url.path}' took {process_time:.4f} seconds.")
    return response



@app.get("/")
async def root():
    return {"message": "Welcome to my application!"}
