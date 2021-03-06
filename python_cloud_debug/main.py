import os
from typing import Optional
from asyncio import sleep
from fastapi import FastAPI


if "LOCAL" not in os.environ:
    try:
        import googleclouddebugger
        import googlecloudprofiler
        googleclouddebugger.enable(breakpoint_enable_canary=True)
        googlecloudprofiler.start(
            service='python-cloud-debug',
            service_version='1.0.1',
            # 0-error, 1-warning, 2-info, 3-debug
            verbose=3,
            project_id="serverless-251114",
        )
    except (ValueError, NotImplementedError) as exc:
        print(exc)

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    await sleep(2)
    return {"item_id": item_id, "q": q}
