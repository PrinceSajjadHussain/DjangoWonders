from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World from server 1!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000,    ssl_certfile=r"C:\Users\Sajjad.Baloch\Desktop\jsbank blink app\updated_load_balancer_elastic\updated code\certfile.pem",
        ssl_keyfile=r"C:\Users\Sajjad.Baloch\Desktop\jsbank blink app\updated_load_balancer_elastic\updated code\keyfile.pem",)
