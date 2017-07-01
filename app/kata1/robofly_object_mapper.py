from app.kata1.robofly import Robofly

def encode_robofly(robofly):
    return {
        "_type": "robofly",
        "id": robofly.robofly_id,
        "name": robofly.name,
        "constructionYear": robofly.construction_year,
        "size": robofly.size,
        "serviceTime": robofly.service_time,
        "status": robofly.status
    }

def decode_robofly(robofly_document):
    assert robofly_document["_type"] == "robofly"
    return Robofly(
        robofly_document["id"],
        robofly_document["name"],
        robofly_document["constructionYear"],
        robofly_document["size"],
        robofly_document["serviceTime"],
        robofly_document["status"],
    )
