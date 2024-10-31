from pg_resourceloader import LoaderManager
from pg_common import FuncDecoratorManager
from pg_environment import config


__all__ = [
    "ENV_HANDLER_DIR", "httpserver_init", "ENV_NEEDS_BODY_MIDDLEWARE", "ENV_NEEDS_GZIP_BODY",
    "ENV_GZIP_BODY_LENGTH", "ENV_GZIP_COMPRESS_LEVEL", "ENV_NEEDS_GAME_CONFIG", "ENV_NEEDS_GAME_PROPERTY"
]
__auth__ = "baozilaji@gmail.com"


ENV_HANDLER_DIR = "handler_dir"
ENV_NEEDS_BODY_MIDDLEWARE = "needs_body_middleware"
ENV_NEEDS_GZIP_BODY = "needs_gzip_body"
ENV_GZIP_BODY_LENGTH = "gzip_body_length"
ENV_GZIP_COMPRESS_LEVEL = "gzip_compress_level"
ENV_NEEDS_GAME_CONFIG = "needs_game_config"
ENV_NEEDS_GAME_PROPERTY = "needs_game_property"
"""
http server configuration
{
  "handler_dir": "handler",
  "needs_body_middleware": true,
  "needs_gzip_body": true,
  "gzip_body_length": 100,
  "gzip_compress_level": 5,
  "needs_game_config": false,
  "needs_game_property": false
}
"""


def httpserver_init():
    FuncDecoratorManager.scan_decorators(config.get_conf(ENV_HANDLER_DIR, "handlers"))
    LoaderManager.scan_loaders()
