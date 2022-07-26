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
        "url": request.url,
        "path_params": dict(request.path_params),
        "cookies": request.cookies,
    }

    pprint(ret, indent=2, depth=10, compact=False)
    return ret


@app.post("/")
async def root_post(request: Request):

    body = await request.body()

    ret = {
        "query_params": dict(request.query_params),
        "headers": dict(request.headers),
        "method": request.method,
        "body": body,
        "url": request.url,
        "path_params": dict(request.path_params),
        "cookies": request.cookies,
    }

    pprint(ret, indent=2, depth=10, compact=False)
    return ret
