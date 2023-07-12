from fastapi import FastAPI

from controller import UserController, Fast

app = FastAPI()

app.include_router(Fast.router)
app.include_router(UserController.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
