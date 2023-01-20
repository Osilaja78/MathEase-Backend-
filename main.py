from fastapi import FastAPI
from api.routers import questions, users

import uvicorn


app = FastAPI(title="MathBuddy")


@app.get('/')
def index():
    return {'message': 'Welcome to MathBuddy!'}

app.include_router(questions.router)


# solve+3x-10%3D11
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
    