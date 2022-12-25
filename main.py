# Dependancies
from fastapi import Depends, FastAPI, Body

app = FastAPI()


# async def common_parameters(
#     q: str | None = None,
#     skip: int = 0,
#     limit: int = 100
# ):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons


# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameters)):
#     return commons


# Classes as Dependencies
# fake_items_db = [
#     {"item_name": "Foo"}, {"item_name": "Bar"},
#     {"item_name": "Baz"}
# ]


# class CommonQueryParams:
#     def __init__(
#         self, q: str | None = None, skip: int = 0, limit: int = 100
#     ):
#         self.q = q
#         self.skip = skip
#         self.limit = limit

    
# @app.get("/items/")
# async def read_items(commons = Depends(CommonQueryParams)):
#     response = {}
#     if commons.q:
#         response.update(
#             {"q": commons.q}
#         )
#     items = fake_items_db[commons.skip : commons.skip + commons.limit]

#     response.update({"items": items})

#     return response


def query_extractor(q: str | None = None):
    return q


def query_or_body_extractor(
    q: str = Depends(query_extractor),
    last_query: str | None = Body(None)
):
    if q:
        return q
    return last_query

@app.post("/items/")
async def try_query(query_or_body: str = Depends(query_or_body_extractor)):
    return {"q_or_body": query_or_body}
