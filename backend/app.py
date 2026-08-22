from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.search import router as search_router
from routes.upload import router as upload_router

app = FastAPI(title="StudyMate AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload_router)
app.include_router(search_router)


@app.get("/")
def home():
    return {"message": "StudyMate AI Backend Running"}