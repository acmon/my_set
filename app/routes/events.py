from fastapi import APIRouter, HTTPException
from uuid import uuid4, UUID
from typing import List
from models.Event import Event


router = APIRouter()

db: List[Event] = [
    Event(id=uuid4(), avenue="Rio de Janeiro", datetime='2021-01-15 20:25'),
    Event(id=uuid4(), avenue="São Paulo", datetime='2022-02-12 21:55'),
    Event(id=uuid4(), avenue="Nova Friburgo", datetime='2022-02-18 18:30'),
    Event(id=uuid4(), avenue="Brasília", datetime='2022-03-11 17:15'),
    Event(id=uuid4(), avenue="Salvador", datetime='2022-05-10 22:00')
]


@router.get("/api/v1/events")
def get_all_events():
    return db


@router.get("/api/v1/events/{event_id}")
def get_event(event_id: UUID):
    result = {}
    for song in db:
        if song.id == event_id:
            result = song

    if result:
        return result
    else:
        raise HTTPException(
            status_code=404,
            detail=f"event with id: {event_id} does not exists"
        )


@router.post("/api/v1/events")
def create_event(event: Event):
    db.append(event)
    return {"id": event.id}


@router.put("/api/v1/events/{event_id}")
def edit_event(event: Event, event_id: UUID):
    for i, item in enumerate(db):
        if item.id == event_id:
            db[i] = event
            return
    raise HTTPException(
        status_code=404,
        detail=f"event with id: {event_id} does not exists"
    )


@router.delete("/api/v1/events/{event_id}")
def delete_event(event_id: UUID):
    for event in db:
        if event.id == event_id:
            db.remove(event)
            return
    raise HTTPException(
        status_code=404,
        detail=f"event with id: {event_id} does not exists"
    )
