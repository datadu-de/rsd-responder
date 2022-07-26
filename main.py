from pprint import pprint

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root_get(request: Request):

    ret = {
        "query_params": dict(request.query_params),
        "headers": dict(request.headers),
        "method": request.method,
        "body": b"",
    }

    pprint(ret, indent=2, depth=10)
    return ret


@app.post("/")
async def root_post(request: Request):

    body = await request.body()

    ret = {
        "query_params": dict(request.query_params),
        "headers": dict(request.headers),
        "method": request.method,
        "body": body,
    }

    pprint(ret, indent=2, depth=10)
    return ret
