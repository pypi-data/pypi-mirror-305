# Copyright (C) 2021 Bloomberg LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  <http://www.apache.org/licenses/LICENSE-2.0>
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, Optional

from aiohttp_middlewares.annotations import UrlCollection
from aiohttp_middlewares.cors import ACCESS_CONTROL_ALLOW_CREDENTIALS, ACCESS_CONTROL_ALLOW_ORIGIN

from buildgrid._protos.build.bazel.remote.execution.v2.remote_execution_pb2 import ActionResult
from buildgrid.server.settings import (
    BROWSER_BLOB_CACHE_MAX_LENGTH,
    BROWSER_BLOB_CACHE_TTL,
    BROWSER_RESULT_CACHE_MAX_LENGTH,
    BROWSER_RESULT_CACHE_TTL,
)
from buildgrid.server.utils.async_lru_cache import LruCache

TARBALL_DIRECTORY_PREFIX = "bgd-browser-tarball-"


def get_cors_headers(origin: Optional[str], origins: UrlCollection, allow_all: bool) -> Dict[str, str]:
    headers = {}
    if origin:
        headers[ACCESS_CONTROL_ALLOW_CREDENTIALS] = "true"
        if origin in origins:
            headers[ACCESS_CONTROL_ALLOW_ORIGIN] = origin
        elif allow_all:
            headers[ACCESS_CONTROL_ALLOW_ORIGIN] = "*"
    return headers


class ResponseCache:
    def __init__(self) -> None:
        self._action_results: LruCache[ActionResult] = LruCache(BROWSER_RESULT_CACHE_MAX_LENGTH)
        self._blobs: LruCache[bytes] = LruCache(BROWSER_BLOB_CACHE_MAX_LENGTH)

    async def store_action_result(self, key: str, result: ActionResult) -> None:
        await self._action_results.set(key, result, BROWSER_RESULT_CACHE_TTL)

    async def get_action_result(self, key: str) -> Optional[ActionResult]:
        return await self._action_results.get(key)

    async def store_blob(self, key: str, blob: bytes) -> None:
        await self._blobs.set(key, blob, BROWSER_BLOB_CACHE_TTL)

    async def get_blob(self, key: str) -> Optional[bytes]:
        return await self._blobs.get(key)
