from fastapi import FastAPI
from api.routers import questions, users, auth, questionHistory
from fastapi.middleware.cors import CORSMiddleware
from api import models
from api.database import engine
import uvicorn

# Initialize a FastAPI instance.
app = FastAPI(title="MathEase")

# Enable CORS middleware
origins = [
    "https://r6mjxn.deta.dev"
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database migration
models.Base.metadata.create_all(bind=engine)

# Index page
@app.get('/')
def index():
    return {'message': 'Welcome to MathBuddy!'}

# Include routes from other router files
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(questionHistory.router)

# Run uvicorn server
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
    