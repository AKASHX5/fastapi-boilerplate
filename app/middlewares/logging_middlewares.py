import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("fastapi-boilerplate.middleware")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. Record the start time
        start_time = time.perf_counter()

        # 2. Extract request details
        method = request.method
        path = request.url.path
        client_ip = request.client.host if request.client else "unknown"

        # 3. Process the request
        response = await call_next(request)

        # 4. Calculate duration
        process_time = (
                                   time.perf_counter() - start_time) * 1000  # Convert to ms
        formatted_process_time = "{0:.2f}".format(process_time)

        # 5. Log the result
        logger.info(
            f"IP: {client_ip} | Method: {method} | Path: {path} | "
            f"Status: {response.status_code} | Duration: {formatted_process_time}ms "
        )

        # 6. Optional: Add the duration to the response headers (great for
        # debugging)
        response.headers["X-Process-Time"] = f"{formatted_process_time}ms"

        return response