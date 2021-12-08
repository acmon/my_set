from fastapi import FastAPI

from routes import songs, events

app = FastAPI()

app.include_router(songs.router)
app.include_router(events.router)
