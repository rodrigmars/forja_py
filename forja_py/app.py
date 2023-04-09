import time
from contextlib import contextmanager


@contextmanager
def timer(label: str):
    start: float = time.perf_counter()

    try:
        yield
    finally:
        end: float = time.perf_counter()
        print(f'{label}:{end - start:.3f} secs')


def kill_time():
    time.sleep(1)


with timer("Func"):
    kill_time()
