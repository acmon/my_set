from fastapi import APIRouter, HTTPException
from uuid import uuid4, UUID
from typing import List

from models.Song import Song
from config.db import client
from schemas.songs import song_entity, song_list_entity


router = APIRouter()


@router.get("/api/v1/songs")
def get_all_songs():
    return song_list_entity(client.my_set.songs.find())


# @router.get("/api/v1/songs/{song_id}")
# def get_song(song_id: UUID):
#     result = {}
#     for song in db:
#         if song.id == song_id:
#             result = song
#
#     if result:
#         return result
#     else:
#         raise HTTPException(
#             status_code=404,
#             detail=f"song with id: {song_id} does not exists"
#         )


@router.post("/api/v1/songs")
def create_song(song: Song):
    client.my_set.songs.insert_one(dict(song))


# @router.put("/api/v1/songs/{song_id}")
# def edit_song(song: Song, song_id):
#     client.my_set.songs.find_one_and_update({"_id": objectId(song_id)})


# @router.delete("/api/v1/songs/{song_id}")
# def delete_song(song_id: UUID):
#     for song in db:
#         if song.id == song_id:
#             db.remove(song)
#             return
#     raise HTTPException(
#         status_code=404,
#         detail=f"song with id: {song_id} does not exists"
#     )
