import os, math
from typing import Optional, List
from fastapi import FastAPI


def is_prime(n: int) -> bool:
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def generate_prime_numbers(n: int) -> List[int]:
    prime_numbers: List[int] = []
    num = 2
    while len(prime_numbers) < n:
        if is_prime(num):
            prime_numbers.append(num)
        num += 1
    return prime_numbers


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
        )
    except (ValueError, NotImplementedError) as exc:
        print(exc)

app = FastAPI()


@app.get("/")
def read_root():
    print(generate_prime_numbers(30000)[:100])
    return {"hello": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    print(generate_prime_numbers(30000)[:100])
    return {"item_id": item_id, "q": q}
