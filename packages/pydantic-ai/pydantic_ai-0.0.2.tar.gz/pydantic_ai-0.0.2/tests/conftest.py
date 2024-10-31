from __future__ import annotations as _annotations

import importlib.util
import os
import re
import secrets
import sys
from datetime import datetime
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING, Any, Callable

import httpx
import pytest
from _pytest.assertion.rewrite import AssertionRewritingHook
from typing_extensions import TypeAlias

__all__ = 'IsNow', 'TestEnv'

if TYPE_CHECKING:

    def IsNow(*args: Any, **kwargs: Any) -> datetime: ...
else:
    from dirty_equals import IsNow

try:
    from logfire.testing import CaptureLogfire
except ImportError:
    pass
else:

    @pytest.fixture(autouse=True)
    def logfire_disable(capfire: CaptureLogfire):
        pass


class TestEnv:
    __test__ = False

    def __init__(self):
        self.envars: set[str] = set()

    def set(self, name: str, value: str) -> None:
        self.envars.add(name)
        os.environ[name] = value

    def pop(self, name: str) -> None:  # pragma: no cover
        self.envars.remove(name)
        os.environ.pop(name)

    def clear(self) -> None:
        for n in self.envars:
            os.environ.pop(n)


@pytest.fixture
def env():
    test_env = TestEnv()

    yield test_env

    test_env.clear()


@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest.fixture
async def client_with_handler():
    client: httpx.AsyncClient | None = None

    def create_client(handler: Callable[[httpx.Request], httpx.Response]) -> httpx.AsyncClient:
        nonlocal client
        assert client is None, 'client_with_handler can only be called once'
        client = httpx.AsyncClient(mounts={'all://': httpx.MockTransport(handler)})
        return client

    try:
        yield create_client
    finally:
        if client:  # pragma: no cover
            await client.aclose()


ClientWithHandler: TypeAlias = Callable[[Callable[[httpx.Request], httpx.Response]], httpx.AsyncClient]


# pyright: reportUnknownMemberType=false, reportUnknownArgumentType=false
@pytest.fixture
def create_module(tmp_path: Path, request: pytest.FixtureRequest) -> Callable[[str], Any]:
    """Taken from `pydantic/tests/conftest.py`, create module object, execute and return it."""

    def run(
        source_code: str,
        rewrite_assertions: bool = True,
        module_name_prefix: str | None = None,
    ) -> ModuleType:
        """Create module object, execute and return it.

        Can be used as a decorator of the function from the source code of which the module will be constructed.

        Args:
            source_code: Python source code of the module
            rewrite_assertions: whether to rewrite assertions in module or not
            module_name_prefix: string prefix to use in the name of the module, does not affect the name of the file.

        """

        # Max path length in Windows is 260. Leaving some buffer here
        max_name_len = 240 - len(str(tmp_path))
        # Windows does not allow these characters in paths. Linux bans slashes only.
        sanitized_name = re.sub('[' + re.escape('<>:"/\\|?*') + ']', '-', request.node.name)[:max_name_len]
        module_name = f'{sanitized_name}_{secrets.token_hex(5)}'
        path = tmp_path / f'{module_name}.py'
        path.write_text(source_code)
        filename = str(path)

        if module_name_prefix:
            module_name = module_name_prefix + module_name

        if rewrite_assertions:
            loader = AssertionRewritingHook(config=request.config)
            loader.mark_rewrite(module_name)
        else:
            loader = None

        spec = importlib.util.spec_from_file_location(module_name, filename, loader=loader)
        sys.modules[module_name] = module = importlib.util.module_from_spec(spec)  # pyright: ignore[reportArgumentType]
        spec.loader.exec_module(module)  # pyright: ignore[reportOptionalMemberAccess]
        return module

    return run
