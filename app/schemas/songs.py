def song_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": str(item["title"])
    }


def song_list_entity(entity) -> list:
    return [song_entity(item) for item in entity]
