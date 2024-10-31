import httpx
from fastapi.responses import StreamingResponse
from starlette.background import BackgroundTask

from vmc.context.request import request
from vmc.types.errors import VMCException


class VMC:
    def __init__(self, port: int, host: str = "localhost"):
        self.host = host
        self.port = port
        self.client = httpx.AsyncClient(base_url=f"http://{self.host}:{self.port}", timeout=60)

    def __getattr__(self, name):
        """Redirects all calls to the VMC server"""

        async def _(**kwargs):
            req = request.get()
            http_req = self.client.build_request(
                req.method,
                url=req.url.path,
                content=req.scope["body"],
                headers=req.headers,
            )
            try:
                res = await self.client.send(http_req, stream=True)
            except Exception:
                raise VMCException(http_code=500, vmc_code=500, msg="Failed to connect to VMC")
            return StreamingResponse(
                content=res.aiter_text(),
                headers=res.headers,
                status_code=res.status_code,
                background=BackgroundTask(res.close),
            )

        return _
