import json
from fastapi import FastAPI, applications
from contextlib import asynccontextmanager
import asyncio
from pg_objectserialization import loads, dumps
import uvicorn
from starlette.datastructures import MutableHeaders
from pg_common import log_info, log_error, start_coroutines, base64_decode, base64_encode
from pg_environment import config
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from .define import ENV_NEEDS_BODY_MIDDLEWARE, \
    ENV_NEEDS_GAME_CONFIG, ENV_NEEDS_GAME_PROPERTY
from .manager import GameConfigManager, GamePropertyManager
CODE_VERSION = 0

__all__ = [
           "run", "app", "CODE_VERSION"
           ]
__auth__ = "baozilaji@gmail.com"


def swagger_ui_html_patch(*args, **kwargs):
    return get_swagger_ui_html(*args, **kwargs,
                               swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
                               swagger_css_url="/static/swagger-ui/swagger-ui.css")

applications.get_swagger_ui_html = swagger_ui_html_patch

@asynccontextmanager
async def life_span(_app: FastAPI):
    from pg_httpserver import httpserver_init
    httpserver_init()
    start_coroutines(reload_config())
    log_info("http server startup")
    yield
    global _RUNNING
    _RUNNING = False
    log_info("http server shutdown")


app = FastAPI(docs_url=None if config.is_prod() else "/docs", lifespan=life_span)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_RUNNING = True


def reload_code_version():
    global CODE_VERSION
    if not CODE_VERSION:
        with open("VERSION") as _f:
            CODE_VERSION = int(_f.read())
            log_info(f"code version is: {CODE_VERSION}")


async def reload_config():
    while _RUNNING:
        try:
            reload_code_version()
            if config.get_conf(ENV_NEEDS_GAME_CONFIG, False):
                await GameConfigManager.reload()
            if config.get_conf(ENV_NEEDS_GAME_PROPERTY, False):
                await GamePropertyManager.reload()
        except Exception as e:
            log_error(e)
        await asyncio.sleep(60)
    log_info(f"server stopped")


@app.get("/health", description="健康检查接口", response_description="返回代码版本号")
async def health():
    return {
        "status": 0,
        "info": "OK",
        "code_version": CODE_VERSION
    }

class _CustomBodyResponder:
    def __init__(self, _app):
        self.app = _app
        self.initial_message = {}

    async def __call__(self, scope, receive, send) -> None:
        self.receive = receive
        self.send = send
        await self.app(scope, self.receive_with_msg, self.send_with_msg)

    async def receive_with_msg(self):
        message = await self.receive()
        _body: bytes = message.get("body", b"")
        if _body:
            _body = base64_decode(_body)
            _body = loads(_body)
            _body = json.dumps(_body)
            _body = _body.encode()
            message["body"] = _body
        return message
    async def send_with_msg(self, message):
        if message["type"] == "http.response.start":
            self.initial_message = message
            return

        elif message["type"] == "http.response.body":
            headers = MutableHeaders(raw=self.initial_message['headers'])
            body = message['body']
            body = body.decode()
            body = base64_encode(dumps(body))
            message["body"] = body
            headers["Content-Type"] = "text/plain"
            headers["Content-Length"] = str(len(body))
            self.initial_message['headers'] = headers.items()
            await self.send(self.initial_message)
            await self.send(message)

class CustomBodyMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http" or scope["method"] != "POST":
            await self.app(scope, receive, send)
            return

        responder = _CustomBodyResponder(self.app)
        await responder(scope, receive, send)

if config.get_conf(ENV_NEEDS_BODY_MIDDLEWARE, default=True):
    log_info(f"add custom middleware to encrypt response and decrypt request")
    app.add_middleware(CustomBodyMiddleware)


def run(port=None):
    uvicorn.run(app="pg_httpserver.fapi:app", host=config.get_host(),
                port=config.get_port() if port is None else port)