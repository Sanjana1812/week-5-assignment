import time

async def request_logger(request, call_next):

    start = time.time()

    response = await call_next(request)

    end = time.time()

    with open("logs.txt", "a") as file:
        file.write(
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{round(end-start,4)} sec\n"
        )

    return response