from fastapi import FastAPI

from routers import songs, events

app = FastAPI()

app.include_router(songs.router)
app.include_router(events.router)
