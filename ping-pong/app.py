from fastapi import FastAPI

app = FastAPI(title="Ping-pong application")

@app.on_event("startup")
async def start_counter() -> None:
    app.state.counter = -1

@app.get("/pingpong")
async def respond_counter() -> str:
    app.state.counter += 1
    return f"pong {app.state.counter}"