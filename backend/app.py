from fastapi import FastAPI

app = FastAPI(
    title="AI Data Analyst Agent",
    description="AI-powered automated data analysis system",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Data Analyst Agent API is running"
    }
