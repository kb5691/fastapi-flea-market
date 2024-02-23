from fastapi import FastAPI

app = FastAPI()

# デコレーター(@の部分)
@app.get("/test")
async def example():
  return {"message": "hello world"}
