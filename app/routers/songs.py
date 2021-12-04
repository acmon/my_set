from fastapi import APIRouter, HTTPException
from uuid import uuid4, UUID
from typing import List
from models.Song import Song


router = APIRouter()

db: List[Song] = [
    Song(id=uuid4(), title="Soul to Squeeze"),
    Song(id=uuid4(), title="Can't Stop"),
    Song(id=uuid4(), title="Venice Queen"),
    Song(id=uuid4(), title="Warped"),
    Song(id=uuid4(), title="Fortune Faded")
]


@router.get("/api/v1/songs")
def get_all_songs():
    return db


@router.get("/api/v1/songs/{song_id}")
def get_song(song_id: UUID):
    result = {}
    for song in db:
        if song.id == song_id:
            result = song

    if result:
        return result
    else:
        raise HTTPException(
            status_code=404,
            detail=f"song with id: {song_id} does not exists"
        )


@router.post("/api/v1/songs")
def create_song(song: Song):
    db.append(song)
    return {"id": song.id}


@router.put("/api/v1/songs/{song_id}")
def edit_song(song: Song, song_id: UUID):
    for i, item in enumerate(db):
        if item.id == song_id:
            db[i] = song
            return
    raise HTTPException(
        status_code=404,
        detail=f"song with id: {song_id} does not exists"
    )


@router.delete("/api/v1/songs/{song_id}")
def delete_song(song_id: UUID):
    for song in db:
        if song.id == song_id:
            db.remove(song)
            return
    raise HTTPException(
        status_code=404,
        detail=f"song with id: {song_id} does not exists"
    )
